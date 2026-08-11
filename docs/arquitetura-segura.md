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
---
## 11.1 Vulnerabilidades catalogadas

Para cada requisito de segurança foi pesquisada uma vulnerabilidade ou categoria relacionada utilizando catálogos e referências reconhecidas na área de segurança de software.

| **Risco**                                         | **Vulnerabilidade ou categoria**  | **Referência utilizada**                                                         | **Relação com o sistema**                                                                                                                                                                                   |
| ------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R04 – Comprometimento de conta administrativa** | Autenticação inadequada           | **CWE-287 – Improper Authentication / OWASP A07:2025 – Authentication Failures** | Uma falha na autenticação pode permitir que um atacante seja reconhecido como um administrador legítimo e obtenha acesso ao painel e às operações privilegiadas do sistema.                                 |
| **R11 – Exposição de dados dos clientes**         | Autorização incorreta             | **CWE-863 – Incorrect Authorization / OWASP A01:2025 – Broken Access Control**   | Uma falha na verificação das permissões pode permitir que um usuário acesse dados pessoais que não deveriam estar disponíveis para o seu perfil.                                                            |
| **R16 – Indisponibilidade da API de pagamentos**  | Consumo inseguro de APIs externas | **OWASP API Security Top 10:2023 – API10: Unsafe Consumption of APIs**           | A ausência de tratamento adequado para lentidão, erros ou indisponibilidade do serviço externo pode fazer com que requisições permaneçam aguardando respostas e comprometam o processamento dos pagamentos. |
---
## 11.2 Diagrama da arquitetura segura

O diagrama apresenta a organização proposta para o sistema de delivery e a posição dos principais controles relacionados aos riscos selecionados.
