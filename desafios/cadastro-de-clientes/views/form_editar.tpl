<!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Editar Cliente</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                h1 { color: #333; }
                form { background: #f4f4f4; padding: 15px; border-radius: 5px; width: 300px; }
                input { margin-bottom: 10px; padding: 8px; width: 90%; display: block; }
                input[type="submit"] { background: #007bff; color: white; border: none; cursor: pointer; width: 100px; }
                a { color: #6c757d; text-decoration: none; display: inline-block; margin-top: 10px; }
            </style>
        </head>
        <body>
            <h1>Editar Cliente #{{cliente[1]}}</h1>
            
            <form action="/editar/{{cliente[0]}}" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" value="{{cliente[1]}}" required>
                
                <label>E-mail:</label>
                <input type="email" name="email" value="{{cliente[2]}}" required>

                <label>Telefone:</label>
                <input type="text" name="telefone" value="{{cliente[3]}}" required>
                
                <input type="submit" value="Salvar">
            </form>
 
            <a href="/">← Cancelar e Voltar</a>
        </body>
        </html>