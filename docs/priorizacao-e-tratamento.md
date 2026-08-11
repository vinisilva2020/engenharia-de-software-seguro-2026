# Priorização e estratégias de tratamento

## 9. Priorização dos riscos

A priorização foi estabelecida considerando pontuação, impacto, quantidade de usuários potencialmente afetados, importância dos ativos, possibilidade de recuperação, dependências entre riscos e urgência do tratamento.

| **Prioridade** | **Risco**                                    | **Pontuação** | **Nível** | **Motivo principal**                                                                    |
| -------------- | -------------------------------------------- | ------------- | --------- | --------------------------------------------------------------------------------------- |
| **1**          | R04 – Comprometimento administrativo         | 12            | Crítico   | Pode conceder controle amplo do sistema e facilitar diversos outros ataques.            |
| **2**          | R11 – Exposição de dados de clientes         | 12            | Crítico   | Pode atingir grande quantidade de usuários e envolver dados pessoais.                   |
| **3**          | R16 – Indisponibilidade da API de pagamentos | 12            | Crítico   | Compromete uma operação essencial e pode provocar perda imediata de vendas.             |
| **4**          | R15 – DoS contra a aplicação                 | 12            | Crítico   | Pode interromper o serviço para clientes, empresas e entregadores simultaneamente.      |
| **5**          | R06 – Manipulação de pagamentos              | 8             | Alto      | Possui impacto financeiro muito alto e afeta transações críticas.                       |
| **6**          | R14 – Exposição de dados financeiros         | 8             | Alto      | Pode facilitar fraudes e comprometer informações de pagamento.                          |
| **7**          | R17 – Elevação de privilégio                 | 8             | Alto      | Pode conceder permissões administrativas a clientes comuns.                             |
| **8**          | R19 – Acesso a funções administrativas       | 8             | Alto      | Pode expor funcionalidades e informações restritas.                                     |
| **9**          | R01 – Conta de cliente comprometida          | 9             | Alto      | Pode gerar fraude financeira e exposição de dados pessoais.                             |
| **10**         | R02 – Conta empresarial comprometida         | 9             | Alto      | Afeta preços, pedidos e operações comerciais.                                           |
| **11**         | R05 – Manipulação de pedidos                 | 9             | Alto      | Compromete diretamente a integridade e os valores das compras.                          |
| **12**         | R08 – Repúdio de pagamentos                  | 9             | Alto      | Envolve transações financeiras e necessidade de evidências confiáveis.                  |
| **13**         | R10 – Falsa confirmação de entrega           | 9             | Alto      | Pode provocar fraudes, reembolsos e conflitos.                                          |
| **14**         | R03 – Conta de entregador comprometida       | 9             | Alto      | Pode interferir em entregas e gerar prejuízos aos envolvidos.                           |
| **15**         | R07 – Alteração de preços/cardápios          | 9             | Alto      | Afeta operações comerciais, mas possui alcance mais limitado que riscos anteriores.     |
| **16**         | R12 – Exposição de dados empresariais        | 6             | Médio     | Pode expor informações relevantes das empresas.                                         |
| **17**         | R13 – Exposição de dados dos entregadores    | 6             | Médio     | Afeta a privacidade e pode facilitar golpes.                                            |
| **18**         | R18 – Elevação de privilégio empresarial     | 6             | Médio     | Afeta principalmente um estabelecimento e depende de condição específica.               |
| **19**         | R09 – Repúdio de pedido                      | 6             | Médio     | Tende a apresentar consequências mais localizadas e maior possibilidade de recuperação. |

Embora R01, R02, R03, R05, R07, R08 e R10 possuam a mesma pontuação, suas prioridades foram diferenciadas de acordo com os ativos afetados e a gravidade das consequências.

Os riscos críticos envolvendo acesso administrativo, dados pessoais, pagamentos e disponibilidade receberam maior prioridade devido à possibilidade de afetar vários usuários e comprometer operações essenciais.

---

# 10. Tratamento dos riscos

## 14.1 Estratégias de tratamento

Para cada risco foi selecionada uma estratégia principal.

| **Risco** | **Estratégia** | **Justificativa**                                                                                                                                    |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| R01       | Reduzir        | A autenticação de clientes é necessária, portanto o risco deve ser diminuído mediante controles.                                                     |
| R02       | Reduzir        | Contas empresariais são essenciais ao funcionamento do sistema e precisam ser protegidas.                                                            |
| R03       | Reduzir        | As contas dos entregadores não podem ser eliminadas, devendo receber controles de segurança.                                                         |
| R04       | Reduzir        | O painel administrativo é necessário, mas requer proteção reforçada.                                                                                 |
| R05       | Reduzir        | A possibilidade de alteração deve ser reduzida por validações realizadas no servidor.                                                                |
| R06       | Reduzir        | A operação de pagamento é essencial e deve possuir mecanismos de integridade e validação.                                                            |
| R07       | Reduzir        | Alterações comerciais legítimas são necessárias, devendo ser controladas por autorização.                                                            |
| R08       | Reduzir        | O risco pode ser reduzido por registros confiáveis de auditoria.                                                                                     |
| R09       | Reduzir        | Registros dos pedidos podem fornecer evidências suficientes para reduzir o risco.                                                                    |
| R10       | Reduzir        | Mecanismos de confirmação podem diminuir a possibilidade de falsa entrega.                                                                           |
| R11       | Reduzir        | O tratamento de dados pessoais é necessário, mas o acesso deve ser limitado e protegido.                                                             |
| R12       | Reduzir        | Os dados empresariais são necessários ao serviço e precisam de controle de acesso.                                                                   |
| R13       | Reduzir        | Os dados dos entregadores precisam ser armazenados, mas seu acesso deve ser restrito.                                                                |
| R14       | Reduzir        | Informações relacionadas ao pagamento precisam ser protegidas e minimizadas.                                                                         |
| R15       | Reduzir        | A exposição da aplicação à Internet é necessária, sendo mais adequado mitigar ataques de sobrecarga.                                                 |
| R16       | Compartilhar   | Parte do risco decorre de um provedor externo de pagamento e deve ser compartilhada com esse prestador, mantendo controles próprios de contingência. |
| R17       | Reduzir        | O risco deve ser mitigado mediante controles de autorização no servidor.                                                                             |
| R18       | Reduzir        | A estrutura de papéis é necessária e deve possuir processo controlado de concessão de privilégios.                                                   |
| R19       | Reduzir        | Funcionalidades administrativas precisam existir, mas devem rejeitar usuários não autorizados.                                                       |

Nenhum dos riscos foi inicialmente tratado pela estratégia **Aceitar**, pois foram identificadas medidas razoáveis para redução ou compartilhamento. Uma eventual aceitação futura deverá ser formalmente justificada, aprovada pelos responsáveis e revisada periodicamente.

---
