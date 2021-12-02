# import speech_recognition as sr

# print(sr.__version__) #print the module version

# r = sr.Recognizer() # audio input lena
# my_mic = sr.Microphone(device_index=1)



# with my_mic as source:
#     print("Listening...")
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)

# res = r.recognize_google(audio)
# print(f"User said: {res}")

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-IN_HEERA_11.0' #indian voice
engine.setProperty('voice',voice_id)
# print(voices[0].id)
# print(voices[1].id)

engine.say("Tell me time. Tell me Date. Tell me day. Tell me year. Tell me school name.")
engine.runAndWait()

# for voice in voices:
#     voice_ids = voice.id
#     engine.setProperty('voice',voice_ids)
#     engine.say("Tell me time. Tell  me day. Tell me Teacher name.")
#     engine.runAndWait()