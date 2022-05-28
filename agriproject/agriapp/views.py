from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.template import loader
from django.shortcuts import render


# Create your views here.
def index(request):
    df = pd.read_csv(r"C:\Users\James\PycharmProjects\pythonProject\agriproject\data_files\Crop_recommendation.csv")
    df_headings = df.columns
    template = loader.get_template("agriapp/index.html")
    context = {"my_df": df, "df_headings": df_headings}
    return render(request, "agriapp/index.html", context)
