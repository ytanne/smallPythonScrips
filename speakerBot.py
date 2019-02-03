import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


CLIENT_ACCESS_TOKEN = '79d37d11ef0845dab586f2643b0f738d'
message2send = "Whazzup?"


def main():

    print(message2send)

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "TomAIbots"

    request.query = message2send

    response = request.getresponse()
    
    responseJson = json.loads(response.read().decode('utf-8'))

    answer = str(responseJson['result']['fulfillment']['speech'])

    print(answer)


if __name__ == '__main__':
    main()