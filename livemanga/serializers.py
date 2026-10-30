from rest_framework import serializers
from .models import Manga
from django.core.files.storage import default_storage
import os

class MangaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Manga
        fields='__all__'

    # def create(self, validated_data):
        # images_data = self.context['request'].FILES.getlist('image')
        # images = []
        # for image_data in images_data:
        #     image = Manga(image=image_data)
        #     image.save()
        #     images.append(image)
        # return images
    image = serializers.ListField(child=serializers.ImageField())

    # anime_name and chapter_name become directory names under media/ and inp/,
    # so they must not be able to climb out of them ("../", absolute paths).
    @staticmethod
    def _safe_path_part(value):
        if (not value or value != value.strip() or value.startswith('.')
                or any(c in value for c in '/\\:') or '..' in value):
            raise serializers.ValidationError(
                'Use a plain name without slashes, colons or "..".')
        return value

    def validate_anime_name(self, value):
        return self._safe_path_part(value)

    def validate_chapter_name(self, value):
        return self._safe_path_part(value)

    def save(self, path):
        images = self.validated_data['image']
        save_path = path.strip("/")
        
        saved_files = []
        for image_data in images:
            image_name = image_data.name
            file_name = os.path.join(save_path, image_name)
            with open(file_name, 'wb+') as destination:
                for chunk in image_data.chunks():
                    destination.write(chunk)
            saved_files.append(file_name)

        return saved_files
       
    

class VideoSerializer(serializers.Serializer):
    name = serializers.CharField(source='file_name')
    url = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj['file_name']

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj['file_path'])