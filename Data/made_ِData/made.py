import datetime

def print_hourly_datetime_until_one_year(start_date):
    end_date = start_date + datetime.timedelta(days=730)
    current_time = start_date

    while current_time < end_date:
        print(current_time.strftime("%Y-%m-%d %H:%M:%S,"))
        current_time += datetime.timedelta(hours=1)

# تاریخ شروع مورد نظر را مشخص کنید
start_date = datetime.datetime(2022, 7, 17, 0, 0, 0)

print_hourly_datetime_until_one_year(start_date)
