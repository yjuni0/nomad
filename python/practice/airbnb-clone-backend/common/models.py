from django.db import models

#다른 model에서 사용하게 하는 model 생성
# Create your models here.
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
# django가 db에 저장하지 않도록 함(abstract)
    class Meta:
        abstract = True
    