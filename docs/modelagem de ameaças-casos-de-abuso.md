# 5 Modelagem de ameaças com STRIDE

| ID  | Categoria STRIDE        | Componente ou ativo      | Ameaça identificada                                                                                                               | Possível impacto                                                                                |
| --- | ----------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| T01 | Spoofing                | Conta do cliente         | Um atacante obtém as credenciais de um cliente e acessa sua conta para realizar pedidos ou visualizar informações pessoais.       | Pedidos realizados em nome da vítima, acesso indevido aos dados pessoais e prejuízo financeiro. |
| T02 | Spoofing                | Cadastro das empresas    | Um atacante utiliza as credenciais de uma empresa para alterar informações do estabelecimento ou gerenciar pedidos indevidamente. | Alteração de produtos, preços e informações da empresa, comprometendo sua credibilidade.        |
| T03 | Spoofing                | Conta do entregador      | Um atacante acessa a conta de um entregador para aceitar, cancelar ou alterar entregas.                                           | Entregas incorretas, atrasos, fraudes e prejuízo para clientes e empresas.                      |
| T04 | Spoofing                | Painel administrativo    | Um invasor obtém as credenciais de um administrador e assume o controle do sistema.                                               | Comprometimento completo do sistema, acesso a todos os dados e alterações indevidas.            |
| T05 | Tampering               | Pedidos                  | Um usuário altera valores, produtos ou quantidades de um pedido antes da confirmação.                                             | Prejuízo financeiro e perda da integridade das informações.                                     |
| T06 | Tampering               | Sistema de pagamentos    | Um atacante modifica o valor de uma transação ou altera informações de pagamento durante o processamento.                         | Fraudes financeiras e prejuízo para clientes e empresas.                                        |
| T07 | Tampering               | Cadastro das empresas    | Alteração não autorizada de preços, cardápios ou promoções.                                                                       | Venda de produtos com valores incorretos e prejuízo financeiro.                                 |
| T08 | Repudiation             | Sistema de pagamentos    | Um cliente ou empresa nega ter realizado um pagamento ou solicitado um reembolso.                                                 | Dificuldade para responsabilizar os envolvidos caso não existam registros de auditoria.         |
| T09 | Repudiation             | Pedidos                  | Um cliente afirma que nunca realizou determinado pedido.                                                                          | Conflitos entre cliente e empresa e possíveis prejuízos financeiros.                            |
| T10 | Repudiation             | Entregas                 | Um entregador afirma que realizou uma entrega que, na realidade, não foi concluída.                                               | Reclamações, perdas financeiras e dificuldade para apuração dos fatos.                          |
| T11 | Information Disclosure  | Cadastro de clientes     | Um usuário não autorizado acessa CPF, endereço, telefone, e-mail e histórico de pedidos dos clientes.                             | Violação da privacidade, descumprimento da LGPD e perda de confiança dos usuários.              |
| T12 | Information Disclosure  | Cadastro das empresas    | Exposição de informações comerciais ou documentos das empresas cadastradas.                                                       | Danos à empresa, vazamento de informações estratégicas e possíveis fraudes.                     |
| T13 | Information Disclosure  | Cadastro de entregadores | Exposição de dados pessoais dos entregadores, como CPF, telefone e informações do veículo.                                        | Violação da privacidade e possibilidade de golpes ou engenharia social.                         |
| T14 | Information Disclosure  | Sistema de pagamentos    | Vazamento de informações relacionadas aos pagamentos, como tokens, comprovantes ou outros dados financeiros.                      | Fraudes financeiras e comprometimento da segurança das transações.                              |
| T15 | Denial of Service (DoS) | Aplicação de delivery    | Um atacante envia um grande volume de requisições para sobrecarregar o sistema.                                                   | O sistema fica indisponível, impedindo clientes de realizar pedidos.                            |
| T16 | Denial of Service (DoS) | API de pagamentos        | Ataques tornam indisponível a comunicação com o sistema de pagamento.                                                             | Impossibilidade de concluir pagamentos e perda de vendas.                                       |
| T17 | Elevation of Privilege  | Painel administrativo    | Um cliente explora uma vulnerabilidade e obtém permissões administrativas.                                                        | Alteração de preços, exclusão de usuários, acesso aos dados e controle do sistema.              |
| T18 | Elevation of Privilege  | Cadastro das empresas    | Um funcionário comum obtém permissões de administrador da empresa.                                                                | Alteração indevida de cardápios, preços, promoções e pedidos.                                   |
| T19 | Elevation of Privilege  | Sistema                  | Um usuário comum consegue acessar funcionalidades restritas destinadas aos administradores.                                       | Comprometimento da segurança do sistema e acesso a informações confidenciais.                   |
| T20 | Elevation of Privilege  | Sistema de pagamento                 |Um atendente de suporte, utilizando seu acesso legítimo, processa reembolsos fraudulentos em conluio com terceiros para pedidos que foram normalmente entregues.                                      | Fraude interna recorrente, prejuízo financeiro direto e difícil detecção, já que a ação é tecnicamente autorizada.                   |

