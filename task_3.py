import json


def application(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')

    if path == '/' and method == 'GET':
        status = '200 OK'
        response_body = json.dumps({"message": "Hello, nfactorial!"})  # создаем JSON-ответ
        headers = [('Content-type', 'application/json; charset=utf-8')]  # Указываем, что это JSON
    else:
        status = '404 Not Found'
        response_body = 'Not Found'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    return [response_body.encode('utf-8')]