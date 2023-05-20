from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# participant model
class UserManager(BaseUserManager):
    @staticmethod
    def validate_field(field):
        if not field:
            raise ValueError('The {0} field is required'.format(field))

    def create_user(self, username, email, password, **kwargs):
        self.validate_field(username)
        self.validate_field(email)
        self.validate_field(password)

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(username, email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class Participant(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username