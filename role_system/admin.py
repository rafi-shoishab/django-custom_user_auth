from django.contrib import admin
from . models import Customuser, JobSeekerProfile, RecruiterProfile

# Register your models here.
admin.site.register(Customuser) # 
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)