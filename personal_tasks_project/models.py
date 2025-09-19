import uuid
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    u_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)   

    class Meta:
        abstract = True