<!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Gestão de Clientes - Bottle + SQLite</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                h1, h2 { color: #333; }
                form { margin-bottom: 20px; background: #f4f4f4; padding: 15px; border-radius: 5px; }
                input { margin-bottom: 10px; padding: 8px; width: 250px; display: block; }
                input[type="submit"] { background: #28a745; color: white; border: none; cursor: pointer; width: 120px; }
                table { width: 100%; border-collapse: collapse; margin-top: 10px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #007bff; color: white; }
                .btn-edit { color: #007bff; text-decoration: none; font-weight: bold; margin-right: 10px; }
                .btn-del { color: red; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Cadastro de Clientes</h1>
            
            <form action="/cadastrar" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" required placeholder="Digite o nome completo">
                
                <label>E-mail:</label>
                <input type="email" name="email" required placeholder="exemplo@email.com">
                <label>Telefone:</label>
                <input type="text" name="telefone" required placeholder="(88)9988-1234">
                
                <input type="submit" value="Cadastrar">
            </form>
 
            <h2>Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Telefone</th>
                    <th>Ações</th>
                </tr>
                % for id_, nome, email, telefone in lista_clientes:
                <tr>
                    <td>{{id_}}</td>
                    <td>{{nome}}</td>
                    <td>{{email}}</td>
                    <td>{{telefone}}</td>
                    <td>
                        <a class="btn-edit" href="/editar/{{id_}}">Editar</a>
                        <a class="btn-del" href="/deletar/{{id_}}">Excluir</a>
                    </td>
                </tr>
                % end
            </table>
        </body>
        </html>