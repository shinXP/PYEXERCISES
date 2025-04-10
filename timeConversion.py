from datetime import datetime

time = input("Enter time: ")
time_obj = datetime.strptime(time, "%I:%M:%S%p")
times = time_obj.strftime("%H:%M:%S")
print(times)

