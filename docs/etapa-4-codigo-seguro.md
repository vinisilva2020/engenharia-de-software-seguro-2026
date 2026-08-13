# Etapa 4 — Código Seguro e Testes de Segurança

## 1. Objetivo

O objetivo desta etapa é demonstrar como as decisões de segurança definidas anteriormente foram transformadas em práticas de implementação segura no sistema de delivery.

Foram selecionadas duas práticas de código seguro:

1. **Controle de autorização com RBAC e menor privilégio**;
2. **Validação de entrada e integridade dos pedidos**.

Para cada prática foram definidos testes de segurança antes da implementação, contemplando um cenário válido e um cenário malicioso, inválido ou não autorizado.

---

# Prática 1 — Controle de autorização com RBAC e menor privilégio

## 2. Riscos e requisitos relacionados

| Item     | Relação                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------- |
| **R04**  | Comprometimento de conta administrativa e execução de operações privilegiadas.                       |
| **R11**  | Exposição de dados pessoais de clientes a perfis não autorizados.                                    |
| **R17**  | Cliente obtém privilégios administrativos.                                                           |
| **R19**  | Usuário comum acessa funcionalidade reservada ao administrador.                                      |
| **RS01** | O servidor deve verificar autenticação e autorização antes da execução de operações administrativas. |
| **RS02** | O servidor deve aplicar RBAC e menor privilégio no acesso aos dados pessoais.                        |

## 3. Testes de segurança definidos antes da implementação

| Teste                          | Entrada ou ação                                                                  | Resultado seguro esperado                                                                     |
| ------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **TS01 — Caso válido**         | Usuário autenticado acessa uma funcionalidade correspondente ao seu perfil.      | A solicitação é permitida e somente as informações autorizadas são retornadas.                |
| **TS02 — Caso não autorizado** | Cliente autenticado tenta acessar uma funcionalidade reservada ao administrador. | A solicitação é recusada com `403 Forbidden` e nenhuma informação administrativa é retornada. |

### Caso válido

Um usuário realiza cadastro e login com credenciais válidas e tenta acessar uma funcionalidade correspondente ao seu perfil.

**Resultado esperado:** o backend reconhece o usuário autenticado, verifica seu papel e permite a operação.

### Caso não autorizado

Um cliente autenticado tenta acessar uma funcionalidade administrativa ou uma área destinada a outro perfil.

**Resultado esperado:** o backend verifica o papel do usuário e recusa a operação, impedindo a elevação indevida de privilégios.

## 4. Implementação

A aplicação utiliza controle de acesso baseado em papéis (**RBAC — Role-Based Access Control**) para separar as permissões de clientes, entregadores, estabelecimentos e administradores.

As funcionalidades protegidas exigem autenticação por token Bearer. Após identificar o usuário, o backend verifica seu papel antes de permitir a execução da operação solicitada.

As regras de autorização são aplicadas no servidor. Dessa forma, modificar a interface ou alterar diretamente uma URL não permite que o usuário obtenha novas permissões.

O administrador é criado internamente e não existe uma opção pública que permita a clientes, entregadores ou estabelecimentos criarem contas com privilégios administrativos.

A implementação também utiliza armazenamento seguro das senhas e permite a revogação dos tokens após o logout.

## 5. Resultado esperado

Espera-se que usuários autenticados consigam acessar somente as funcionalidades correspondentes ao seu perfil.

Tentativas de acessar funcionalidades de outro papel devem ser recusadas pelo servidor. Usuários sem autenticação válida não devem receber informações protegidas.

Com isso, a aplicação aplica os princípios de menor privilégio e negação de acesso quando a autorização necessária não estiver presente.

## 6. Referências OWASP

- **OWASP Authorization Cheat Sheet:** utilizada como referência para menor privilégio, negação por padrão e validação das permissões em cada requisição.
- **OWASP Authentication Cheat Sheet:** utilizada como referência para autenticação segura.
- **OWASP API Security Top 10 — Broken Function Level Authorization:** utilizada como referência para impedir que usuários comuns acessem funcionalidades administrativas.
- **OWASP ASVS:** utilizado como base para requisitos verificáveis relacionados à autenticação e ao controle de acesso.

---

# Prática 2 — Validação de entrada e integridade dos pedidos

## 7. Riscos e requisitos relacionados

Esta prática está relacionada à ameaça identificada anteriormente de **alteração dos valores ou itens de um pedido**, na qual um cliente poderia modificar os dados enviados ao backend para tentar pagar um valor diferente do correto.

