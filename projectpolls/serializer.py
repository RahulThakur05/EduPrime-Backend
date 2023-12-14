from rest_framework import serializers
from .models import Subject, Chapters, HomePhoto, VideoPhoto, SubPhoto, UserTestimonial, PDFDocument, Option, Que, QChp, \
    Videos, ChemVideos, MathsVideos, BioVideos, PYQDocument, User, LastAccessedVideo, UserProfile, Library


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['Subname']


class ChapterSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.Subname')

    class Meta:
        model = Chapters
        fields = ['Chpno', 'Chpname', 'subject']


class HomePhotoSerializer(serializers.ModelSerializer):
    subname = serializers.CharField(source='subname.Subname')

    class Meta:
        model = HomePhoto
        fields = ['subname', 'Photo']


class SubPhotoSerializer(serializers.ModelSerializer):
    subname = serializers.CharField(source='subname.Subname')

    class Meta:
        model = SubPhoto
        fields = ['subname', 'Photo']


class VideoPhotoSerializer(serializers.ModelSerializer):
    Chname = serializers.CharField(source='Chname.Chpname')

    class Meta:
        model = VideoPhoto
        fields = ['Chname', 'photo']


class UserTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestimonial
        fields = [
            'name',
            'testimonial'
        ]


class VideosSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.Subname')
    title = serializers.CharField(source='title.Chpname')

    class Meta:
        model = Videos
        fields = ['subject', 'title', 'description', 'video_url']


class ChemVideosSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.Subname')
    title = serializers.CharField(source='title.Chpname')

    class Meta:
        model = ChemVideos
        fields = ['subject', 'title', 'description', 'video_url']


class MathsVideosSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.Subname')
    title = serializers.CharField(source='title.Chpname')

    class Meta:
        model = MathsVideos
        fields = ['subject', 'title', 'description', 'video_url']


class BioVideosSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.Subname')
    title = serializers.CharField(source='title.Chpname')

    class Meta:
        model = BioVideos
        fields = ['subject', 'title', 'description', 'video_url','views']


class PDFSerializer(serializers.ModelSerializer):
    cls = serializers.CharField(source='cls.clas')

    class Meta:
        model = PDFDocument
        fields = ['cls', 'title', 'pdf_file', 'pdf_img']


class PYQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PYQDocument
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    questions = serializers.CharField(source='questions.question')

    class Meta:
        model = Option
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    subtopic = serializers.CharField(source='subtopic.subtopic')
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Que
        fields = '__all__'


class QChpSerializer(serializers.ModelSerializer):
    class Meta:
        model = QChp
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LastAccessedVideoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.Email')

    class Meta:
        model = LastAccessedVideo
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
