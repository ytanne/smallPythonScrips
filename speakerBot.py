import os.path
import sys
import json
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 3000
r.dynamic_energy_threshold = True

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


CLIENT_ACCESS_TOKEN = '79d37d11ef0845dab586f2643b0f738d'

def dfAnswer(message2send):
    print(message2send)
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'en'  # optional, default value equal 'en'
    request.session_id = "TomAIbots"
    request.query = message2send
    response = request.getresponse()
    responseJson = json.loads(response.read().decode('utf-8'))
    answer = str(responseJson['result']['fulfillment']['speech'])
    return answer

def main():
    while True:
        x = input("Do you want to speak? 1 or 0\n")

        if x == '1':
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=0.5)

                print('Say something')

                audio = r.record(source, duration=4)

                try:
                    text = r.recognize_google(audio, language='en-EN')
                except:
                    text = 'Sorry, I did not understand'

                answer = dfAnswer(text)
                
                command = "say '" + answer + "'"

                os.system(command)
        else:
            break    


if __name__ == '__main__':
    main()