from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoice(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")
    name = models.CharField(max_length=180, default="",)
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    room = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoice.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField("rooms.Amenity",)
    def __str__(self) -> str:
        return self.name

class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Amenities"