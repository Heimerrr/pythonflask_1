from flask import Flask, g, make_response, Response

app = Flask(__name__)
app.debug = True

# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"
#
#
# @app.route("/gg")
# def helloworld():
#     return 'helloworld!' + getattr(g, 'str', '111')

@app.route("/")
def helloworld2():
    return 'helloworld!!'

@app.route("/res1")
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

#WSGI( WebServer Gateway Interface)
@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type','text/plain'),
                  ('Content-Length', str(len(body)))]
        start_response('200 ok', headers)
        return [body]
    return make_response(application)
