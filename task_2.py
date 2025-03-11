def application(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')
    protocol = environ.get('SERVER_PROTOCOL')

    if path == '/info' and method == 'GET':
        status = '200 OK'
        response_body = f"HTTP-метод: {method}\nURL запроса: {environ.get('HTTP_HOST')}{path}\nПротокол запроса: {protocol}"
    else:
        status = '404 Not Found'
        response_body = 'Not Found'

    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    return [response_body.encode('utf-8')]