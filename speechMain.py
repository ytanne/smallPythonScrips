import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 3000
r.dynamic_energy_threshold = True

with sr.Microphone() as source:
    print('The Microphone is ' + str(source))
    r.adjust_for_ambient_noise(source, duration=0.5)
    print('Say something')
    audio = r.record(source, duration=4)
    print(audio)

    try:
        text = r.recognize_google(audio, language='en-EN')
        print(text)
        print('You have said : {}'.format(text))
    except:
        print('Sorry, I did not understand')
