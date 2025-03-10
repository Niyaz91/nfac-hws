def application(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')

    if method == 'GET' and path == '/ping':
        status = '200 OK'
        response_body = 'pong'
    else:
        status = '404 Not Found'
        response_body = 'Not Found'


    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    # Отправляем статус и заголовки
    start_response(status, response_headers)

    # Возвращаем тело ответа
    return [response_body.encode('utf-8')]