# 6 Casos de abuso
---
 
### CA01 — Invasão de conta de cliente via credenciais vazadas
**Ator:** atacante externo.
**Objetivo:** assumir o controle da conta de um cliente para realizar pedidos com o cartão salvo da vítima.
**Condições:** o sistema não possui limitação de tentativas de login (rate limiting) nem verificação adicional para acessos suspeitos.
**Fluxo de abuso:**
1. O atacante obtém uma lista de credenciais vazadas de outros serviços.
2. O atacante testa essas credenciais em massa contra o login da plataforma (*credential stuffing*).
3. O sistema autentica o atacante em contas cujas credenciais coincidem.
4. O atacante realiza pedidos utilizando o método de pagamento salvo na conta da vítima.
   
**Impacto:** prejuízo financeiro à vítima, fraude e perda de confiança na plataforma.

**Categorias STRIDE relacionadas:** Spoofing, Elevation of Privilege.
 
---
 
### CA02 — Alteração indevida do cardápio de um estabelecimento
**Ator:** concorrente ou ex-funcionário mal-intencionado.
**Objetivo:** prejudicar a reputação ou os resultados financeiros de um estabelecimento concorrente.
**Condições:** as credenciais do estabelecimento foram obtidas por phishing, vazamento ou reaproveitamento de senha.
**Fluxo de abuso:**
1. O atacante obtém as credenciais de acesso do estabelecimento.
2. O atacante acessa o painel de gerenciamento do estabelecimento.
3. O atacante altera preços dos produtos para valores incorretos ou remove itens do cardápio.
4. Clientes visualizam e reagem às informações incorretas antes da correção.

**Impacto:** dano à credibilidade do estabelecimento, perda de vendas e insatisfação dos clientes.

**Categorias STRIDE relacionadas:** Spoofing, Tampering.
 
---
 
### CA03 — Desvio de pedido por entregador malicioso
**Ator:** atacante externo que compromete a conta de um entregador, ou o próprio entregador mal-intencionado.
**Objetivo:** subtrair o produto do pedido sem realizar a entrega.
**Condições:** o sistema não confirma a entrega por um mecanismo além da marcação manual do entregador (ex: assinatura, código, foto).
**Fluxo de abuso:**
1. O atacante acessa ou controla a conta de um entregador.
2. O entregador aceita a corrida normalmente.
3. O entregador retira o produto no estabelecimento.
4. O entregador marca o pedido como "entregue" no aplicativo sem realizar a entrega.

**Impacto:** furto de mercadoria, prejuízo ao cliente e ao estabelecimento, reclamações e possíveis reembolsos indevidos.

**Categorias STRIDE relacionadas:** Spoofing, Repudiation.
 
---
 
### CA04 — Comprometimento do painel administrativo
**Ator:** atacante externo ou interno.
**Objetivo:** obter controle total sobre o sistema.
**Condições:** senha fraca do administrador, ausência de autenticação multifator ou vulnerabilidade explorável por phishing.
**Fluxo de abuso:**
1. O atacante identifica um administrador como alvo.
2. O atacante aplica phishing ou explora senha fraca para obter as credenciais.
3. O atacante acessa o painel administrativo com privilégios completos.
4. O atacante altera dados, exclui usuários ou extrai informações do sistema.

