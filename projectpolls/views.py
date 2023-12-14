import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Chapters, HomePhoto, VideoPhoto, SubPhoto, UserTestimonial, PDFDocument, Option, Que, QChp, Videos, \
    ChemVideos, MathsVideos, BioVideos, PYQDocument, User, LastAccessedVideo, UserProfile, Library, Subject
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q, Sum
from rest_framework.response import Response
from .serializer import ChapterSerializer, HomePhotoSerializer, VideoPhotoSerializer, SubPhotoSerializer, \
    UserTestimonialSerializer, PDFSerializer, OptionSerializer, QuestionSerializer, QChpSerializer, \
    VideosSerializer, ChemVideosSerializer, MathsVideosSerializer, BioVideosSerializer, PYQSerializer, UserSerializer, \
    LastAccessedVideoSerializer, LibrarySerializer, UserProfileSerializer
from django.contrib.auth.hashers import check_password
from django.core import serializers


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer


class HomePhotoViewSet(viewsets.ModelViewSet):
    queryset = HomePhoto.objects.all()
    serializer_class = HomePhotoSerializer


class SubPhotoViewSet(viewsets.ModelViewSet):
    queryset = SubPhoto.objects.all()
    serializer_class = SubPhotoSerializer


class VideoPhotoViewSet(viewsets.ModelViewSet):
    queryset = VideoPhoto.objects.all()
    serializer_class = VideoPhotoSerializer


class UserTestimonialViewSet(viewsets.ModelViewSet):
    queryset = UserTestimonial.objects.all()
    serializer_class = UserTestimonialSerializer


class VideosViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer


class ChemVideosViewSet(viewsets.ModelViewSet):
    queryset = ChemVideos.objects.all()
    serializer_class = ChemVideosSerializer


class MathsVideosViewSet(viewsets.ModelViewSet):
    queryset = MathsVideos.objects.all()
    serializer_class = MathsVideosSerializer


class BioVideosViewSet(viewsets.ModelViewSet):
    queryset = BioVideos.objects.all()
    serializer_class = BioVideosSerializer


class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFSerializer


class PYQViewSet(viewsets.ModelViewSet):
    queryset = PYQDocument.objects.all()
    serializer_class = PYQSerializer


class PYQListByExamAndYear(generics.ListAPIView):
    serializer_class = PYQSerializer

    def get_queryset(self):
        exam_name = self.kwargs['exam_name']
        year = self.kwargs['year']
        queryset = PYQDocument.objects.filter(Exam=exam_name, year=year)
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Que.objects.all()
    serializer_class = QuestionSerializer


class QueChViewSet(viewsets.ModelViewSet):
    queryset = QChp.objects.all()
    serializer_class = QChpSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class UserProfileDetailView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        email = self.kwargs.get('email')  # Assuming you pass the email as a URL parameter
        try:
            user = User.objects.get(Email=email)  # Retrieve the user by email
            user_profile = UserProfile.objects.get(user=user)  # Get the UserProfile related to the user
            return user_profile
        except User.DoesNotExist:
            return Response({'error': 'User not found for this email.'}, status=status.HTTP_404_NOT_FOUND)
        except UserProfile.DoesNotExist:
            return Response({'error': 'UserProfile not found for this email.'}, status=status.HTTP_404_NOT_FOUND)


class LastVideoViewSet(generics.ListAPIView):
    serializer_class = LastAccessedVideoSerializer

    def get_queryset(self):
        email = self.kwargs.get('email')

        # Retrieve the user object based on the email
        try:
            user = User.objects.get(Email=email)
        except User.DoesNotExist:
            # Handle the case where the user with the provided email does not exist
            return LastAccessedVideo.objects.none()

        # Filter videos based on the retrieved user object
        queryset = LastAccessedVideo.objects.filter(user=user)
        return queryset


class VideosBySubjectAndChapterView(generics.ListAPIView):
    serializer_class = VideosSerializer

    def get_queryset(self):
        subject = self.kwargs.get('subject')
        chapter = self.kwargs.get('chapter')

        # Filter videos based on subject and chapter
        queryset = Videos.objects.filter(subject__Subname=subject, title__Chpname=chapter)
        return queryset


def search_lectures(request):
    query = request.GET.get('search', '')

    # Assuming you want to search in all subject videos, you can use Q objects for complex queries.
    videos = Videos.objects.filter(Q(title__Chpname__icontains=query) | Q(description__icontains=query)).values('id',
                                                                                                                'subject_id',
                                                                                                                'title__Chpname',
                                                                                                                'description',
                                                                                                                'video_url')
    chem_videos = ChemVideos.objects.filter(
        Q(title__Chpname__icontains=query) | Q(description__icontains=query)).values('id', 'subject_id',
                                                                                     'title__Chpname', 'description',
                                                                                     'video_url')
    maths_videos = MathsVideos.objects.filter(
        Q(title__Chpname__icontains=query) | Q(description__icontains=query)).values('id', 'subject_id',
                                                                                     'title__Chpname', 'description',
                                                                                     'video_url')
    bio_videos = BioVideos.objects.filter(Q(title__Chpname__icontains=query) | Q(description__icontains=query)).values(
        'id', 'subject_id', 'title__Chpname', 'description', 'video_url')

    # Combine all results into a single list.
    all_videos = list(videos) + list(chem_videos) + list(maths_videos) + list(
        bio_videos)

    return JsonResponse(all_videos, safe=False)


