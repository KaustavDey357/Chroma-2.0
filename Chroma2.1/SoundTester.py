from gtts import gTTS
from playsound import playsound

t1 = gTTS("Hello I'm Chroma2.1, nice to meet you")
t1.save("welcome.mp3")

t1 = gTTS("How can I help you today?")
t1.save("welcomer.mp3")

t1 = gTTS("Anything else?")
t1.save("welcomez.mp3")
