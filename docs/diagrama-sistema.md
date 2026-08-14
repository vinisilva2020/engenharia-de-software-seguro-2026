# Diagramas do Sistema de Delivery

## 1. Objetivo

Para auxiliar na compreensão da estrutura, do funcionamento e das interações do sistema de delivery, foram elaborados três diagramas complementares: Diagrama de Contexto, Diagrama de Fluxo de Dados (DFD) e Diagrama Simplificado de Componentes.

A utilização desses diagramas tem como objetivo representar o sistema em diferentes níveis de abstração. Enquanto o Diagrama de Contexto apresenta uma visão geral das interações do sistema com seus usuários e serviços externos, o Diagrama de Fluxo de Dados detalha como as informações são recebidas, processadas e armazenadas. Já o Diagrama Simplificado de Componentes apresenta uma visão dos principais componentes responsáveis pela execução das funcionalidades do sistema.

Essa representação facilita a compreensão da arquitetura e também contribui para a análise de segurança, permitindo identificar pontos de entrada, fluxos de informações, componentes críticos e possíveis superfícies de ataque.

## 2. Diagrama de Contexto

O Diagrama de Contexto apresenta uma visão geral do Sistema Delivery e das entidades externas que interagem diretamente com ele.

No centro do diagrama está o Sistema Delivery, representando a aplicação principal. Ao redor dele estão os principais atores e serviços externos envolvidos no funcionamento do sistema:

- Cliente;
- Estabelecimento;
- Entregador;
- Administrador;
- Sistema de Pagamento.

Cada ligação representa informações que são enviadas ou recebidas pelo sistema.

### 2.1 Cliente

O cliente é responsável por utilizar o sistema para realizar suas operações de delivery. Entre as principais informações relacionadas ao cliente estão:

- dados de login;
- informações do pedido;
- dados relacionados ao pagamento;
- acompanhamento do pedido;
- avaliação de pedidos e serviços;
- recebimento de confirmações e atualizações de status.

O cliente envia informações ao sistema para realizar operações e recebe informações referentes ao andamento de seus pedidos. A avaliação, em especial, representa uma informação enviada pelo cliente após a conclusão do pedido.

Essa interação é importante para a segurança porque envolve dados pessoais e informações relacionadas a pedidos e pagamentos. O trabalho identifica justamente a proteção dos dados dos clientes como um dos pontos relevantes da análise de riscos.

### 2.2 Estabelecimento

O estabelecimento interage com o sistema para disponibilizar seus produtos e administrar os pedidos recebidos.

Entre as principais informações trocadas estão:

- cardápio;
- produtos;
- valores;
- atualização de pedidos;
- confirmação de novos pedidos;
- alteração do status dos pedidos.

O estabelecimento precisa possuir permissões diferentes das de um cliente comum. Dessa forma, o sistema deve garantir que somente usuários autorizados possam realizar alterações relacionadas aos produtos, preços e pedidos.

Essa preocupação está relacionada aos controles de autorização e RBAC definidos no trabalho. Cabe reforçar que, embora o diagrama represente o Estabelecimento como um único ator, esse ator engloba tanto o responsável pelo estabelecimento quanto os funcionários autorizados.

### 2.3 Entregador

O entregador participa da etapa de transporte e conclusão do pedido.

As principais informações relacionadas a esse ator são:

- solicitação de entrega;
- endereço necessário para realização da entrega;
- dados do pedido;
- localização;
- confirmação da entrega;
- atualização do status.

O acesso do entregador deve ser limitado às informações necessárias para realizar sua função. Essa separação é importante porque o sistema trabalha com dados pessoais e informações de localização.

### 2.4 Administrador

O administrador possui um nível de acesso superior aos demais usuários.

Entre suas responsabilidades estão:

- gerenciamento do sistema;
- configurações;
- gerenciamento de usuários;
- acesso a relatórios;
- consulta a registros e logs;
- administração das funcionalidades.

Por possuir privilégios elevados, a conta administrativa representa um ativo crítico para a segurança. O trabalho identifica o comprometimento de contas administrativas como um dos riscos críticos e recomenda controles como RBAC, menor privilégio, autenticação e registro das operações administrativas.

É importante notar que essa relação é bidirecional: o Administrador envia informações ao sistema, como login e configurações, e recebe informações de saída, como relatórios e registros.

### 2.5 Sistema de Pagamento

O sistema de pagamento representa um serviço externo responsável pelo processamento das transações financeiras.

O Sistema Delivery envia informações necessárias para iniciar ou confirmar um pagamento e recebe informações relacionadas ao resultado da transação.

Essa integração deve utilizar mecanismos de proteção, como conexões seguras, proteção das credenciais de integração e validação das respostas recebidas. O trabalho também considera a indisponibilidade do serviço de pagamento como um risco importante.

O diagrama de contexto representa apenas o gateway de pagamento, por ser o de maior criticidade financeira e o mais diretamente ligado aos riscos críticos priorizados (R16).

### 2.6 Como o Diagrama de Contexto foi utilizado?

O Diagrama de Contexto foi utilizado para delimitar o sistema e identificar quem ou o que interage com ele.

Ele é importante porque permite visualizar rapidamente:

- quem utiliza o sistema;
- quais serviços externos são necessários;
- quais informações entram no sistema;
- quais informações saem do sistema;
- quais atores possuem diferentes responsabilidades.

Além disso, o diagrama ajuda na identificação dos pontos de interação, que são importantes para a análise de segurança. O trabalho define esses pontos como funcionalidades e interfaces pelas quais usuários, componentes internos ou serviços externos enviam e recebem informações.
<img width="911" height="492" alt="Diagramadecontexto drawio" src="https://github.com/user-attachments/assets/f4e4fbf8-0c27-4ead-9f3f-cb38b864c3e5" />

