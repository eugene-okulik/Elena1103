import datetime

date_start = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date_start, '%b %d, %Y - %H:%M:%S')

full_month_name = python_date.strftime('%B')
print(full_month_name)

new_date_format = python_date.strftime('%d.%m.%Y, %H:%M')
print(new_date_format)
