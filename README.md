# microservice-jitsi-log

Microservice para logging de eventos de login e logout do Jitsi. 

## TODO


 * [ ] Melhorar check de campos
 * [ ] Melhorar imagem do container
 * [ ] Fazer o logging funcionar no WSGI (traceback ok!)
 * [ ] Adicionar testes

## Endpoints

| Método  | Endpoint             | Ação                             |
|---------|----------------------|----------------------------------|
| POST    | /api/v1.0/logs       | Cria um novo log                 |
| GET     | //healthcheck        | Checa a saude da aplicacao       |
| GET     | /                    | Checa o nome do microservice     |

## Modelo de dados

Payload:

```javascript
{
  "sala": "10_5_Hadoop",
  "curso": 10,
  "turma": "Turma 1522",
  "aluno": "Bryan A.",
  "jid": "b28cb3fe-f53f-4006-99d9-16e5db86f35c@jitsi.domain.tld/7utDTbSM",
  "email": "bryan@domain.tld",
  "timestamp": 1592572981,
  "action": "login"
}

```

## Deploy

### Dev

```bash
docker-compose up --build -d
```

## Agradecimentos

* [Arthur Nascimento](https://github.com/tureba) - Code review
* [Lucas Ricciardi de Salles](https://github.com/LucasRicciardi) - Code review
