# Download-s-Time
I create a python program that calculates and show the time for download the file, basicly you need give the file´s size and your internet´s speed, he will make the rest
print('Digit the file´s size in mb')
file_size = float(input("Here: "))
print('Digit the internet´s speed in mb/s')
internet_speed = float(input("Here: "))
time_seconds = file_size / (internet_speed / 8)
print(f"Your download it will take {time_seconds} seconds for finish")
