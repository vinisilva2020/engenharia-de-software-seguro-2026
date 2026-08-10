# Critérios, cálculo e registro de riscos

## 7. Critérios de probabilidade

Para avaliar a possibilidade de ocorrência de cada risco, será utilizada a seguinte escala:

| **Valor** | **Classificação** | **Critério**                                                                                  |
| --------- | ----------------- | --------------------------------------------------------------------------------------------- |
| 1         | Baixa             | O evento depende de condições incomuns, acesso muito específico ou grande capacidade técnica. |
| 2         | Média-baixa       | O evento é possível, mas depende de uma vulnerabilidade ou condição específica.               |
| 3         | Média-alta        | O evento é plausível e pode ocorrer em situações comuns de uso ou ataque.                     |
| 4         | Alta              | O evento pode ocorrer com facilidade, frequência ou durante condições previsíveis do sistema. |

A atribuição dos valores considera as características do sistema de delivery, os diferentes tipos de usuários, as vulnerabilidades necessárias para exploração e as condições em que cada evento poderá ocorrer.

---

## 7.1 Critérios de impacto

Para avaliar as consequências de cada risco, será utilizada a seguinte escala:

| **Valor** | **Classificação** | **Critério**                                                                          |
| --------- | ----------------- | ------------------------------------------------------------------------------------- |
| 1         | Baixo             | Causa pequeno transtorno e pode ser corrigido rapidamente.                            |
| 2         | Moderado          | Causa interrupção ou inconsistência limitada, com possibilidade de recuperação.       |
| 3         | Alto              | Causa prejuízo relevante aos usuários, ao negócio, à administração ou à privacidade.  |
| 4         | Muito alto        | Pode afetar muitos usuários, comprometer operações críticas ou causar prejuízo grave. |

Na avaliação do impacto foram considerados fatores como prejuízos financeiros, exposição de dados, indisponibilidade de funcionalidades, quantidade de usuários afetados, danos à privacidade, consequências jurídicas ou regulatórias, danos à reputação e dificuldade de recuperação.

---

## 7.2 Cálculo e classificação dos riscos

A pontuação de cada risco é obtida pela multiplicação entre sua probabilidade e seu impacto:

**Pontuação = Probabilidade × Impacto**

A classificação adotada é:

| **Pontuação** | **Nível do risco** |
| ------------- | ------------------ |
| 1 a 3         | Baixo              |
| 4 a 7         | Médio              |
| 8 a 11        | Alto               |
| 12 a 16       | Crítico            |

A pontuação é utilizada como apoio para comparação e priorização dos riscos. Entretanto, também são consideradas as características específicas de cada situação, os ativos envolvidos, as consequências possíveis e a capacidade de recuperação do sistema.

---

## 8. Registro de riscos

## Cada ameaça STRIDE identificada na Etapa 1 foi relacionada a pelo menos um risco.

