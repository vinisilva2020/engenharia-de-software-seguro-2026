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

## 5. Diagrama Simplificado de Componentes

O Diagrama Simplificado de Componentes apresenta uma visão arquitetural dos principais elementos que compõem o Sistema Delivery e das relações existentes entre eles. Diferentemente do Diagrama de Contexto, que apresenta os atores externos, e do Diagrama de Fluxo de Dados, que detalha o processamento e armazenamento das informações, este diagrama tem como objetivo representar a organização dos componentes responsáveis pela execução das funcionalidades do sistema.

No centro da arquitetura está a API / Servidor, responsável por intermediar a comunicação entre as aplicações utilizadas pelos diferentes perfis do sistema, os serviços externos e o banco de dados. Dessa forma, as aplicações clientes não realizam acesso direto ao banco de dados, sendo as requisições encaminhadas ao servidor para processamento e aplicação das regras de negócio.

Os principais componentes representados no diagrama são:

- Aplicativo Cliente;
- Painel Estabelecimento;
- Painel Administrativo;
- Aplicativo Entregador;
- Serviço de Pagamento;
- Banco de Dados;
- API / Servidor.

### 5.1 Aplicativo Cliente

O Aplicativo Cliente representa a interface utilizada pelos consumidores do sistema. Por meio desse componente, o usuário pode realizar operações relacionadas aos pedidos, consultar informações e acompanhar o andamento de suas solicitações.

As requisições realizadas pelo aplicativo são encaminhadas para a API / Servidor, que é responsável por autenticar o usuário, verificar suas permissões, processar as operações solicitadas e retornar as informações correspondentes.

A utilização da API como intermediária contribui para a segurança da aplicação, uma vez que impede que o aplicativo cliente tenha acesso direto aos recursos internos do sistema, como o banco de dados.

### 5.2 Painel Estabelecimento

O Painel Estabelecimento representa a interface utilizada pelos estabelecimentos participantes do sistema. Esse componente permite o gerenciamento das informações relacionadas aos produtos e aos pedidos recebidos.

As operações realizadas pelo estabelecimento são encaminhadas à API / Servidor, que deve verificar a identidade e as permissões do usuário antes de executar as alterações solicitadas. Essa separação é importante porque estabelecimentos possuem responsabilidades e permissões diferentes das atribuídas aos clientes.

Dessa forma, o controle de acesso deve garantir que cada estabelecimento possa manipular somente os recursos para os quais possui autorização.

### 5.3 Painel Administrativo

O Painel Administrativo representa a interface destinada aos usuários responsáveis pela administração do sistema. Por possuir acesso a funcionalidades de maior privilégio, esse componente exige mecanismos de segurança mais rigorosos.

As operações administrativas são encaminhadas à API / Servidor, que deve validar as permissões do usuário antes de permitir ações como gerenciamento de usuários, configurações, consultas de informações administrativas e acesso a registros e logs.

A separação entre o painel administrativo e as demais interfaces facilita a aplicação do princípio do menor privilégio, reduzindo a possibilidade de que usuários comuns obtenham acesso a funcionalidades administrativas.

### 5.4 Aplicativo Entregador

O Aplicativo Entregador representa a interface utilizada pelos responsáveis pela realização das entregas. Esse componente permite o acesso às informações necessárias para execução e acompanhamento das entregas, incluindo dados do pedido, endereço, localização e atualização do status.

Assim como ocorre com os demais componentes, a comunicação é realizada por meio da API / Servidor. O servidor deve verificar as permissões associadas ao perfil do entregador e disponibilizar somente as informações necessárias para a execução de suas atividades.

Essa limitação é particularmente importante devido à existência de informações pessoais e dados de localização, que não devem ser disponibilizados de forma irrestrita.

### 5.5 API / Servidor

A API / Servidor constitui o principal componente intermediário. Ela recebe as informações dos diferentes aplicativos e painéis, realiza o processamento das operações e estabelece a comunicação com os demais recursos do sistema.

Entre suas principais responsabilidades estão:

- autenticação e autorização dos usuários;
- aplicação das regras de negócio;
- gerenciamento dos pedidos;
- gerenciamento das entregas;
- processamento das operações administrativas;
- comunicação com o serviço de pagamento;
- acesso ao banco de dados;
- validação das informações recebidas pelas aplicações.

A centralização dessas operações permite que as regras de segurança sejam aplicadas no lado do servidor, evitando que a aplicação cliente seja considerada uma fonte confiável para informações críticas. Essa característica é especialmente relevante em operações como cálculo de valores, alteração de status, controle de permissões e processamento de pagamentos.

Essa centralização também é o componente responsável por aplicar a decisão de arquitetura DA02 (centralização do acesso aos dados pelo Backend/API) e por hospedar os mecanismos de autenticação multifator previstos na decisão DA01, ainda que o diagrama não represente um componente de "Serviço de Autenticação" isolado.

### 5.6 Serviço de Pagamento

O Serviço de Pagamento representa o componente externo responsável pelo processamento das transações financeiras. A comunicação com esse serviço ocorre por meio da API / Servidor, que encaminha as informações necessárias e recebe o resultado da operação.