**Impacto:** comprometimento completo do sistema, acesso a todos os dados e alterações indevidas em larga escala.

**Categorias STRIDE relacionadas:** Spoofing, Elevation of Privilege, Information Disclosure.
 
---
 
### CA05 — Alteração do valor do pedido antes da confirmação
**Ator:** cliente mal-intencionado.
**Objetivo:** pagar um valor menor do que o real pelo pedido.
**Condições:** a validação de preços e quantidades é feita apenas no lado do cliente (client-side), sem revalidação no servidor.
**Fluxo de abuso:**
1. O atacante monta o pedido normalmente pelo aplicativo.
2. O atacante intercepta a requisição enviada ao servidor antes da confirmação.
3. O atacante altera o valor, a quantidade ou o produto no payload interceptado.
4. O servidor aceita os dados alterados sem revalidação.

**Impacto:** cobrança incorreta, prejuízo financeiro à empresa e perda da integridade das informações do pedido.

**Categorias STRIDE relacionadas:** Tampering.
 
---
 
### CA06 — Falsificação de confirmação de pagamento
**Ator:** atacante externo posicionado entre o cliente e o gateway de pagamento (*man-in-the-middle*).
**Objetivo:** obter produtos ou serviços sem efetuar o pagamento real.
**Condições:** a comunicação entre a aplicação e o gateway de pagamento não utiliza validação de integridade suficiente (ex: assinatura de resposta).
**Fluxo de abuso:**
1. O atacante intercepta a comunicação entre a aplicação e o gateway de pagamento.
2. O atacante impede ou altera a requisição real de cobrança.
3. O atacante forja uma resposta de "pagamento aprovado" para o sistema.
4. O sistema libera o pedido acreditando que o pagamento foi concluído.

**Impacto:** fraude financeira direta e prejuízo à empresa.

**Categorias STRIDE relacionadas:** Tampering, Spoofing.
 
---
 
### CA07 — Fraude de estorno (chargeback) indevido
**Ator:** cliente mal-intencionado.
**Objetivo:** obter o produto e, além disso, reaver o valor pago.
**Condições:** o processo de contestação de pagamento não exige evidências suficientes por parte do estabelecimento/plataforma.
**Fluxo de abuso:**
1. O cliente realiza o pedido normalmente e efetua o pagamento.
2. O cliente recebe o produto ou serviço integralmente.
3. O cliente solicita reembolso ou aciona a operadora do cartão alegando não ter realizado a compra.
4. A plataforma ou o estabelecimento arca com o prejuízo do estorno.

**Impacto:** prejuízo financeiro recorrente à empresa e à plataforma, dificuldade de responsabilização sem registros de auditoria adequados.

**Categorias STRIDE relacionadas:** Repudiation.
 
---
 
### CA08 — Confirmação falsa de entrega
**Ator:** entregador mal-intencionado.
**Objetivo:** receber o pagamento pela entrega sem realizá-la de fato.
**Condições:** a confirmação da entrega depende exclusivamente da marcação feita pelo próprio entregador no aplicativo.
**Fluxo de abuso:**
1. O entregador aceita a corrida e retira o pedido.
2. O entregador não realiza a entrega ao destinatário.
3. O entregador marca o status como "entregue" no aplicativo.
4. O sistema processa o pagamento da entrega normalmente.

**Impacto:** perda financeira, cliente lesado e dificuldade de apuração dos fatos sem evidência de entrega.

**Categorias STRIDE relacionadas:** Repudiation.
 
---
 
### CA09 — Extração em massa de dados pessoais de clientes
**Ator:** atacante externo ou usuário autenticado mal-intencionado.
**Objetivo:** coletar dados pessoais (CPF, telefone, endereço) de todos os clientes cadastrados.
**Condições:** o endpoint de consulta de usuários não verifica se o identificador solicitado pertence ao usuário autenticado (falha de autorização a nível de objeto — IDOR).
**Fluxo de abuso:**
1. O atacante autentica-se com uma conta válida qualquer.
2. O atacante identifica que o endpoint aceita um identificador sequencial na URL.
3. O atacante escreve um script que percorre os identificadores em sequência.
4. O sistema retorna os dados pessoais de cada cliente sem validar a autorização.

