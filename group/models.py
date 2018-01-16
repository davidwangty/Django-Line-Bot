from django.db import models


class LineGroup(models.Model):
    group_name = models.CharField(max_length=50)
    emba_group = models.ForeignKey('EMBAGroup', on_delete=models.CASCADE)
    group_line_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class EMBAGroup(models.Model):
    group_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
