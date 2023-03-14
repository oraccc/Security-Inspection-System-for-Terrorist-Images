from django.shortcuts import render
from upload.models import IMG,IMG_Person
import sys
sys.path.append('C:\\Users\\IBM\\Desktop\\resnet')
sys.path.append('C:\\Users\\IBM\\Desktop\\face-recognition')
import test_on_pictures
import face_recognition


# Create your views here.
def uploadImgPerson(request):
    if request.method == 'POST':
        new_img = IMG_Person(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'uploading2.html')

def showImgPerson(request):
    name, picture_name = face_recognition.face_detection()
    terror_flag = True
    if name == "Unknown":
        terror_flag = False

    content = {
        'terror_flag' : terror_flag,
        'name' : name,
        'picture_name' : picture_name,
    }
    return render(request, 'showing2.html', content)

def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'uploading.html')

def showImg(request):
    imgs = IMG.objects.last()
    picture_dir = 'C:/Users/IBM/Desktop/system/media/upload/*.jpg'

    result = test_on_pictures.picture_detection(picture_dir)
    if result == 0:
        message = "Heavy"

    elif result == 1:
        message = "None"

    else:
        message = "Slight"

    content = {
        'imgs':imgs,
        'message':message,
    }
    return render(request, 'showing.html', content)
