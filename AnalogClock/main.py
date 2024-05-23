
def calculate_angle(string_time):
    time = string_time.split(":")
    hours = int(time[0])
    minutes = int(time[1])

    hour_angle = (hours % 12) * 30 + (minutes * 0.5) # 30 degrees per hour (360/12=30), 0.5 degrees per minute (30/60=0.5)
    minute_angle = minutes * 6
    difference = abs(hour_angle - minute_angle)
    acute_angle = min(difference, 360 - difference)

    return acute_angle


string_time = input("Enter the time in the format HH:MM ")

print(f"The acute angle at {string_time} is {calculate_angle(string_time)} degrees")