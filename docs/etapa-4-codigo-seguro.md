# Prática selecionada: autenticação, autorização RBAC e menor privilégio

## 1. Objetivo

Implementar uma API de backend para o sistema de delivery que autentique os
usuários e verifique, no servidor, se o perfil possui permissão para acessar
cada área da aplicação. A prática impede que a interface, a URL ou os dados
enviados pelo cliente sejam usados para obter privilégios indevidos.

O exemplo está em `implementacao/` e utiliza FastAPI, tokens Bearer, armazenamento em
memória para fins didáticos e templates HTML para cadastro e login.

## 2. Riscos e requisitos relacionados

| Item | Relação                                                                                  |
| ---- | ---------------------------------------------------------------------------------------- |
| R04  | Comprometimento de conta administrativa e execução de operações privilegiadas.           |
| R11  | Exposição de dados pessoais de clientes a perfis não autorizados.                        |
| R17  | Cliente obtém privilégios administrativos.                                               |
| R19  | Usuário comum acessa funcionalidade reservada ao administrador.                          |
| RS01 | O servidor deve verificar autenticação e autorização antes de operações administrativas. |
| RS02 | O servidor deve aplicar RBAC e menor privilégio aos dados pessoais.                      |

## 3. Casos de uso

### Caso de uso válido — cadastro e acesso do cliente

1. O usuário informa nome, e-mail e senha com pelo menos 12 caracteres na tela
   de cadastro.
2. A API valida os dados e cria a conta com o papel cliente.
3. O usuário realiza login com e-mail e senha.
4. A API retorna um token Bearer aleatório.
5. O cliente acessa somente a área correspondente ao seu papel.

**Resultado:** a conta é criada, a senha não é armazenada em texto puro e o acesso
à área de cliente é permitido.

### Caso de uso inválido — cadastro duplicado ou senha fraca

O usuário tenta cadastrar e-mail já existente ou senha com menos de 12
caracteres.

**Resultado:** a API recusa a operação com erro de validação (422) ou conflito
(409), sem criar uma segunda conta.

### Caso de uso malicioso — elevação de privilégio

Um cliente autenticado tenta acessar `/api/v1/areas/administrador` ou altera a
URL para acessar uma área de outro perfil.

**Resultado:** a API verifica o papel no servidor e responde `403 Forbidden`. O
cliente não recebe conteúdo administrativo.

### Caso de uso não autorizado — acesso sem autenticação

Uma pessoa tenta acessar uma área protegida sem enviar o cabeçalho
`Authorization: Bearer <token>` ou envia um token inválido.

**Resultado:** a API responde `401 Unauthorized` e não executa a operação.

## 4. Testes definidos antes da implementação

| Teste | Entrada ou ação                                                          | Resultado seguro esperado                                                         |
| ----- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| TS01  | Cliente envia cadastro válido em `/api/v1/auth/register/clientes`.       | Conta criada com papel cliente; senha armazenada somente como hash; resposta 201. |
| TS02  | Entregador envia cadastro com senha menor que 12 caracteres.             | Cadastro recusado por validação; nenhuma conta criada; resposta 422.              |
| TS03  | Estabelecimento tenta cadastrar um e-mail já existente.                  | Operação recusada sem sobrescrever a conta original; resposta 409.                |
| TS04  | Usuário cadastrado informa credenciais corretas em `/api/v1/auth/login`. | Token Bearer aleatório emitido; nenhum dado sensível retornado.                   |
| TS05  | Usuário informa senha incorreta no login.                                | Resposta genérica 401; não revelar se o e-mail existe nem emitir token.           |
| TS06  | Cliente autenticado acessa `/api/v1/areas/cliente`.                      | Solicitação permitida; resposta limitada à área de cliente.                       |
| TS07  | Cliente autenticado acessa `/api/v1/areas/administrador`.                | Solicitação recusada com 403; nenhuma operação administrativa executada.          |
| TS08  | Cliente autenticado acessa `/api/v1/areas/entregador`.                   | Solicitação recusada com 403; dados e funções de entregador não expostos.         |
| TS09  | Usuário acessa área protegida sem token.                                 | Solicitação recusada com 401; nenhuma informação protegida retornada.             |
| TS10  | Administrador criado internamente acessa `/api/v1/areas/administrador`.  | Solicitação permitida, pois o papel é administrador.                              |
| TS11  | Usuário realiza logout e reutiliza o token revogado.                     | Token deixa de ser aceito; resposta 401.                                          |
