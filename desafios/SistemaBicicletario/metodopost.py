from bottle import post, request, route, run


@route('/')
def index():
    form =  '''
            <form action="/process" method="post">
                Name: <input type="text" name="name">
                <br>
                Idade: <input type="text" name="idade">
                <br>
                <input type="submit">
            </form>
            '''
    page = f'<h1>Web App</h1>{form}'
    return page

@post('/process')
def index_process():
    name = request.forms.get('name')
    idade = request.forms.get('idade')

    message = f'Olá {name}, você tem {idade} anos!'

    return message

run(host='localhost', port=8080)