## 3. Diagrama de Fluxo de Dados

O Diagrama de Fluxo de Dados (DFD) apresenta uma visão mais detalhada do funcionamento interno do Sistema Delivery.

No diagrama foram representados os principais processos:

- Gerenciar Usuário;
- Gerenciar Pedido;
- Gerenciar Entrega;
- Processar Pagamento;
- Administração.

Também foram representados os principais armazenamentos de dados:

- D1 — Usuário;
- D2 — Pedido;
- D3 — Entrega;
- D4 — Pagamento.

### 3.1 Processo 1 — Gerenciar Usuário

O processo Gerenciar Usuário é responsável por receber e processar informações relacionadas ao cadastro e autenticação dos usuários.

O cliente fornece informações como login e dados necessários para sua identificação. Após o processamento, as informações relacionadas ao usuário são armazenadas no D1 — Usuário.

Esse processo é importante porque representa uma das principais portas de entrada da aplicação.

A autenticação precisa ser realizada antes do acesso às funcionalidades protegidas. Além disso, a autorização deve ser verificada de acordo com o papel do usuário.

No trabalho, essa proteção é implementada utilizando autenticação por token e RBAC, separando permissões de clientes, entregadores, estabelecimentos e administradores.

### 3.2 Processo 2 — Gerenciar Pedido

O processo Gerenciar Pedido é responsável pelo tratamento das informações relacionadas aos pedidos realizados pelos clientes.

Nesse processo ocorre a comunicação entre cliente e estabelecimento, incluindo:

- criação do pedido;
- produtos;
- quantidades;
- confirmação;
- atualização do status;
- informações necessárias para a entrega.

Os dados relacionados aos pedidos são armazenados no D2 — Pedido.

Esse processo possui grande importância para a segurança porque os valores e informações críticas do pedido não devem ser confiados diretamente aos dados enviados pelo cliente.

O backend deve utilizar os produtos e preços controlados pelo próprio sistema para calcular o valor final. Assim, caso o cliente tente alterar manualmente o preço enviado na requisição, o valor manipulado não deverá ser utilizado.

### 3.3 Processo 3 — Gerenciar Entrega

O processo Gerenciar Entrega controla as informações necessárias para que o pedido seja encaminhado ao entregador e posteriormente concluído.

Entre as informações envolvidas estão:

- pedido;
- endereço;
- localização;
- status da entrega;
- confirmação de entrega.

Essas informações são armazenadas no D3 — Entrega.

O controle de acesso é especialmente importante nessa etapa, pois o entregador precisa receber as informações necessárias para executar a entrega, mas não deve possuir acesso irrestrito aos demais dados do sistema.

O trabalho estabelece, por exemplo, que os dados dos entregadores devem ser disponibilizados somente aos perfis autorizados e que sejam exibidas apenas as informações necessárias.

### 3.4 Processo 4 — Processar Pagamento

O processo Processar Pagamento é responsável por encaminhar os dados necessários ao processamento da transação e receber a confirmação do sistema de pagamento.

A comunicação ocorre entre o sistema de delivery e o Sistema de Pagamento, sendo o resultado armazenado no D4 — Pagamento.

Esse processo exige atenção especial porque envolve informações financeiras.

O sistema deve validar os identificadores e valores da transação, utilizar comunicação segura e verificar o estado da transação antes de confirmar o pedido.

Também devem ser considerados cenários de indisponibilidade do serviço externo. O trabalho propõe mecanismos como circuit breaker, tentativas controladas e prevenção de pagamentos duplicados.

### 3.5 Processo 5 — Administração

O processo Administração representa as funcionalidades administrativas do sistema.

Por meio dele, o administrador pode acessar informações como:

- relatórios;
- logs;
- usuários;
- configurações;
- informações administrativas.

Esse processo possui alto nível de privilégio e, por isso, deve possuir controles de autorização mais rigorosos.

O sistema deve verificar no servidor se o usuário possui realmente o papel necessário para executar uma operação administrativa. A simples alteração de uma URL ou de uma informação enviada pelo cliente não deve permitir a obtenção de novos privilégios.

O fluxo entre o Administrador e o processo Administração é bidirecional: o administrador envia login e configurações para o sistema, e recebe relatórios, logs e informações de usuários como retorno. Essa entrada de dados deve ser considerada no detalhamento do DFD.

## 4. Como o Diagrama de Fluxo de Dados foi utilizado?

O DFD foi utilizado para detalhar o funcionamento interno do sistema e demonstrar o caminho percorrido pelas informações.

Sua utilização permite compreender:

- de onde os dados vêm;
- qual processo recebe esses dados;
- como eles são processados;
- onde são armazenados;
- quais outros processos utilizam essas informações;
- quais informações são enviadas para serviços externos.

Além disso, o DFD facilita a identificação de pontos que precisam de proteção.

Por exemplo, o fluxo de dados de pagamento exige proteção das informações financeiras, enquanto o fluxo de usuários exige controle de autenticação e autorização. Já o fluxo de pedidos precisa impedir que valores enviados pelo cliente sejam utilizados de maneira indevida.

Dessa forma, o diagrama contribui diretamente para relacionar a arquitetura funcional aos requisitos de segurança definidos no trabalho.

<img width="1067" height="770" alt="diagramafluxodedados drawio (1)" src="https://github.com/user-attachments/assets/561a8000-6cc7-4061-9774-41a2d5a94825" />
