from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
sp = gTTS(text='copy the code ',lang="en",slow = False)
sp.save(audio)
playsound(audio)
print(" ----- listen -----")