| **ID**  | **Origem STRIDE**            | **Evento de risco**                                                                               | **Vulnerabilidade ou condição**                                                                | **Prob.** | **Impacto** | **Pontuação** | **Nível** |
| ------- | ---------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------- | ----------- | ------------- | --------- |
| **R01** | T01 – Spoofing               | Um atacante acessa a conta de um cliente e realiza pedidos ou consulta informações em seu nome.   | Credenciais comprometidas e ausência de verificação adicional de identidade.                   | 3         | 3           | **9**         | Alto      |
| **R02** | T02 – Spoofing               | Um atacante assume a conta de uma empresa e altera informações ou gerencia pedidos indevidamente. | Credenciais comprometidas e autenticação insuficiente.                                         | 3         | 3           | **9**         | Alto      |
| **R03** | T03 – Spoofing               | Um atacante assume a conta de um entregador e manipula operações relacionadas às entregas.        | Credenciais comprometidas e ausência de verificação adicional.                                 | 3         | 3           | **9**         | Alto      |
| **R04** | T04 – Spoofing               | Um invasor assume uma conta administrativa e passa a executar operações privilegiadas.            | Credenciais administrativas comprometidas e ausência de mecanismos adicionais de autenticação. | 3         | 4           | **12**        | Crítico   |
| **R05** | T05 – Tampering              | Produtos, quantidades ou valores de um pedido são alterados indevidamente antes da confirmação.   | Validação insuficiente no servidor e confiança excessiva nos dados enviados pelo cliente.      | 3         | 3           | **9**         | Alto      |
| **R06** | T06 – Tampering              | Valores ou informações de uma transação são alterados durante o processamento do pagamento.       | Falha na validação, integridade ou comunicação entre o sistema e o serviço de pagamento.       | 2         | 4           | **8**         | Alto      |
| **R07** | T07 – Tampering              | Cardápios, preços ou promoções são alterados sem autorização.                                     | Controle inadequado de acesso às funcionalidades administrativas da empresa.                   | 3         | 3           | **9**         | Alto      |
| **R08** | T08 – Repudiation            | Um cliente ou empresa nega ter realizado pagamento ou solicitado reembolso.                       | Ausência ou insuficiência de registros de auditoria das operações financeiras.                 | 3         | 3           | **9**         | Alto      |
| **R09** | T09 – Repudiation            | Um cliente nega ter realizado um pedido registrado pelo sistema.                                  | Falta de evidências suficientes sobre criação e confirmação do pedido.                         | 3         | 2           | **6**         | Médio     |
| **R10** | T10 – Repudiation            | Uma entrega é registrada como concluída sem ter sido efetivamente realizada.                      | Ausência de mecanismo confiável de confirmação da entrega.                                     | 3         | 3           | **9**         | Alto      |
| **R11** | T11 – Information Disclosure | Dados pessoais dos clientes são acessados ou divulgados a pessoas não autorizadas.                | Controle de acesso inadequado, permissões excessivas ou falha na proteção dos dados.           | 3         | 4           | **12**        | Crítico   |
| **R12** | T12 – Information Disclosure | Informações comerciais ou documentos das empresas são expostos indevidamente.                     | Permissões inadequadas ou proteção insuficiente das informações armazenadas.                   | 2         | 3           | **6**         | Médio     |
| **R13** | T13 – Information Disclosure | Dados pessoais dos entregadores são acessados ou expostos indevidamente.                          | Controle de acesso inadequado ou permissões excessivas.                                        | 2         | 3           | **6**         | Médio     |
| **R14** | T14 – Information Disclosure | Tokens, comprovantes ou outras informações relacionadas aos pagamentos são expostos.              | Armazenamento, transmissão ou controle de acesso inadequado às informações financeiras.        | 2         | 4           | **8**         | Alto      |
| **R15** | T15 – Denial of Service      | Um grande volume de requisições torna a aplicação indisponível.                                   | Ausência ou insuficiência de mecanismos para limitar requisições e absorver sobrecarga.        | 3         | 4           | **12**        | Crítico   |
| **R16** | T16 – Denial of Service      | A API de pagamentos fica indisponível, impedindo a conclusão das transações.                      | Dependência de serviço externo e ausência de mecanismos adequados de contingência.             | 3         | 4           | **12**        | Crítico   |
| **R17** | T17 – Elevation of Privilege | Um cliente consegue privilégios administrativos e executa operações restritas.                    | Falha de autorização ou validação inadequada das permissões no servidor.                       | 2         | 4           | **8**         | Alto      |
| **R18** | T18 – Elevation of Privilege | Um funcionário comum obtém permissões administrativas da empresa.                                 | Configuração incorreta de papéis ou falhas na verificação de privilégios.                      | 2         | 3           | **6**         | Médio     |
| **R19** | T19 – Elevation of Privilege | Um usuário comum consegue acessar funcionalidades reservadas aos administradores.                 | Ausência ou falha de validação de autorização no servidor.                                     | 2         | 4           | **8**         | Alto      |

---
