from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(
        blank=True, null=True
    )  # Store the content of the file here
    file_source = models.FileField(
        upload_to="", blank=True, null=True
    )  # Temporary file upload, not saved
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Read and store the file content without saving the file
        if self.file_source:  # If a file is uploaded
            file = self.file_source.file  # Access the file
            file.seek(0)  # Ensure we are at the start of the file
            self.content = file.read().decode(
                "utf-8"
            )  # Read the file content into the 'content' field

            # Clear the file source so that it isn't saved anywhere
            self.file_source = None

        super().save(*args, **kwargs)

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
