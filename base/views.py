from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from base.models import Text
from base.serializers import TextSerializer


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        if "file" in request.FILES:
            file = request.FILES["file"]
            content = file.read().decode("utf-8")  # Read the file and store its content
            text = Text.objects.create(
                title=file.name, content=content
            )  # Save content instead of file path
            serializer = self.get_serializer(text)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return super().create(request, *args, **kwargs)