@csrf_exempt
def save_testimonial_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        testimonial = request.POST.get('testimonial')

        UserTestimonial.objects.create(name=name, testimonial=testimonial)

        return JsonResponse({'message': 'Data saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@api_view(['GET'])
def get_question_options(request, question_id):
    try:
        options = Option.objects.filter(questions_id=question_id)
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)
    except Option.DoesNotExist:
        return Response({'error': 'Options not found'}, status=404)


from rest_framework.decorators import api_view


@api_view(['GET'])
def get_questions_and_options_by_subtopic(request, subtopic_id):
    try:
        # First, retrieve the subtopic based on its ID
        subtopic = QChp.objects.get(pk=subtopic_id)

        # Next, retrieve all questions related to the subtopic
        questions = Que.objects.filter(subtopic=subtopic)

        # Serialize the questions and their options
        question_serializer = QuestionSerializer(questions, many=True)

        option_serializer = OptionSerializer(Option.objects.filter(questions__in=questions), many=True)

        # Create a dictionary to combine questions and options
        data = {
            'questions': question_serializer.data,
            'options': option_serializer.data,
        }

        return Response(data)
    except QChp.DoesNotExist:
        return Response({'error': 'Subtopic not found'}, status=404)


@api_view(['GET'])
def get_3questions_and_options_by_subtopic(request):
    subtopic_ids = request.GET.getlist('subtopic_id')  # Get a list of subtopic IDs from the query parameters

    # Ensure that only three subtopic IDs are selected (you can add additional validation logic if needed)
    if len(subtopic_ids) != 3:
        return Response({'error': 'Please select exactly three subtopic IDs.'}, status=400)

    try:
        # Retrieve all questions related to the specified subtopic IDs
        questions = Que.objects.filter(subtopic__in=subtopic_ids)

        # Serialize the questions and their options
        question_serializer = QuestionSerializer(questions, many=True)

        option_serializer = OptionSerializer(
            Option.objects.filter(questions__in=questions), many=True
        )

        # Create a dictionary to combine questions and options
        data = {
            'questions': question_serializer.data,
            'options': option_serializer.data,
        }

        return Response(data)
    except Que.DoesNotExist:
        return Response({'error': 'No questions found for the specified subtopics.'}, status=404)


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('Name')
            email = serializer.validated_data.get('Email')
            number = serializer.validated_data.get('Num')
            password = serializer.validated_data.get('Pass')

            # Check if the user already exists with the given email
            if User.objects.filter(Email=email).exists():
                return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate name
            if not name.isalpha():
                return Response({'error': 'Name should only contain characters.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate phone number
            if not number.isdigit() or len(number) != 10:
                return Response({'error': 'Phone number should only contain digits and have a length of 10.'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Validate password length
            if len(password) < 8:
                return Response({'error': 'Password length should be at least 8 characters.'},
                                status=status.HTTP_400_BAD_REQUEST)

            User.objects.create(Name=name, Email=email, Num=number, Pass=password)
            return JsonResponse({'message': 'Data saved successfully'})
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('Email')
        password = request.data.get('Pass')
        user = User.objects.filter(Email=email).first()
        if user is None:
            return JsonResponse({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        stored_password = user.Pass

        if password == stored_password:
            return JsonResponse({'message': 'Login successfully'})
        else:
            return JsonResponse({'error': 'Incorrect password.'}, status=status.HTTP_401_UNAUTHORIZED)

    else:
        return JsonResponse({'error': 'Invalid request method'})


def user_detail_api(request, email):
    user = get_object_or_404(User, Email=email)
    data = {
        'name': user.Name,
        'email': user.Email,
        'num': user.Num,
        # Add more fields as needed
    }
    return JsonResponse(data)


@csrf_exempt
@permission_classes([IsAuthenticated])
def update_last_played_video(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_email = data.get('User-Email')
            video_url = data.get('video_url')
            video_title = data.get('video_title')
            video_description = data.get('video_description')
            user = User.objects.get(Email=user_email)

            last_accessed_video, created = LastAccessedVideo.objects.get_or_create(user=user)

            last_accessed_video.last_accessed_video_url = video_url
            last_accessed_video.last_accessed_video_title = video_title
            last_accessed_video.last_accessed_video_description = video_description
            last_accessed_video.save()

            return JsonResponse({'message': 'Last played video updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'})
        except Exception as e:
            return JsonResponse({'error': f'Error: {str(e)}'})

    return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
@permission_classes([IsAuthenticated])
def increment_total_quizzes_attended(request):
    data = json.loads(request.body)
    user_email = data.get('User-Email')

    print(f'Received POST request for user_email: {user_email}')

    try:
        user = User.objects.get(Email=user_email)
    except User.DoesNotExist:
        print('User not found')
        return JsonResponse({'message': 'User not found'}, status=404)

    try:
        user_profile, created = UserProfile.objects.get_or_create(user=user)

        # Check if 'IncrementQuestionsAttended' is present in the JSON payload
        if data.get('IncrementQuestionsAttended'):
            user_profile.questions_attended += 1
            user_profile.save()

        print('Total quizzes attended updated successfully')
        return JsonResponse({'message': 'Total quizzes attended updated successfully'}, status=200)
    except Exception as e:
        print(f'Error: {e}')
        return JsonResponse({'message': 'Error occurred while updating total quizzes attended'}, status=500)


@csrf_exempt
@permission_classes([IsAuthenticated])
def update_totalminwatched(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_email = data.get('User-Email')
            total_min_watched = data.get('totalminwatched')
            print(data);

            if not user_email or not total_min_watched:
                return JsonResponse({'message': 'Missing required fields'}, status=400)

            user = User.objects.filter(Email=user_email).first()

            if not user:
                return JsonResponse({'message': 'User not found'}, status=404)

            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.total_minutes_watched += total_min_watched
            user_profile.save()

            return JsonResponse({'message': 'Total minutes watched updated successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


@api_view(['POST'])
def update_password(request):
    if request.method == 'POST':
        email = request.data.get('Email')
        new_password = request.data.get('NewPassword')

        try:
            user = User.objects.get(Email=email)
            user.Pass = new_password
            user.save()

            return JsonResponse({'message': 'Password updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({'error': 'Invalid request method'})


# views.py

@api_view(['POST'])
def update_view_count(request):
    try:
        video_url = request.data.get('video_url')
        video = BioVideos.objects.get(video_url=video_url)
        video.views += 1
        video.save()
        return Response(status=status.HTTP_200_OK)
    except BioVideos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def most_played_videos(request):
    videos = BioVideos.objects.order_by('-views')[:10]  # Get the top 10 most played videos
    serializer = BioVideosSerializer(videos, many=True)
    return Response(serializer.data)


# ----------------Report Generation views----------------------------------


def subject_report(request):
    return render(request, 'subject_report.html', {})


def subject_report_data(request):
    subjects = Subject.objects.all()

    data = []
    for subject in subjects:
        video_count = (
                Videos.objects.filter(subject=subject).count() +
                ChemVideos.objects.filter(subject=subject).count() +
                MathsVideos.objects.filter(subject=subject).count() +
                BioVideos.objects.filter(subject=subject).count()
        )
        data.append({
            "Subject.Subname": subject.Subname,
            "Videos Count": video_count
        })

    return JsonResponse(data, safe=False)


def video_report(request):
    return render(request, 'video_view_chp.html', {})


def video_views_by_chapter_data(request):
    chapters = Chapters.objects.all()

    data = []
    for chapter in chapters:
        video_views = BioVideos.objects.filter(title=chapter).aggregate(Sum('views'))['views__sum'] or 0
        data.append({
            "Chapters.Chpname": f"{chapter.Chpname} {chapter.Chpno}",
            "Videos Views": video_views
        })

    return JsonResponse(data, safe=False)


def question_report(request):
    return render(request, 'question_report.html', {})


def question_report_data(request):
    subtopics = QChp.objects.all()
    data = []

    for subtopic in subtopics:
        questions = Que.objects.filter(subtopic=subtopic)
        question_data = []

        for question in questions:
            options = Option.objects.filter(questions=question)
            option_data = [option.option for option in options]

            question_data.append({
                "Question": question.question,
                "Correct Answer": question.correct_ans,
                "Options": ", ".join(option_data)
            })

        data.append({
            "Subtopic": subtopic.subtopic,
            "Questions": question_data,
            "Total Questions": len(question_data)  # Count the total number of questions for this subtopic
        })

    return JsonResponse(data, safe=False)


def question_attend_report(request):
    return render(request, 'quiz_attened.html', {})


def user_questions_attended_data(request):
    user_profiles = UserProfile.objects.all()
    data = []

    for user_profile in user_profiles:
        data.append({
            "Name": user_profile.user.Name,
            "Total Questions Attended": user_profile.questions_attended
        })

    return JsonResponse(data, safe=False)


def subject_stats_report(request):
    return render(request, 'subject_stats.html', {})


def subject_stats_report_data(request):
    data = []

    # Retrieve data from the BioVideos model
    queryset = BioVideos.objects.all()

    for item in queryset:
        # Retrieve the UserProfile related to the User in the BioVideos model
        try:
            user_profile = UserProfile.objects.get(user=item.subject.user)
        except UserProfile.DoesNotExist:
            user_profile = None

        data.append({
            'subject': item.subject.name,
            'total_quizzes_attended': user_profile.total_quizzes_attended if user_profile else 0,
            'views': item.views,
        })

    return JsonResponse(data, safe=False)
