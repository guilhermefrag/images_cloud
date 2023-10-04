from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Photos
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url='/login/')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        
        photo = Photos(photo_name=name, photo_file=photo)
        photo.save()
        return redirect('/cloud/home/')
    
@login_required(login_url='/login/')
def photo_list(request):
    if request.method == 'GET':
        photos = Photos.objects.values('id','photo_name','photo_file')
        return render(request, 'photo_list.html', {'photos': photos})
    elif request.method == 'POST':
        
        return HttpResponse('Photo deleted successfully')
    
@login_required(login_url='/login/')
def delete_photo(request, photo_id):
    photo_media = Photos.objects.filter(id=photo_id).values('id', 'photo_file').first()
    path = "./media/" + photo_media['photo_file']
    print(path)
    os.remove(path)
    photo = Photos.objects.filter(id=photo_id).first()
    photo.delete()
    
    return redirect('/cloud/photolist/')
    
@login_required(login_url='/login/')
def download_file(request, photo_id):
    photo = Photos.objects.filter(id=photo_id).values('photo_name','photo_file').first()
    file_path = "./media/" + photo['photo_file']
    file_name = photo['photo_name']
    
    file_wrapper = FileWrapper(open(file_path, 'rb'))
    response = StreamingHttpResponse(file_wrapper, content_type=mimetypes.guess_type(file_path)[0])
    response['Content-Disposition'] = f'attachment; filename={file_name + ".jpg"}'
    response['Content-Length'] = os.path.getsize(file_path)
    return response