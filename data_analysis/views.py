from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from .forms import CSVUploadForm
import os

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            # Store the uploaded file temporarily
            with open('temp.csv', 'wb') as f:
                for chunk in csv_file.chunks():
                    f.write(chunk)
            return redirect('data_analysis:analyze')
    else:
        form = CSVUploadForm()
    return render(request, 'data_analysis/upload_csv.html', {'form': form})


def analyze(request):
    df = pd.read_csv('temp.csv')
    
    summary_stats = df.describe()
    missing_values = df.isnull().sum()
    

    df.fillna(df.mean(), inplace=True)
    
    data_preview = df.head()
    
    plot_files = plot(request, df)
    return render(request, 'data_analysis/analyze.html', {
        'summary_stats': summary_stats.to_html(),
        'missing_values': missing_values.to_frame().to_html(),
        'data_preview': data_preview.to_html(),
        'plot_files': plot_files
    })

def plot(request, df):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    plot_files = []
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Histogram of {col}')
        file_path = os.path.join(settings.MEDIA_ROOT, 'plots', f'{col}_histogram.png')
        plt.savefig(file_path)
        plot_files.append(f'plots/{col}_histogram.png')
    return plot_files

