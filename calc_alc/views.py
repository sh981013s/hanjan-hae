from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Alcohol
from openpyxl import load_workbook
import pandas as pd

def excelToModel(request):
    path = "data/Alcohol_Model.xlsx"
    reader = pd.read_excel(path, sheet_name = 0, header=0)
    list = []
    for row in reader.to_dict(orient='split').get('data') :
        # print(i)
        list.append(Alcohol(
            name=row[0],
            alc=row[1],
            cup=row[2],
            bottle=row[3],
            alc_type=row[4],
            company=row[5],
        ))

    Alcohol.objects.bulk_create(list)

# Connection
def home(request):
    if(Alcohol.objects.count()==0):
        excelToModel(request)
    alcohol = Alcohol.objects.all()
    return render(request, 'alcohol.html',{'alcohol':alcohol})

def calculator(drink, alc):
    # 마신 총 알코올양 = (마신양(drink) * 알코올 도수 (alc/100) * 0.8)/100
    return drink * alc * 0.00008

def searchAlc(request) :
    selected = request.GET.get('alc_type')
    sObj = Alcohol.objects.filter(name=selected)
    return render(request, 'alcohol.html', {'selectedObj':sObj})
