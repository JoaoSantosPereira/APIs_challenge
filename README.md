Desafio de entrevista de emprego Accenture

BÁSICO – Criar e consumir APIs
_________________________________________________________________________________________________________________________________________________________________________________
1. Criar uma API com Flask
Cria uma API com os seguintes endpoints:
GET /ping → deve retornar { "message": "pong" }
POST /echo → recebe um JSON com um campo text e retorna o mesmo texto
Exemplo:
bash
CopyEdit
curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -d '{"text":"hello"}'
_________________________________________________________________________________________________________________________________________________________________________________
2. Testar uma API pública com curl
Usa o curl para chamar a API de piadas do Chuck Norris:
bash
CopyEdit
curl https://api.chucknorris.io/jokes/random
Depois, extrai e imprime só o texto da piada (campo value) usando jq ou Python.
_________________________________________________________________________________________________________________________________________________________________________________
4. Explica com palavras tuas
O que é uma API REST?
Qual a diferença entre GET e POST?
Para que serve o código HTTP 404? E o 500?
_________________________________________________________________________________________________________________________________________________________________________________
INTERMEDIÁRIO – Criar uma mini-API CRUD
4. API de Tarefas (ToDo)
Cria uma API simples para gerenciar tarefas, com:
  >GET /tasks – lista todas as tarefas
  >POST /tasks – adiciona nova tarefa
  >PUT /tasks/<id> – edita tarefa
  >DELETE /tasks/<id> – apaga tarefa
  Tarefa = objeto com { "id": int, "title": str, "done": bool }
_________________________________________________________________________________________________________________________________________________________________________________
5. Validação de dados
Adiciona validações no POST /tasks:
title deve ser obrigatório e com pelo menos 3 letras
done deve ser true ou false
Se os dados forem inválidos, responde com 400 Bad Request.
_________________________________________________________________________________________________________________________________________________________________________________
AVANÇADO – Autenticação e integração
6. Autenticação com token
Adiciona um middleware na tua API:
Todos os endpoints devem exigir um header Authorization: Bearer <token>
Se o token for diferente de secrettoken123, retornar 401 Unauthorized
_________________________________________________________________________________________________________________________________________________________________________________
7. Consumir uma API externa
Cria um endpoint que, ao ser chamado, busque a temperatura atual de Lisboa usando uma API pública como OpenWeatherMap (precisa de API key) e retorne só a temperatura em Celsius.
_________________________________________________________________________________________________________________________________________________________________________________
8. Documentação com Swagger
Instala o pacote Flasgger e cria a documentação Swagger da tua API com /docs.
_________________________________________________________________________________________________________________________________________________________________________________
9. Testes automáticos
Cria testes unitários para os endpoints da tua API usando pytest:
Testar se GET /ping retorna status 200
Testar se POST /tasks funciona com dados válidos
