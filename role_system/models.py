from django.db import models 
from django.contrib.auth.models import AbstractUser #

# Create your models here.
class Customuser(AbstractUser): # inherit abstractuser

    ROLE_CHOICE = (
        ('job_seeker', 'Job Seeker'), # key, show 
        ('recruiter', 'Recruiter')
    )

    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICE) # 

class RecruiterProfile(models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return f"Recruiter {self.user.username}"
    
class JobSeekerProfile (models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE) #
    skills = models.CharField()
    bio = models.TextField()
    
    def __str__(self):
        return f"Seeker {self.user.username}"
    