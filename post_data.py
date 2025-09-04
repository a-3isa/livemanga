import requests
import os
import shutil

"""

This code is used for posting manga for livemanga project 
1- create a directory named manga 
2- inside the directory create a folder for every manga named by its name (ex : onepiece) 
3- inside every manga folder create folder for every chapter named by its number
   and number of voices you need (3-7-9) splitted by "_" (ex : ch3_5)
   
   
"""
url = 'https://3857-34-29-191-156.ngrok-free.app'
os.chdir("manga/")
while True :
    if len(os.listdir()) != 0 :
        for voice_number in os.listdir():
            for anime_name in os.listdir(voice_number):
                for chapter_name in os.listdir(f"{voice_number}/{anime_name}/{chapter_name}"):
                    print(anime_name)
                    print(chapter_name)
                    images=[]
                    for image in os.listdir(f"{anime_name}/{chapter_name}"):
                        print(image)
                        image_file=open(f"{anime_name}/{chapter_name}/{image}", "rb")
                        images.append(("image",image_file ))
                    
                    variable = {"chapter_name":chapter_name.split("_")[0],"anime_name":anime_name,"voices_number":chapter_name.split("_")[1]}
                    done = False
                    while not done :
                        response=requests.post(url+"/mangaupload/", files = images,data=variable)
                        if response.status_code == 201 :
                            done = True
                            print(response.status_code)
                    image_file.close()
                    images=[]
            shutil.rmtree(f"{anime_name}")