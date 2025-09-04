# from django.http import JsonResponse
# from .models import Manga
from .serializers import MangaSerializer,VideoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import os
# from inference_text import model2annotations
# from TTS.api import TTS
# from launch import liveManga
# from paddleocr import PaddleOCR
# from gramformer import Gramformer


# live=liveManga(PaddleOCR,model2annotations,Gramformer)



class VideoListAPIView(APIView):
    def get(self, request, format=None):
        # media_folder = 'media/'  # Replace with the path to your media folder
        # video_extensions = ['.mp4', '.avi', '.mkv']  # Add more video extensions if needed

        # videos = []
        # for root, dirs, files in os.walk(media_folder):
        #     for file in files:
        #         if any(file.lower().endswith(ext) for ext in video_extensions):
        #             file_path = os.path.join(media_folder, file)
        #             file_name = os.path.basename(file_path)
        #             videos.append({'file_path': file_path, 'file_name': file_name})

        # serializer = VideoSerializer(videos, many=True, context={'request': request})
        # return Response(serializer.data)
        return Response(len(os.listdir("inp")))
    
class MangaUploadView(APIView): 
   
    def post(self, request, format=None):
        serializer=MangaSerializer(data=request.data ,context={'request': request})
        
        if serializer.is_valid():
            print("Data is valid. Start the process")
            for directory in ['media/'+request.data['anime_name'],f'inp/{request.data["anime_name"]}_{request.data["chapter_name"]}_{request.data["voices_number"]}',
                              'media/'+request.data['anime_name']+'/'+request.data['chapter_name']]:
                if not os.path.exists(directory):
                    os.makedirs(directory)

            serializer.save(f'inp/{request.data["anime_name"]}_{request.data["chapter_name"]}_{request.data["voices_number"]}')
            # live.work(request.data['anime_name'],request.data['chapter_name'],request.data['voices_number'])
            
            with open("public_url.txt","r") as f :

                puplic_url= f.read()

            return Response({"result": f" {puplic_url}/media/{request.data['anime_name']}/{request.data['chapter_name']}"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
