from django.db import models
# Create your models here.
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserAlexaManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class UserAlexa(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    full_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    workplace = models.CharField(max_length=200, blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    foreign_languages = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    hometown = models.CharField(max_length=200, blank=True, null=True)
    certificates = models.TextField(blank=True, null=True)
    warning_count = models.IntegerField(default=0)
    day_start = models.DateField(blank=True, null=True)
    day_end = models.DateField(blank=True, null=True)
    block_count = models.IntegerField(default=0)
    block_forever = models.BooleanField(default=False)
    hide_date_of_birth = models.BooleanField(default=False)
    hide_phone_number = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=False)
    hide_address = models.BooleanField(default=False)
    hide_workplace = models.BooleanField(default=False)
    hide_qualifications = models.BooleanField(default=False)
    hide_foreign_languages = models.BooleanField(default=False)
    hide_hobbies = models.BooleanField(default=False)
    hide_hometown = models.BooleanField(default=False)
    hide_certificates = models.BooleanField(default=False)

    # Các trường Django quản lý người dùng
    is_staff = models.BooleanField(default=False)  # Cần cho quyền truy cập vào admin
    is_superuser = models.BooleanField(default=False)  # Cần cho quyền admin

    objects = UserAlexaManager()

    USERNAME_FIELD = 'username'  # Trường xác thực
    REQUIRED_FIELDS = ['email']  # Các trường yêu cầu khi tạo user

    def get_full_name(self):
        return self.full_name or self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
