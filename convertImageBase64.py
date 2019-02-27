import glob
import base64

listName = glob.glob("mapas/*.jpg")

for name in listName:
    with open(name,"rb") as file:
        str64 = base64.b64encode(file.read())
    nameImage = name.split('/')[1].split('.')[0]
    text_file = open('mapaBase64/'+nameImage+'.txt', "w")
    text_file.write( str64 )
    text_file.close()