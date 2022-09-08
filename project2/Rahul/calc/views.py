from django.shortcuts import render, HttpResponse

from .forms import MyfileUploadForm
from .models import file_upload
import openpyxl



def index(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            file_upload(file_name=name, my_file=the_files).save()
            
            excel_file = request.FILES["the_files"]

            wb = openpyxl.load_workbook(excel_file)

            worksheet = wb["Sheet1"]
            print(worksheet)

            return HttpResponse("file upload")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request, 'index.html', context)
        



def show_file(request):
    all_data = file_upload.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'view.html', context)
    

