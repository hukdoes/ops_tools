def application(environ, start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body='<h1>hello,%s!</h1>'%(environ['PATH_INFO'][1:]or'web')
    return [body.encode('utf-8')]
    # return [b'<h1>hello,web!</h1>']
