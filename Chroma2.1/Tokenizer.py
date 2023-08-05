import nltk
import wikipedia

text = "Who was Subhas Chandra Bose"
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


print(text)
wordcount("Basic.txt", text)
print(text)
text = ' '.join(map(str, text))

s = wikipedia.summary(text, sentences=3)
print(s)
