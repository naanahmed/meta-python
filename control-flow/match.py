http_status = int(input('What is the http_status'))

match http_status :
    case 200 | 201 :
        print('Success')
    case 400:
        print('Bad request')
    case 404:
        print('Not Found')
    case 500 | 501 :
        print('Server Error')
    case _:
        print('Unknown')