A utilização de um componente intermediário permite que as informações relacionadas ao pagamento sejam tratadas pelo servidor antes de serem enviadas ao serviço externo. Além disso, a comunicação deve utilizar mecanismos de proteção, validação das respostas e controle de credenciais.

Também devem ser considerados problemas de disponibilidade desse serviço, uma vez que uma falha na comunicação pode afetar diretamente a confirmação dos pedidos e o processamento das transações. Esse comportamento é detalhado na Prática 3 (Etapa 4), que descreve a aplicação de timeout e circuit breaker na comunicação entre o Backend/API e a API externa de pagamentos.

### 5.7 Banco de Dados

O Banco de Dados representa o componente responsável pelo armazenamento persistente das informações utilizadas pelo sistema. Conforme apresentado no Diagrama de Fluxo de Dados, entre as informações armazenadas estão dados relacionados a usuários, pedidos, entregas e pagamentos.

A API / Servidor é responsável por realizar a comunicação com o banco de dados, evitando que os aplicativos e painéis tenham acesso direto a esse componente.

Essa organização contribui para centralizar as operações de leitura e escrita e aplicar regras de validação e autorização antes que uma informação seja armazenada ou modificada.

### 5.8 Comunicação entre os Componentes

A arquitetura apresentada estabelece a API / Servidor como ponto central de comunicação entre os componentes do sistema. Os aplicativos e painéis encaminham suas solicitações ao servidor, que processa as informações e realiza, quando necessário, operações no Banco de Dados ou comunicação com o Serviço de Pagamento.

Esse modelo permite separar as interfaces utilizadas pelos diferentes perfis das regras de negócio e dos recursos internos do sistema. Consequentemente, os usuários não precisam possuir acesso direto aos componentes responsáveis pelo armazenamento ou processamento das informações.

Do ponto de vista de segurança, essa estrutura também facilita a aplicação de mecanismos de autenticação, autorização, controle de acesso baseado em papéis (RBAC), validação das entradas e registro das operações. Dessa forma, o diagrama complementa o DFD ao apresentar não apenas o fluxo das informações, mas também a organização dos principais componentes responsáveis por processá-las.

### 5.9 Importância do Diagrama de Componentes para a Segurança

O Diagrama Simplificado de Componentes contribui para a análise de segurança ao permitir identificar os principais pontos de comunicação e os componentes que concentram responsabilidades críticas.

A API / Servidor representa um componente central e um ponto importante de proteção. O Banco de Dados concentra informações que precisam ser protegidas contra acesso não autorizado, enquanto o Serviço de Pagamento representa uma integração externa que exige mecanismos de comunicação segura e validação.

Da mesma forma, a separação entre Aplicativo Cliente, Painel Estabelecimento, Aplicativo Entregador e Painel Administrativo permite visualizar que diferentes perfis possuem diferentes necessidades de acesso.

Assim, o Diagrama Simplificado de Componentes complementa as demais representações ao demonstrar como os principais elementos do Sistema Delivery estão organizados e como se comunicam. A combinação entre os diagramas permite analisar o sistema em diferentes níveis, facilitando a identificação de componentes críticos, pontos de entrada, integrações externas e possíveis superfícies de ataque.
<img width="832" height="482" alt="Diagradecomponente drawio" src="https://github.com/user-attachments/assets/18668d1e-7914-4099-89f5-7e34b42dcdbe" />


## 6. Relação entre os três diagramas

Os três diagramas possuem funções diferentes, mas complementares.

| Diagrama | Principal objetivo | Pergunta que responde |
|---|---|---|
| Diagrama de Contexto | Mostrar o sistema e suas entidades externas | Quem interage com o sistema? |
| Diagrama de Fluxo de Dados | Mostrar processos, dados e armazenamentos | Como os dados circulam pelo sistema? |
| Diagrama de Componentes | Mostrar a organização interna da aplicação | Como o sistema é dividido internamente? |

A utilização conjunta dos três diagramas proporciona uma visão mais completa do Sistema Delivery.

O Diagrama de Contexto apresenta a visão externa e estabelece os limites do sistema. O DFD aprofunda essa representação mostrando o processamento e armazenamento das informações. Por fim, o Diagrama de Componentes apresenta uma visão estrutural da aplicação, demonstrando como suas partes internas podem ser organizadas.

## 7. Relação com a segurança do sistema

A modelagem dos diagramas não tem apenas finalidade de documentação. Ela também auxilia diretamente na identificação e tratamento dos riscos de segurança.

A partir dos diagramas é possível identificar pontos como:

- autenticação de usuários;
- autorização baseada em papéis;
- acesso a dados pessoais;
- manipulação de pedidos;
- avaliação de pedidos e possível manipulação de notas;
- processamento de pagamentos;
- comunicação com serviços externos;
- acesso administrativo;
- armazenamento de informações;
- registro de auditoria das operações administrativas;
- troca de informações com entregadores.

Esses pontos estão diretamente relacionados aos riscos identificados, como exposição de dados pessoais, comprometimento de contas administrativas, manipulação de pedidos, indisponibilidade do sistema e elevação indevida de privilégios.
