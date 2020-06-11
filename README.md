# microservice-jitsi-log

Microservice para logging de eventos de login e logout do Jitsi. 

## TODO


 * [ ] Deixar parametros do insert como vars de ambiente ou armazenar tudo
 * [ ] Mensagem de erro com parametros obrigatorios
 * [ ] getenv para o modulo
 * [ ] Verificar timestamp do banco
 * [ ] Atualizar payload
 * [ ] Melhorar imagem do container
 * [ ] Fazer o logging funcionar no WSGI (traceback ok!)
 * [ ] Adicionar testes

## Endpoints

| Método  | Endpoint             | Ação                             |
|---------|----------------------|----------------------------------|
| POST    | /api/v1.0/logs       | Cria u a novo log                |
| GET     | //healthcheck        | Checa a saude da aplicacao       |
| GET     | /                    | Checa o nome do microservice     |

## Modelo de dados

- courseid - ID do curso
- jid - 8 caracteres alfanumericos
- displayname - Nome do usuario
- action - login ou logout
- timestamp - datetime UTC

Payload:

```
{
   "courseid": "2",
   "jid":"4321dcba",
   "displayname":"admin",
   "action":"login",
   "timestamp": "2020-06-04 06:10:32.172286"
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
