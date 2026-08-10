# Plano de tratamento, implementação e risco residual

## 10.4 Plano de tratamento

| **Risco** | **Estratégia** | **Controles propostos**                                                                                                                                                                | **Funções relacionadas**                            | **Responsáveis**                                                     | **Evidências e verificação**                                                                         |
| --------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **R01**   | Reduzir        | Exigir autenticação adicional para operações sensíveis; limitar tentativas de login; permitir encerramento de sessões suspeitas.                                                       | Protect, Detect, Respond                            | Desenvolvimento e infraestrutura                                     | Testes de autenticação, registros de login e simulação de tentativas consecutivas.                   |
| **R02**   | Reduzir        | Implementar autenticação multifator para contas empresariais; RBAC; confirmação de alterações críticas; registrar alterações.                                                          | Protect, Detect, Respond                            | Desenvolvimento                                                      | Testes de autorização e análise dos registros de alteração.                                          |
| **R03**   | Reduzir        | Utilizar autenticação adicional, controle de sessões e confirmação de operações críticas de entrega.                                                                                   | Protect, Detect, Respond                            | Desenvolvimento                                                      | Testes de autenticação e análise dos registros de entrega.                                           |
| **R04**   | Reduzir        | Exigir MFA de administradores; RBAC; princípio do menor privilégio; registrar operações administrativas; alertar sobre acessos suspeitos.                                              | Govern, Protect, Detect, Respond, Recover           | Administração, desenvolvimento e infraestrutura                      | Testes de MFA, testes de autorização, análise de logs e simulação de comprometimento.                |
| **R05**   | Reduzir        | Recalcular preços e totais no servidor; validar produtos, quantidades, descontos e promoções antes de registrar o pedido.                                                              | Protect, Detect, Respond                            | Desenvolvimento                                                      | Testes alterando valores enviados nas requisições e comparação com valores calculados pelo servidor. |
| **R06**   | Reduzir        | Validar valores e identificadores das transações no servidor; utilizar TLS; conferir o estado da transação antes de confirmar o pedido.                                                | Identify, Protect, Detect, Respond                  | Desenvolvimento e serviço de pagamento                               | Testes de integração e comparação entre pedido e transação registrada.                               |
| **R07**   | Reduzir        | Aplicar RBAC às funções de alteração de preços e cardápios; registrar usuário, horário, valor anterior e valor novo.                                                                   | Protect, Detect, Respond                            | Desenvolvimento e administração das empresas                         | Testes de autorização e auditoria das alterações.                                                    |
| **R08**   | Reduzir        | Registrar pagamentos e reembolsos com usuário, horário, identificador da transação, valor, ação realizada e resultado.                                                                 | Govern, Protect, Detect, Respond                    | Desenvolvimento e setor financeiro                                   | Consulta aos logs e teste de reconstrução do histórico de uma operação.                              |
| **R09**   | Reduzir        | Registrar criação, confirmação, alterações e responsável por cada pedido.                                                                                                              | Protect, Detect, Respond                            | Desenvolvimento                                                      | Auditoria de pedidos e testes de rastreabilidade.                                                    |
| **R10**   | Reduzir        | Utilizar código único ou outra confirmação de entrega; registrar data, horário e conta responsável pela conclusão.                                                                     | Protect, Detect, Respond                            | Desenvolvimento e operação de entregas                               | Simulação de entrega e verificação dos registros produzidos.                                         |
| **R11**   | Reduzir        | Aplicar RBAC e menor privilégio; proteger dados pessoais em trânsito e armazenamento; registrar acessos a informações sensíveis.                                                       | Govern, Identify, Protect, Detect, Respond, Recover | Desenvolvimento, infraestrutura e responsável pela proteção de dados | Testes de permissão, inspeção das configurações e auditoria dos registros de acesso.                 |
| **R12**   | Reduzir        | Restringir documentos e informações empresariais por função; proteger arquivos armazenados e registrar seus acessos.                                                                   | Identify, Protect, Detect, Respond                  | Desenvolvimento e infraestrutura                                     | Testes utilizando diferentes perfis e análise de logs.                                               |
| **R13**   | Reduzir        | Limitar dados dos entregadores aos perfis autorizados; exibir somente informações necessárias; registrar acessos.                                                                      | Identify, Protect, Detect, Respond                  | Desenvolvimento                                                      | Testes de autorização e revisão das informações exibidas a cada perfil.                              |
| **R14**   | Reduzir        | Não armazenar informações financeiras desnecessárias; restringir acesso a tokens e comprovantes; proteger transmissões com TLS.                                                        | Govern, Identify, Protect, Detect, Respond          | Desenvolvimento, infraestrutura e serviço de pagamento               | Revisão dos dados armazenados, testes de acesso e inspeção das conexões protegidas.                  |
| **R15**   | Reduzir        | Aplicar rate limiting; controlar quantidade de requisições; monitorar tráfego; adotar mecanismos de mitigação contra DDoS.                                                             | Identify, Protect, Detect, Respond, Recover         | Infraestrutura e desenvolvimento                                     | Testes de carga, métricas de disponibilidade e verificação dos alertas.                              |
| **R16**   | Compartilhar   | Utilizar provedor especializado de pagamento com requisitos de disponibilidade; implementar timeout, circuit breaker, tentativas controladas e prevenção de duplicidade de pagamentos. | Govern, Identify, Protect, Detect, Respond, Recover | Desenvolvimento, infraestrutura e provedor de pagamento              | Simulação de indisponibilidade, testes de timeout/circuit breaker e análise de registros.            |
| **R17**   | Reduzir        | Validar autorização no servidor em todos os endpoints administrativos; utilizar RBAC e menor privilégio.                                                                               | Identify, Protect, Detect, Respond                  | Desenvolvimento                                                      | Testes tentando utilizar endpoints administrativos com uma conta de cliente.                         |
| **R18**   | Reduzir        | Aplicar RBAC; controlar concessão e revogação de privilégios; registrar toda mudança de função.                                                                                        | Govern, Protect, Detect, Respond                    | Administração da empresa e desenvolvimento                           | Testes de papéis e auditoria das alterações de privilégios.                                          |
| **R19**   | Reduzir        | Verificar autorização no servidor antes de executar funções restritas; negar acesso por padrão; centralizar controles de permissão.                                                    | Identify, Protect, Detect, Respond                  | Desenvolvimento                                                      | Testes de acesso às funcionalidades administrativas utilizando perfis comuns.                        |

