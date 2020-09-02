import requests
import json
import shutil
import os
from PIL import Image
from PIL import ImageFile
import urllib
import time

ImageFile.LOAD_TRUNCATED_IMAGES=True
API_KEY='243705df3c8a858189414b8af7921dc6'
paginas=5
K=0
items=[]
print("How many datasets would you like to download?")
N=input()
for i in range(int(N)):
    print("Input the " + str(i+1) + " query")
    query=input()
    items.append(query.replace(" ","+"))


start_time=time.time()

for index,i in enumerate(items):

    images=[]

    for u in range(paginas):
        PARAMS=dict(
            api_key=API_KEY,
            sort="interestingness-desc",
            text=i,
            per_page=500,
            extras='url_c',
            content_type=1,
            media="photos",
            format="json",
            nojsoncallback=1,
            page=u+1
        )

        response=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.search",params=PARAMS)

        if ( "200" in str(response) and u==0):
            print("API requested correctly the dataset: " + i.replace("+"," "))
            try:
                if not os.path.exists(i.replace("+"," ")):
                    os.makedirs(i.replace("+"," "))
            except OSError:
                print("Error al crear el directorio, el directorio ya existe")

        data=response.json()
        photos=data.get("photos")
        photo=photos.get("photo")
        for p in photo:
            if 'url_c' in p:
                ImagenFlickr=p['url_c']
                images.append(ImagenFlickr)

    for o in images:
        if(K==500*5-1):
            K=0

        local_filename=requests.get(o,stream=True)
        file_name='local_image_'+str(K)+'.jpg'
        local_file = open(file_name, 'wb')
        local_filename.raw.decode_content = True
        shutil.copyfileobj(local_filename.raw, local_file)
        path="./"+i.replace("+"," ")+"/"+file_name
        shutil.copyfile("./"+file_name,path)
        local_file.close()

        try:
            image=Image.open(path)
        except OSError:
            continue
        image=image.convert(mode='L')
        image=image.resize((50,50))
        image.save(path)

        os.remove(file_name)
        del local_filename
        K=K+1



print("The datasets were downloaded correctly")

print("--- %s seconds ---" % (time.time()-start_time))