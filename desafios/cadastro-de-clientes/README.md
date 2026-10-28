# Cadastro de Clientes

Aplicação web de estudo feita em Python, Bottle e SQLite. Permite cadastrar,
visualizar e excluir clientes em um banco de dados local.

## Funcionalidades

- Cadastro de clientes com nome, e-mail e telefone.
- Listagem dos clientes cadastrados, com identificador automático.
- Exclusão de um cliente pelo identificador.
- Criação automática da tabela ao iniciar a aplicação.

O banco contém os campos `id`, `nome`, `email` e `telefone`. A edição de
cadastros e o tratamento de erros ainda estão pendentes.

## Requisitos

- Python 3.
- Não é necessário instalar dependências: o projeto inclui o Bottle e usa
  SQLite pela biblioteca padrão do Python.

## Como executar

No terminal, na pasta do projeto, execute:

```bash
python app.py
```

Depois, acesse [http://localhost:8080](http://localhost:8080). O arquivo
`clientes.db` e a tabela `clientes` são criados na pasta do projeto quando a
aplicação é iniciada pela primeira vez.

## Estrutura do projeto

- `app.py`: inicializa o banco e define as rotas da aplicação web.
- `bottle.py`: framework Bottle incluído no projeto.
- `clientesbd.py`: exercícios de acesso ao SQLite e inserção de dados de
  exemplo.
- `views/form_clientes.tpl`: formulário e tabela de clientes.

## Próximas etapas

- [ ] Implementar a edição de clientes.
- [ ] Melhorar o tratamento de erros e a validação dos dados.