---

## 10.5 Ordem inicial de implementação

A ordem de implementação dos controles considera os riscos críticos, dependências entre mecanismos de segurança, abrangência dos controles e capacidade de uma única medida reduzir diversos riscos.

### 1ª prioridade — Controle de identidade, privilégios e painel administrativo

**Riscos relacionados:** R04, R17, R19 e R18.

Controles principais:

- MFA para administradores;
- RBAC;
- princípio do menor privilégio;
- validação de autorização no servidor;
- registro de alterações de privilégios.

Essa implementação recebe prioridade porque falhas de autorização ou comprometimento administrativo podem facilitar diversos outros riscos.

### 2ª prioridade — Proteção dos dados pessoais e financeiros

**Riscos relacionados:** R11, R12, R13 e R14.

Controles principais:

- restrição de acesso por perfil;
- minimização dos dados;
- proteção das informações em armazenamento e transmissão;
- registros de acesso a informações sensíveis.

Esses controles são prioritários devido à sensibilidade dos dados e à quantidade de usuários potencialmente afetados.

### 3ª prioridade — Segurança e disponibilidade dos pagamentos

**Riscos relacionados:** R06, R08 e R16.

Controles principais:

- validação de transações;
- registros de auditoria;
- TLS;
- timeouts;
- circuit breaker;
- tratamento de indisponibilidade.

Os pagamentos possuem grande importância para o negócio e podem gerar perdas financeiras imediatas.

### 4ª prioridade — Segurança das contas

**Riscos relacionados:** R01, R02 e R03.

Controles principais:

- mecanismos adicionais de autenticação;
- limitação de tentativas;
- controle de sessões;
- registros de acesso.

Os controles reduzem o comprometimento de contas utilizadas diariamente por clientes, empresas e entregadores.

### 5ª prioridade — Integridade de pedidos e informações comerciais

**Riscos relacionados:** R05 e R07.

Controles principais:

- validação no servidor;
- recálculo dos valores;
- autorização de alterações;
- auditoria das modificações.

Esses controles impedem que alterações feitas no lado do cliente sejam aceitas indevidamente.

### 6ª prioridade — Rastreabilidade de pedidos e entregas

**Riscos relacionados:** R09 e R10.

Controles principais:

- registros de criação e confirmação dos pedidos;
- confirmação de entrega;
- identificação de responsáveis e horários.

A implementação melhora a capacidade de apurar contestações e conflitos.

### 7ª prioridade — Resiliência contra indisponibilidade da aplicação

**Risco relacionado:** R15.

Controles principais:

- rate limiting;
- monitoramento de tráfego;
- capacidade de mitigação de DDoS;
- testes de carga e recuperação.