| Item                        | Relação                                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **T05**                     | Alteração indevida de valores ou itens de um pedido.                                                                 |
| **Risco relacionado a T05** | Manipulação dos dados do pedido para alterar preços, produtos, quantidades ou o valor total.                         |
| **Requisito relacionado**   | O backend deve validar os dados recebidos e determinar no servidor os valores utilizados no processamento do pedido. |

> **Observação:** substituir “Risco relacionado a T05” e “Requisito relacionado” pelos respectivos IDs `Rxx` e `RSxx` definidos nas etapas anteriores, caso existam.

## 8. Testes de segurança definidos antes da implementação

| Teste                     | Entrada ou ação                                                                            | Resultado seguro esperado                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **TS03 — Caso válido**    | Cliente autenticado cria um pedido informando produtos e quantidades válidas.              | O servidor valida os dados e calcula o valor total utilizando os preços mantidos pela aplicação. |
| **TS04 — Caso malicioso** | Cliente modifica a requisição e tenta informar um preço inferior ao valor real do produto. | O preço enviado pelo cliente não é utilizado e o servidor calcula o pedido com o valor correto.  |

### Caso válido

Um cliente autenticado cria um pedido informando o estabelecimento, os produtos desejados e suas respectivas quantidades.

**Resultado esperado:** o backend valida as informações recebidas e calcula o valor total do pedido utilizando os preços controlados pelo próprio sistema.

### Caso malicioso

Um cliente altera os dados da requisição e tenta enviar manualmente um preço inferior ao preço real do produto.

**Resultado esperado:** o backend não utiliza o preço informado pelo cliente como fonte confiável. O valor correto do produto é utilizado no cálculo do pedido.

Como verificação adicional, também foi considerado o envio de um pedido sem produtos.

**Resultado esperado:** a solicitação é considerada inválida e recusada antes do processamento.

## 9. Implementação

A criação de pedidos foi implementada considerando que informações críticas não devem ser determinadas diretamente pelo cliente.

O cliente informa os produtos desejados e suas respectivas quantidades. O backend utiliza essas informações para obter os valores correspondentes e calcular o total.

Dessa forma, mesmo que o cliente tente adicionar ou modificar manualmente um preço na requisição, esse valor não é utilizado para determinar o preço final.

A aplicação também realiza a validação dos dados necessários para a criação do pedido. Solicitações inválidas, como pedidos sem produtos, são recusadas antes do processamento.

Essa abordagem mantém no servidor a responsabilidade por informações críticas e reduz o risco de manipulação dos valores dos pedidos.

## 10. Resultado esperado

Espera-se que pedidos válidos sejam processados normalmente e que seus valores sejam calculados pelo backend.

Tentativas de manipular os preços enviados ao servidor não devem modificar o valor real utilizado pela aplicação.

Entradas inválidas devem ser recusadas antes do processamento, preservando a integridade dos dados do pedido.

## 11. Referências OWASP

- **OWASP Input Validation Cheat Sheet:** utilizada como referência para validação das entradas recebidas pela aplicação e rejeição de dados inválidos.
- **OWASP Web Security Testing Guide:** utilizada como referência para testes envolvendo manipulação de parâmetros.
- **OWASP ASVS:** utilizado como referência para requisitos verificáveis relacionados à validação das entradas e à integridade dos dados processados.

---

# 12. Resultado da execução dos testes

Além da definição prévia dos testes de segurança, foram implementados testes automatizados para verificar o comportamento da aplicação.

Os testes contemplaram cenários relacionados a autenticação, autorização, controle de acesso, validação de pedidos e tentativa de manipulação dos valores enviados pelo cliente.

A execução dos testes automatizados apresentou:

**13 testes aprovados e nenhuma falha.**

Resultado registrado:

`13 passed, 24 warnings in 1.36s`

Os avisos apresentados durante a execução são provenientes de dependências utilizadas pela aplicação e não representam falhas nos testes.

O resultado obtido demonstra que os cenários automatizados executados apresentaram o comportamento seguro esperado.

---

# 13. Limitações da demonstração

A implementação possui finalidade acadêmica e utiliza componentes simplificados.

Em um ambiente de produção, seriam necessários controles adicionais, como armazenamento persistente, TLS obrigatório, expiração e rotação de tokens, autenticação multifator para contas administrativas, auditoria persistente, proteção de segredos e mecanismos adicionais de validação e monitoramento.
