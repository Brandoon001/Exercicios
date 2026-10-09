from bottle import route, run

@route('/')
def index():
    file = "image"
    page = f'''
    <link rel = stylesheet type = "text/css" hr >    
'''
run(host='localhost', port=8080)