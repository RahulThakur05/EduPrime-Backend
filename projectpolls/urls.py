from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import save_testimonial_data, get_question_options, VideosBySubjectAndChapterView, user_login, \
    register_user, update_last_played_video, increment_total_quizzes_attended, update_totalminwatched, update_password, \
    UserProfileDetailView

router = DefaultRouter()
router.register("Chapters", views.ChapterViewSet.as_view({'get': 'list'}), basename='chapter'),
router.register("HomePhoto", views.HomePhotoViewSet.as_view({'get': 'list'}), basename='photo'),
router.register("SubPhoto", views.SubPhotoViewSet.as_view({'get': 'list'}), basename='subphoto'),
router.register("VideoPhoto", views.VideoPhotoViewSet.as_view({'get': 'list'}), basename='photo'),
router.register("user-testimonial", views.UserTestimonialViewSet.as_view({'get': 'list'}), basename='testimonial'),
router.register("Lecture", views.VideosViewSet.as_view({'get': 'list'}), basename='lecture'),
router.register("PDF", views.PDFViewSet.as_view({'get': 'list'}), basename='Pdf'),


urlpatterns = [

    path("Chapters", views.ChapterViewSet.as_view({'get': 'list'})),
    path("HomePhoto", views.HomePhotoViewSet.as_view({'get': 'list'})),
    path("SubPhoto", views.SubPhotoViewSet.as_view({'get': 'list'})),
    path("Subtopic", views.QueChViewSet.as_view({'get': 'list'})),
    path("VideoPhoto", views.VideoPhotoViewSet.as_view({'get': 'list'})),
    path('save_testimonial_data/', save_testimonial_data, name='save_testimonial_data'),
    path('view_user_data/', views.UserTestimonialViewSet.as_view({'get': 'list'})),
    path("VideoLecture/", views.VideosViewSet.as_view({'get': 'list'}), name="video-lecture-list"),
    path("chemVideoLecture/", views.ChemVideosViewSet.as_view({'get': 'list'}), name="chem-video-lecture-list"),
    path("mathsVideoLecture/", views.MathsVideosViewSet.as_view({'get': 'list'}), name="Maths-video-lecture-list"),
    path("bioVideoLecture/", views.BioVideosViewSet.as_view({'get': 'list'}), name="Bio-video-lecture-list"),
    path("PDFView/", views.PDFViewSet.as_view({'get': 'list'}), name="PdfView"),
    path("PYQView/", views.PYQViewSet.as_view({'get': 'list'}), name="PyqView"),
    path("Question/", views.QuestionViewSet.as_view({'get': 'list'}), name="question"),
    path("Options/", views.OptionViewSet.as_view({'get': 'list'}), name="option"),
    path('questions/<int:question_id>/options/', get_question_options, name='get_question_options'),
    path('api/questions/<int:subtopic_id>/', views.get_questions_and_options_by_subtopic,
         name='get_questions_by_subtopic'),
    path('api/questions/', views.get_3questions_and_options_by_subtopic, name='get_questions_by_subtopic'),
    path('videos/<str:subject>/<str:chapter>/', VideosBySubjectAndChapterView.as_view(),
         name='videos-by-subject-chapter'),
    path('pyq/<str:exam_name>/<str:year>/', views.PYQListByExamAndYear.as_view(), name='pyq-list'),
    path('searchVideoLecture/', views.search_lectures, name='search_lectures'),
    path('login/', user_login, name='user_login'),
    path('register/', views.register_user, name='register'),
    path('api/user/<str:email>/', views.user_detail_api, name='user_detail_api'),
    path('update_last_played_video/', update_last_played_video, name='update_last_played_video'),
    path('lastVideo/<str:email>/',views.LastVideoViewSet.as_view(), name='last-video'),
    path('total_quizz/', increment_total_quizzes_attended, name='total_quizzes'),
    path('total_min/', update_totalminwatched, name='total_min'),
    path('reset_password/', update_password, name='reset_passwd'),
    path("Library/", views.LibraryViewSet.as_view({'get': 'list'}), name="library"),
    path("usr_details/<str:email>/", UserProfileDetailView.as_view(), name="user-details"),
    path('update_view_count/', views.update_view_count, name='update_view_count'),
    path('most_played_videos/', views.most_played_videos, name='most_played_videos'),
    path('subject_report', views.subject_report, name='subject_report'),
    path('subreport', views.subject_report_data, name='subject_report_data'),
    path('video_report', views.video_report, name='video_report'),
    path('video_views_by_chapter/', views.video_views_by_chapter_data, name='video_views_by_chapter_data'),
    path('question_report', views.question_report, name='question_report'),
    path('question_report_data/', views.question_report_data, name='question_report_data'),
    path('question_attended_report', views.question_attend_report, name='question_attend_report'),
    path('questions_attended/', views.user_questions_attended_data,
         name='user_questions_attended_data'),
    path('subject_stats_report', views.subject_stats_report, name='question_attend_report'),
    path('subject_stats_report_data/', views.subject_stats_report_data, name='subject_stats_report_data'),

]

