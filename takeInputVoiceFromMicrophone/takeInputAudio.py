import speech_recognition as sr

print(sr.__version__) #print the module version

r = sr.Recognizer() # audio input lena
my_mic = sr.Microphone(device_index=1)

with my_mic as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

res = r.recognize_google(audio)
print(f"User said: {res}")