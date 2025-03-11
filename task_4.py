def app(environ, start_response):
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', '')

    if path == '/meaning-of-life' and method == 'POST':
        response_body = '{"meaning": "42"}'
        status = '200 OK'
        headers = [('Content-type', 'application/json')]
    else:
        response_body = '{"error": "Not Found"}'
        status = '404 Not Found'
        headers = [('Content-type', 'application/json')]

    start_response(status, headers)
    return [response_body.encode('utf-8')]

