## 11 Requisitos de segurança

Foram selecionados três riscos classificados como críticos na etapa anterior:

- **R04 – Comprometimento de conta administrativa**
- **R11 – Exposição de dados dos clientes**
- **R16 – Indisponibilidade da API de pagamentos**

Esses riscos foram escolhidos por ocuparem as três primeiras posições na priorização realizada anteriormente.

| **ID**   | **Risco de origem**                               | **Requisito de segurança**                                                                                                                                                                                              | **Critério de verificação**                                                                                                                                                                                                                      |
| -------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **RS01** | **R04 – Comprometimento de conta administrativa** | O sistema deverá exigir autenticação multifator (MFA) para todas as contas administrativas e verificar, no servidor, se o usuário possui autorização antes da execução de qualquer operação administrativa.             | O acesso administrativo deverá ser recusado quando o segundo fator de autenticação não for validado. Uma operação administrativa também deverá ser recusada quando a conta utilizada não possuir a permissão necessária.                         |
| **RS02** | **R11 – Exposição de dados dos clientes**         | O sistema deverá verificar, no servidor, as permissões do usuário antes de permitir o acesso aos dados pessoais dos clientes, utilizando controle de acesso baseado em papéis (RBAC) e o princípio do menor privilégio. | Em testes com contas de cliente, empresa, entregador e administrador, cada perfil deverá visualizar somente os dados necessários às suas funções. Tentativas de acesso a informações não autorizadas deverão ser recusadas pelo servidor.        |
| **RS03** | **R16 – Indisponibilidade da API de pagamentos**  | O sistema deverá tratar falhas e indisponibilidades da API externa de pagamentos utilizando mecanismos de timeout e circuit breaker.                                                                                    | Ao simular lentidão ou indisponibilidade da API de pagamentos, a requisição deverá ser encerrada após o tempo máximo definido. Após falhas consecutivas, o circuit breaker deverá interromper temporariamente novas chamadas ao serviço externo. |
