from django.db import models

class Mooc(models.Model):

    info = models.CharField(max_length=255)
    starting_date = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    enroll_url = models.URLField(blank=True)

    position = models.IntegerField(default=True)

    # description
    introduction = models.TextField()
    what_you_will_learn = models.TextField()
    what_skills_will_you_need = models.TextField()
    duration_of_the_course = models.TextField()

    def __str__(self, **kwargs):
        return self.info


class Module(models.Model):

    mooc = models.ForeignKey(Mooc)
    info = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self, **kwargs):
        return self.info

    def info_parts(self, **kwargs):
        return self.info.split(': ')