**Impacto:** vazamento em massa de dados pessoais, violação da LGPD e exposição dos clientes a golpes.

**Categorias STRIDE relacionadas:** Information Disclosure, Elevation of Privilege.
 
---
 
### CA10 — Engenharia social com dados vazados de entregadores
**Ator:** atacante externo.
**Objetivo:** aplicar golpes contra entregadores utilizando dados pessoais obtidos indevidamente.
**Condições:** dados como CPF, telefone e documentos de entregadores foram expostos por falha de proteção no armazenamento ou na transmissão.
**Fluxo de abuso:**
1. O atacante obtém dados pessoais de entregadores por meio de vazamento do sistema.
2. O atacante utiliza essas informações para se passar por um contato confiável (ex: suporte da plataforma).
3. O atacante contata o entregador solicitando dados bancários ou credenciais.
4. O entregador, acreditando ser um contato legítimo, fornece as informações solicitadas.

**Impacto:** fraude financeira contra o entregador e dano reputacional à plataforma.

**Categorias STRIDE relacionadas:** Information Disclosure, Spoofing.
 
---
 
### CA11 — Indisponibilidade da plataforma em horário de pico
**Ator:** concorrente mal-intencionado ou extorsionário.
**Objetivo:** tornar a plataforma indisponível durante o período de maior movimento (almoço/jantar).
**Condições:** ausência de proteção contra grandes volumes de requisições (ex: mitigação de DDoS, limitação de taxa).
**Fluxo de abuso:**
1. O atacante identifica o horário de maior uso da plataforma.
2. O atacante envia um grande volume de requisições simultâneas ao sistema.
3. Os servidores ficam sobrecarregados e deixam de responder adequadamente.
4. Clientes e estabelecimentos ficam impossibilitados de utilizar o sistema.

**Impacto:** perda de vendas, indisponibilidade do serviço e insatisfação de clientes e estabelecimentos.

**Categorias STRIDE relacionadas:** Denial of Service.
 
---
 
### CA12 — Elevação de privilégio via manipulação de token
**Ator:** cliente comum mal-intencionado.
**Objetivo:** obter acesso a funcionalidades restritas a administradores.
**Condições:** o backend não valida corretamente a assinatura do token de autenticação (JWT), permitindo alteração de seus campos.
**Fluxo de abuso:**
1. O atacante autentica-se normalmente como cliente.
2. O atacante analisa a estrutura do token de autenticação recebido.
3. O atacante altera o campo referente ao perfil de acesso (de "cliente" para "administrador").
4. O sistema aceita o token alterado por falha na validação da assinatura.

**Impacto:** acesso não autorizado a funções administrativas, comprometimento da segurança do sistema.

**Categorias STRIDE relacionadas:** Elevation of Privilege, Tampering.
 
---
 
### CA13 — Fraude interna por atendente de suporte
**Ator:** atendente de suporte (usuário legítimo, ameaça interna).
**Objetivo:** obter vantagem financeira indevida em conluio com terceiros.
**Condições:** o processo de reembolso não exige segunda aprovação nem gera trilha de auditoria detalhada vinculando a ação ao responsável.
**Fluxo de abuso:**
1. O atendente identifica pedidos já entregues normalmente.
2. O atendente, em conluio com um cliente ou conta falsa, processa reembolso para esses pedidos sem motivo legítimo.
3. O sistema aprova o reembolso, pois o atendente possui essa permissão dentro de suas atribuições.
4. O valor reembolsado é dividido entre o atendente e o cúmplice.

**Impacto:** fraude interna recorrente, prejuízo financeiro direto e de difícil detecção, já que a ação é tecnicamente autorizada.

**Categorias STRIDE relacionadas:** Repudiation, Elevation of Privilege.
 
---
