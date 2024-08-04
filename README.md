# Data Analysis Project

This project allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Setup Instructions

1. First create the admin project in your directory using `django-admin startproject DataAnalysis` it will create the project.
2. Create/ Setup the app in under ypur directory using `python manage.py startapp data_analysis`
3. Migrate your app using cmd: `python manage.py makemigrations` and `python manage.py migrate`
4. Install dependencies: `Install dependencies pandas, numpy, seaborn and matplotlib etc..`
5. Run the Django development server: `python manage.py runserver`
6. Open a web browser and navigate to `http://localhost:8000/data_analysis/`

# Project overview
1. In Data analysis project Just created a empty string url in urls.py which redirect to data_analysis app where I create a urls.py.
2. Developed a upload_csv.html where user can upload the csv file and created a view based on required field format.
3. Once you upload the csv file it stored the csv file in your project directory for reading purpose and manuplate the data. 
4. I created a analyze function where it read the csv file thorugh pandas library and it summarized the data like mean, median, mode and Histograms plots show in web page.
    (it will redirect to the analyze.html file for representation and analyze function used ffor analyze the data (mean, median, missing value, handle missing value)
     and plots function it plots the simple Histograms)

   
# Images
 Over view how web page looklike-
![analysis](https://github.com/user-attachments/assets/0b0266b9-289a-4b8f-9183-0dbbbc7fc532)
![file_upload](https://github.com/user-attachments/assets/8deb783d-3c12-40e4-a672-a005dcd379a6)
![plots](https://github.com/user-attachments/assets/aa52952f-28fc-4e12-af4a-27cbe3ee7620)

## Sample CSV File

A sample CSV file is provided in the `temp.csv` directory. You can use this file to
