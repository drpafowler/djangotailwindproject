from django.db import models
import uuid
from django_countries.fields import CountryField
# Create your models here.

class Publisher(models.Model):
    '''id: '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Publisher: {self.name} from {self.country}"