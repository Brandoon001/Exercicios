
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Cliente</title>
</head>
<body>
    <h1>Editar Cliente</h1>

    <form action="/salvar-edicao/{{cliente[0]}}" method="post">
        <label>Nome:</label>
        <input
            type="text"
            name="nome"
            value="{{cliente[1]}}"
            required
        >

        <label>E-mail:</label>
        <input
            type="email"
            name="email"
            value="{{cliente[2]}}"
            required
        >

        <label>Telefone:</label>
        <input
            type="text"
            name="telefone"
            value="{{cliente[3]}}"
            required
        >

        <button type="submit">Salvar edição</button>
    </form>

    <a href="/">Cancelar</a>
</body>
</html>
