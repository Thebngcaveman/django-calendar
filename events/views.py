from django.shortcuts import render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name = "Jogger"
    month = month.title()
    #Convert month name => number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    #get current year
    today = datetime.now()
    current_year = today.year
    #get current time
    today_time = today.strftime('%I:%M:%S %p')
    return render(request, 
    'events/home.html', {
        "first_name":name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "today_time": today_time,
    })
