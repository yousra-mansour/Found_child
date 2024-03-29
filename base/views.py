from django.shortcuts import render,redirect
from .models import found_child_data,missing_child_data
from deepface import DeepFace
import pywhatkit    
import time
import pyautogui
from pynput.keyboard import Key, Controller

def send_msg_to_parent(pk,person_name, phone_number, address, child_name):
    data = missing_child_data.objects.get(id = pk)
    keyboard = Controller()
    parent_num = data.phone_number
    msg = f"""
    we found your child {child_name}
    Mrs/Mr {person_name} found him
    {person_name} found your child in {address} 
    Here is his phone number {phone_number}
    call him now
    """
    pywhatkit.sendwhatmsg_instantly(parent_num, msg,tab_close=True)
    time.sleep(4)
    pyautogui.click()
    time.sleep(2)
    keyboard.press(Key.enter)
    return redirect('after_found')


def home(request):
    
    context = {}
    return render(request, 'base/index.html', context)


def missing(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        child_name = request.POST.get('child_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        img = request.FILES.get('img')

        data = missing_child_data(person_name = person_name ,child_name = child_name ,phone_number = phone_number ,address = address ,email = email ,img = img)
        data.save()

        for stored_photo in found_child_data.objects.all():
            img1 = r"C:/Users/Asus/Desktop/found_child/Found_child/media/missing_photos/{}".format(img)
            img2 = r"C:/Users/Asus/Desktop/found_child/Found_child/media/{}".format(stored_photo.img)
            result = DeepFace.verify(img1_path =img1 ,img2_path =img2,model_name = 'Facenet')
            if result['verified']:
                return redirect('after_missing_sccuess' ,pk=stored_photo.id)
        return redirect('after_mising_fail')
    context = {}
    return render(request, 'base/missing.html', context)


def found(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        child_name = request.POST.get('child_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        img = request.FILES.get('file')

        data = found_child_data(person_name = person_name ,child_name = child_name ,phone_number = phone_number ,address = address ,email = email ,img = img)
        data.save()

        for stored_photo in missing_child_data.objects.all():
            img1 = r"C:/Users/Asus/Desktop/found_child/Found_child/media/found_photos/{}".format(img)
            img2 = r"C:/Users/Asus/Desktop/found_child/Found_child/media/{}".format(stored_photo.img)
            result = DeepFace.verify(img1_path =img1 ,img2_path =img2,model_name = 'Facenet')
            if result['verified']:
                send_msg_to_parent(stored_photo.id, person_name,phone_number, address, child_name)
                return redirect('after_found')
        return redirect('after_found')
    return render(request, 'base/found.html')


def after_found(request):
    context = {}
    return render(request, 'base/after-found.html', context)


def after_missing_sccuess(request,pk):
    data = found_child_data.objects.get(id = pk)
    context = {"data":data}
    return render(request, 'base/after-missing-sccuess.html', context)

def after_found_sccuess(request,pk):
    data = found_child_data.objects.get(id = pk)
    context = {"data":data}
    return render(request, 'base/after-found-sccuess.html', context)


def after_mising_fail(request):
    context = {}
    return render(request, 'base/after-mising-404.html', context)

def about_us(request):
    context = {}
    return render(request, 'base/about-us.html', context)
