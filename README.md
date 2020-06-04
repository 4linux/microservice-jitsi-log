# microservice-jitsi-log

Microservice para logging de eventos de login e logout do Jitsi. 

## TODO

 * [ ] Melhorar imagem do container
 * [ ] Fazer o logging funcionar no WSGI (traceback ok!)
 * [ ] Adicionar testes

## Endpoints

| Método  | Endpoint             | Ação                             |
|---------|----------------------|----------------------------------|
| POST    | /api/v1.0/logs       | Cria u a novo log                |
| GET     | /healtcheck          | Checa a saude da aplicacao       |
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

Para subir a aplicacao na sua maquina basta efetuar o clone do repositorio, ativar o virtualenv, subir as dependencias, subir o container do MongoDB expondo a porta 27017 e chamar o Flask. Esse processo pode ser feito com os comandos abaixo:

Ou utilizar o docker-compose.
