# microservice-jitsi-log

Microservice para logging de eventos de login\logout do Jitsi atraves da API em JS do [lib-jitsi-meet](https://github.com/jitsi/lib-jitsi-meet)

## Endpoints

| Método  | Endpoint             | Ação                             |
|---------|----------------------|----------------------------------|
| POST    | /api                 | Cria uma novo log                |
| GET     | /healtcheck          | Checa a saude da aplicacao       |

## Modelo de dados

- jid - 8 caracteres alfanumericos
- displayname - Nome do usuario
- action - login ou logout


Payload:

```
{
   "jid":"4321dcba",
   "displayname":"admin",
   "action":"login"
}
```

## Deploy

### Dev

Para subir a aplicacao na sua maquina basta efetuar o clone do repositorio, criar o virtualenv, subir as dependencias, subir o container do MongoDB expondo a porta 27017 e chamar o Flask. Esse processo pode ser feito com os comandos abaixo:


### Prod

[] Escolher o WSGI para deploy
