from django.db import models


class Subject(models.Model):
    Subname = models.CharField(max_length=100)

    def __str__(self):
        return self.Subname


class Chapters(models.Model):
    Chpno = models.IntegerField()
    Chpname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.Chpname + str(self.Chpno)


class HomePhoto(models.Model):
    subname = models.ForeignKey(Subject, default=1, on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to='images', default="")


class SubPhoto(models.Model):
    subname = models.ForeignKey(Subject, default=1, on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to='images', default="")


class VideoPhoto(models.Model):
    Chname = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images')


class UserTestimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()


class Videos(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    description = models.TextField()
    video_url = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title)


class ChemVideos(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    description = models.TextField()
    video_url = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title)


class MathsVideos(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    description = models.TextField()
    video_url = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title)


class BioVideos(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    description = models.TextField()
    video_url = models.CharField(max_length=300)
    views = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Class(models.Model):
    clas = models.IntegerField()

    def __str__(self):
        return str(self.clas)


class PDFDocument(models.Model):
    cls = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')
    pdf_img = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return str(self.cls) + ' ' + self.title


class PYQDocument(models.Model):
    Exam = models.CharField(max_length=100)
    year = models.IntegerField()
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return str(self.year) + ' ' + self.Exam


class QChp(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    subtopic = models.CharField(max_length=100)

    def __str__(self):
        return self.subtopic


class Que(models.Model):
    subtopic = models.ForeignKey(QChp, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    correct_ans = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Option(models.Model):
    questions = models.ForeignKey(Que, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)


class User(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Email = models.EmailField(unique=True)
    Num = models.CharField(max_length=12,null=True)
    Pass = models.CharField(max_length=100, default='')


class LastAccessedVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    last_accessed_video_url = models.CharField(max_length=300)
    last_accessed_video_title = models.CharField(max_length=255)
    last_accessed_video_description = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questions_attended = models.PositiveIntegerField(default=0)
    total_minutes_watched = models.IntegerField(default=0)
    total_quizzes_attended = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.Name


class Library(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/')
    pdf_img = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.title
