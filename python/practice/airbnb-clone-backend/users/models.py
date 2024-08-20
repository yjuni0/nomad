from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "MALE")
        FEMALE = ("female", "FEMALE")

    class LanguageChoice(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoice(models.TextChoices):
        KRW = ("krw", "Korean won")
        USD = ("usd", "Us dollar")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(blank=True)
    name = models.CharField(
        max_length=150,
        default="",
    )  # CharField 는 null이 될 수 없음
    is_host = models.BooleanField(
        default=False,
    )  # in_host 는 null이 될 수 없음
    # 새로운 column을 만들었을 때 이전 사용자들은 null 값을 갖는다. 때문에 default 값을 추가해 줌
    # 또는 null = True 를 사용해 설정할 수 있따...
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoice.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoice.choices,
    )
