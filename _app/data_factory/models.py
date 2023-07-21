from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200)


class Expertise(models.Model):
    title = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill, related_name="expertises", on_delete=models.CASCADE)


class ServiceDetail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.ManyToManyField(ServiceDetail)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


class Education(models.Model):
    title = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


class SoftSkill(models.Model):
    skill = models.ForeignKey(Skill, related_name="skills", on_delete=models.CASCADE)


class Language(models.Model):
    lang = models.ForeignKey(Skill, related_name="languages", on_delete=models.CASCADE)
