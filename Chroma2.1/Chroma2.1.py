import speech_recognition as sr
from pydub import AudioSegment
import pyaudio
import wikipedia
from gtts import gTTS
from playsound import playsound

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()
r = 2
q = 0
o = "How can I help you today?"
print("Hello I'm Chroma2.1, nice to meet you")
playsound("welcome.mp3")

while r > 0:
    with mic as source:

        q += 1
        recognizer.adjust_for_ambient_noise(source)
        print(o)
        playsound("welcomez.mp3") if q > 1 else playsound("welcomer.mp3")
        o = "Anything else?"
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(text)
        text = text.split()

        def wordcount(Basic, text):

            file = open(Basic, "r")
            read = file.readlines()
            file.close()

            for i in range(len(text)):

                word = text[i-1]

                for j in range(len(read)):

                    sentence = read[j]
                    line = sentence.split()

                    for z in range(len(line)):
                        each = line[z]
                        line2 = each.lower()
                        line2 = line2.strip(",.!@#$%^&*<>~")
                        if word == line2:
                            if word in text:
                                text.remove(word)

                        elif (word.lower()) == line2:
                            if word in text:
                                text.remove(word)
                        z += 1
                    j += 1
                i += 1

        wordcount("Basic.txt", text)
        # text = ' '.join(map(str, text))

        try:
            s = wikipedia.summary(text, sentences=3)
        except:
            text = ' '.join(map(str, text))
            s = wikipedia.summary(text, sentences=3)
        print(s)
        t1 = gTTS(s)
        t1.save("welcomet.mp3")
        playsound("welcomet.mp3")

    except sr.UnknownValueError:
        print("Could not understand")

    except sr.RequestError:
        print("Speech service down\n")
# Import the required module for text
# to speech conversion

# s = wikipedia.summary(audio, sentences=5)
# print(s)
# t1 = gTTS(s)
# t1.save("welcome.mp3")
# playsound("welcome.mp3")
