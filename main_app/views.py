from django.shortcuts import render, redirect
from django.conf import settings
from .models import CSVFILE
import os
import pandas as pd
def home(request):
    csv_files = CSVFILE.objects.all()
    return render(request, 'main_app/index.html', {"files" : csv_files})

def upload(request):
    if request.method == 'POST':
        
        file = request.FILES.get('file')
        
        csv = CSVFILE(file_name=file, title=file.name)
        csv.save()
        return redirect('main_app:home')

def delete(request, pk):
    file = CSVFILE.objects.get(pk=pk)
    file.delete()
    return redirect('main_app:home')


def analysis(request, pk):
    csv_file = CSVFILE.objects.get(pk=pk)
    file_path = os.path.join(settings.BASE_DIR, 'media\data_files', csv_file.title)
    if csv_file.title.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    rows = []
    for index, row in df.iterrows():
        rows.append(row)
    return render(request, 'main_app/analysis.html', {"df" : df, "rows": rows})
