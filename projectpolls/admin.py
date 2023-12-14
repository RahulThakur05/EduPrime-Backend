from django.contrib import admin
from .models import Subject, Chapters, HomePhoto, VideoPhoto, SubPhoto, UserTestimonial, Class, PDFDocument, Option, \
    Que, QChp, Videos, ChemVideos, MathsVideos, BioVideos, PYQDocument, User, LastAccessedVideo, UserProfile, Library

admin.site.register(Subject)
admin.site.register(Chapters)
admin.site.register(HomePhoto)
admin.site.register(SubPhoto)
admin.site.register(VideoPhoto)
admin.site.register(UserTestimonial)
admin.site.register(Videos)
admin.site.register(ChemVideos)
admin.site.register(MathsVideos)
admin.site.register(BioVideos)
admin.site.register(PYQDocument)
admin.site.register(Class)
admin.site.register(PDFDocument)
admin.site.register(Que)
admin.site.register(Option)
admin.site.register(QChp)
admin.site.register(User)
admin.site.register(LastAccessedVideo)
admin.site.register(UserProfile)
admin.site.register(Library)
