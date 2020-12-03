from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Empty email field')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def get_by_natural_key(self, username):
        user = self.get(**{self.model.USERNAME_FIELD: username})
        return user


class Users(AbstractBaseUser):
    user_type = [('guest', 'Ziyaretçi'), ('student', 'Öğrenci'), ('staff', 'Akademik Personel')]
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True, max_length=255)
    user_type = models.CharField(choices=user_type, max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "db_user"