Embora R15 seja crítico, alguns controles de identidade, dados e infraestrutura precisam estar estruturados previamente. A prioridade poderá ser revista caso a aplicação seja exposta publicamente antes das demais funcionalidades.

---

## 10.6 Estimativa do risco residual

Os níveis abaixo representam uma **estimativa do risco esperado após a implementação e validação dos controles**. Não significam que o risco já foi reduzido.

| **Risco** | **Nível inicial** | **Nível residual esperado** | **Condição para aceitar o residual**                                                                    |
| --------- | ----------------- | --------------------------- | ------------------------------------------------------------------------------------------------------- |
| R01       | Alto (9)          | Médio (6)                   | Controles adicionais de autenticação, limitação de tentativas e monitoramento implementados e testados. |
| R02       | Alto (9)          | Médio (6)                   | MFA, RBAC e auditoria de alterações funcionando conforme testes.                                        |
| R03       | Alto (9)          | Médio (6)                   | Autenticação adicional, controle de sessões e registros de entrega validados.                           |
| R04       | Crítico (12)      | Médio (4)                   | MFA obrigatório, RBAC, menor privilégio e monitoramento administrativo implementados e testados.        |
| R05       | Alto (9)          | Médio (6)                   | Valores calculados no servidor e testes de manipulação das requisições realizados com sucesso.          |
| R06       | Alto (8)          | Médio (4)                   | Validação de transações, comunicação protegida e testes de integração concluídos.                       |
| R07       | Alto (9)          | Médio (6)                   | RBAC e auditoria de preços, cardápios e promoções funcionando corretamente.                             |
| R08       | Alto (9)          | Médio (6)                   | Logs permitirem reconstruir e comprovar o histórico de pagamentos e reembolsos.                         |
| R09       | Médio (6)         | Baixo (3)                   | Registros permitirem identificar criação, confirmação e responsável pelo pedido.                        |
| R10       | Alto (9)          | Médio (6)                   | Mecanismo de confirmação de entrega implementado e validado.                                            |
| R11       | Crítico (12)      | Médio (4)                   | Controles de acesso, proteção das informações e registros de acesso testados.                           |
| R12       | Médio (6)         | Baixo (3)                   | Permissões e proteção dos dados empresariais verificadas por testes.                                    |
| R13       | Médio (6)         | Baixo (3)                   | Acesso aos dados dos entregadores limitado aos perfis necessários e validado.                           |
| R14       | Alto (8)          | Médio (4)                   | Minimização, proteção e restrição de acesso aos dados de pagamento verificadas.                         |
| R15       | Crítico (12)      | Alto (8)                    | Rate limiting, monitoramento e mitigação implementados e avaliados mediante testes de carga.            |
| R16       | Crítico (12)      | Alto (8)                    | Mecanismos de contingência e responsabilidades do provedor definidos e testados.                        |
| R17       | Alto (8)          | Médio (4)                   | Endpoints administrativos rejeitarem corretamente contas sem privilégios.                               |
| R18       | Médio (6)         | Baixo (3)                   | Processo de concessão de privilégios e RBAC implementados e auditáveis.                                 |
| R19       | Alto (8)          | Médio (4)                   | Funções restritas verificarem autorização no servidor em todos os testes.                               |

Os riscos R15 e R16 permanecem estimados como **altos** mesmo após os controles, pois existem fatores externos que não podem ser eliminados completamente. No caso do R15, ataques de grande escala ainda podem superar a capacidade da infraestrutura. No R16, a aplicação permanece parcialmente dependente da disponibilidade do provedor externo de pagamentos.

A aceitação desses riscos residuais somente deverá ocorrer caso os controles tenham sido implementados e testados, existam procedimentos de resposta e recuperação e os responsáveis considerem que o nível restante é compatível com as necessidades do sistema.

---

# 11. Considerações finais

A análise desta etapa permitiu transformar as ameaças identificadas pelo STRIDE em riscos avaliáveis, considerando sua probabilidade e impacto. Entre os riscos mais críticos estão o comprometimento de contas administrativas, a exposição de dados pessoais e a indisponibilidade da aplicação e do serviço de pagamentos.

Para tratar os riscos, foram definidos controles de segurança específicos e utilizadas as funções do NIST CSF 2.0 para organizar as ações de governança, identificação, proteção, detecção, resposta e recuperação. A implementação dos controles foi priorizada de acordo com a criticidade dos riscos e a importância dos ativos envolvidos.

Por fim, os níveis de risco residual apresentados são estimativas e sua redução efetiva deverá ser confirmada após a implementação e verificação dos controles propostos. Dessa forma, a análise contribui para uma abordagem mais estruturada e adequada à segurança do sistema de delivery.
