import json
import math

def application(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')

    if path.startswith('/'):
        num_str = path[1:]
    else:
        num_str = path

    if method == 'GET' and num_str.isdigit():
        num = int(num_str)
        factorial = math.factorial(num)
        status = '200 OK'
        response_body = json.dumps({"nfactorial": factorial})
        headers = [('Content-type', 'application/json; charset=utf-8')]
    else:
        status = '404 Not Found'
        response_body = 'Not Found'
        headers = [('Content-type', 'text/plain; charset=utf-8')]


    start_response(status, headers)
    return [response_body.encode('utf-8')]