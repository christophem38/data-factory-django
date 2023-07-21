from django.contrib import admin
from .models import (
    Education,
    Expertise,
    Language,
    Service,
    Experience,
    ServiceDetail,
    Skill,
    SoftSkill,
)

admin.site.register(ServiceDetail)
admin.site.register(Skill)
admin.site.register(SoftSkill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(Expertise)
admin.site.register(Service)
