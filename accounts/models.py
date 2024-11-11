# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('IMPORT EMAIL!')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)
    

# class User(AbstractBaseUser):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'  # Kullanıcı girişi için email kullanılacak
#     REQUIRED_FIELDS = ['username']  # Kayıt için gereken alanlar

#     def __str__(self):
#         return self.email