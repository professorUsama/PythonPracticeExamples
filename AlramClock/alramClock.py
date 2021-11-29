from datetime import datetime
from playsound import playsound
if __name__ == '__main__':
    input_alram_time = input("Enter alram time as format HH:MM:SS (am/pm):")
    alaram_hour = input_alram_time[0:2] # to store the hour input form the user
    alaram_min = input_alram_time[3:5] # to store minutes input form the user
    alaram_sec = input_alram_time[6:8] # to store the seconds input from the user
    alaram_period = input_alram_time[9:11].upper() # to store the PM and AM
    print(f"Alaram time = {alaram_hour}:{alaram_min}:{alaram_sec} {alaram_period}")
    print("Setting up alaram...")
    while(True):
        current_time = datetime.now() # to store the current time
        current_hour = current_time.strftime("%I") # to store the current hour
        current_min = current_time.strftime("%M") # to store the current min
        current_sec = current_time.strftime("%S") # to store the current sec
        current_period = current_time.strftime("%p") # to store the current pm or am
        if current_period == alaram_period:
            if current_hour == alaram_hour:
                if current_min == alaram_min:
                    if current_sec == alaram_sec:
                        print("wake up...")
                        playsound('alaram.wav') # to play alaram sound
                        break