# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class CustomUser(AbstractUser):
#     full_name = models.CharField(max_length=500)
#     username = models.CharField(max_length=50, null=True, blank=True, unique=True)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     password = models.CharField(max_length=16)
#     address = models.TextField(null=True, blank=True)
#     dob = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True, default=None)
#     mobile = models.CharField(max_length=15, null=True, blank=True)
#     phone = models.CharField(max_length=25, null=True, blank=True)
#     user_type = models.CharField(max_length=10)
#     specialization = models.CharField(max_length=100, null=True, blank=True, default=None)
#     degree = models.CharField(max_length=500, null=True, blank=True, default=None)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'user_master'
#
#     def __str__(self):
#         return self.username
