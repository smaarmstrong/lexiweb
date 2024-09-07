from django.db import models
from django.utils import timezone


class Text(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    file_source = models.FileField(upload_to="texts/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Link(models.Model):  # Changed from Highlight to Link
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name="links")
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    linked_word = models.CharField(max_length=255)
    footnote = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Link in {self.text.title}: {self.linked_word}"
