from django.contrib import admin
from .models import Info, Images, Job_Vacancies, Team, Subscribe, Daily_Opportunie, Job_Vacancies
# Register your models here.


admin.site.register(Info)
admin.site.register(Images)
admin.site.register(Team)
admin.site.register(Subscribe)
admin.site.register(Daily_Opportunie)
admin.site.register(Job_Vacancies)