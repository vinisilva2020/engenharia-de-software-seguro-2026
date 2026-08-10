# 2. Usuários, ativos e pontos de interação

O sistema que o grupo escolheu é uma plataforma de delivery de alimentos. Ele conecta clientes, estabelecimentos e entregadores, permitindo consultar cardápios, realizar pedidos, efetuar pagamentos, acompanhar entregas e avaliar os serviços prestados.

# 2.1 Usuários e perfis de acesso

Cada perfil possui permissões específicas e deve acessar somente as informações necessárias para realizar suas atividades.

| Perfil   |                Descrição |                       Principais    permissões                                                                                               |
| -------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Cliente              | Pessoa que utiliza o aplicativo para realizar pedidos   | Criar conta, consultar cardápios, fazer pedidos, pagar, acompanhar entregas, cancelar pedidos e realizar avaliações |
| Estabelecimento      | Restaurante ou loja responsável por preparar os pedidos | Cadastrar produtos, alterar preços, aceitar pedidos, atualizar o andamento da preparação e solicitar cancelamento   |
| Entregador           | Pessoa responsável por retirar e entregar os pedidos    | Aceitar entregas, consultar rotas e endereços e atualizar a situação da entrega                                     |
| Atendente de suporte | Pessoa responsável por auxiliar os usuários             | Consultar pedidos, responder mensagens, registrar reclamações, processar reembolsos e solucionar problemas          |
| Administrador        | Responsável pelo gerenciamento da plataforma            | Gerenciar usuários, estabelecimentos, entregadores, pedidos, avaliações e configurações do sistema                  |

Cada perfil tem acesso limitado somente às informações necessárias para desempenhar suas funções. 

# 2.2 Ativos importantes

Os ativos são dados, recursos e componentes que precisam ser protegidos. O acesso, a alteração, a destruição ou a indisponibilidade desses elementos pode causar prejuízos aos usuários, aos estabelecimentos, aos entregadores e à própria plataforma.

| Ativo                         | Descrição                                                                     | Importância | Possível prejuízo                                                  |
| ----------------------------- | ----------------------------------------------------------------------------- | :---------: | ------------------------------------------------------------------ |
| Dados pessoais                | Nome, CPF, telefone e e-mail dos usuários                                     |     Alta    | Violação de privacidade e utilização indevida dos dados            |
| Credenciais                   | E-mail, senha e códigos de acesso                                             |     Alta    | Invasão e roubo de contas                                          |
| Tokens de autenticação        | Tokens gerados após o login para manter a sessão ativa                        |     Alta    | Sequestro de sessão e acesso não autorizado                        |
| Dados de pagamento            | Tokens de pagamento, identificação da transação, valor e situação da cobrança |     Alta    | Fraudes e prejuízos financeiros                                    |
| Endereço do cliente           | Local informado para a entrega do pedido                                      |     Alta    | Exposição da residência e risco à segurança                        |
| Localização do entregador     | Posição obtida por GPS durante a entrega                                      |     Alta    | Rastreamento indevido e violação de privacidade                    |
| Pedidos                       | Produtos, quantidades, valores, endereço e situação do pedido                 |     Alta    | Alteração indevida, cobrança incorreta ou entrega errada           |
| Cancelamentos e reembolsos    | Solicitações e registros de cancelamentos ou estornos                         |     Alta    | Cancelamentos indevidos, fraudes e prejuízos financeiros           |
| Cardápios e preços            | Produtos e valores cadastrados pelos estabelecimentos                         |     Alta    | Cobranças incorretas e prejuízos ao estabelecimento                |
| Mensagens                     | Comunicação entre cliente, entregador, estabelecimento e suporte              |    Média    | Exposição de informações e aplicação de golpes                     |
| Avaliações                    | Notas e comentários publicados pelos clientes                                 |    Média    | Manipulação de avaliações e danos à reputação                      |
| Documentos                    | Documentos de identificação de entregadores e estabelecimentos                |     Alta    | Fraude de identidade e criação de cadastros falsos                 |
| Configurações do sistema      | Taxas, regras, validações e permissões da plataforma                          |     Alta    | Comprometimento da segurança ou do funcionamento do sistema        |
| Banco de dados                | Armazena usuários, pedidos, pagamentos e avaliações                           |     Alta    | Vazamento, alteração ou perda de informações                       |
| Histórico de operações        | Registra pedidos, pagamentos, cancelamentos e alterações                      |     Alta    | Dificuldade para identificar fraudes e responsabilizar usuários    |
| Logs de auditoria e segurança | Registram acessos, tentativas de login e eventos de segurança                 |     Alta    | Dificuldade para detectar e investigar incidentes                  |
| Servidores                    | Mantêm o sistema disponível e processam suas operações                        |     Alta    | Interrupção ou indisponibilidade do serviço                        |
| APIs                          | Permitem a comunicação entre aplicativos, servidores e serviços externos      |     Alta    | Vazamento, interceptação ou alteração de dados                     |
| Aplicativo móvel              | Interface utilizada pelos clientes e entregadores                             |     Alta    | Acesso indevido às funcionalidades ou indisponibilidade do serviço |

Os ativos considerados mais críticos são os dados pessoais, as credenciais, os tokens de autenticação, os dados de pagamento, os endereços, a localização, os pedidos, os cancelamentos e reembolsos, as configurações do sistema, os logs de auditoria e o banco de dados.


# 2.3 Serviços externos

O sistema de delivery depende de serviços fornecidos por empresas externas para realizar determinadas operações. Embora esses serviços não sejam controlados diretamente pela plataforma, falhas, ataques ou indisponibilidades podem comprometer o funcionamento e a segurança do sistema.

| Serviço externo                   | Finalidade                                                                             | Risco relacionado                                                                   |
| --------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Gateway de pagamento              | Processar pagamentos, confirmar transações e realizar estornos                         | Fraudes, vazamento de informações, transações incorretas ou indisponibilidade       |
| Serviço de mapas e GPS            | Calcular rotas, localizar endereços e acompanhar entregas                              | Exposição da localização, rastreamento indevido ou fornecimento de rotas incorretas |
| Serviço de notificações           | Enviar atualizações sobre pedidos por notificação, SMS ou e-mail                       | Mensagens falsas, atrasadas, interceptadas ou não entregues                         |
| Provedor de autenticação          | Permitir o acesso por contas externas, como Google ou Apple                            | Acesso indevido caso a conta externa ou o provedor seja comprometido                |
| Serviço de armazenamento em nuvem | Armazenar documentos, imagens, registros e outros arquivos do sistema                  | Vazamento, alteração, perda de dados ou indisponibilidade                           |
| Serviço de comunicação            | Permitir a troca de mensagens entre clientes, estabelecimentos, entregadores e suporte | Interceptação de mensagens, exposição de informações ou aplicação de golpes         |

A integração com esses serviços deve ocorrer por meio de conexões seguras e APIs autenticadas. A plataforma também deve limitar as informações compartilhadas, proteger as chaves de acesso e registrar as operações realizadas. Além disso, deve prever medidas alternativas para reduzir os impactos causados pela falha ou indisponibilidade de um serviço externo.


# 2.4 Pontos de interação

Os pontos de interação representam as funcionalidades pelas quais usuários, componentes internos e serviços externos trocam informações. Esses pontos precisam ser protegidos, pois podem ser utilizados como portas de entrada para ataques, fraudes e acessos não autorizados.

| Ponto de interação        | Envolvidos                                               | Informações utilizadas                                                       |
| ------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Cadastro de usuário       | Usuário, aplicativo e servidor                           | Dados pessoais, credenciais e, quando aplicável, documentos de identificação |
| Login                     | Usuário, aplicativo e servidor                           | E-mail, telefone, senha e dados da sessão                                    |
| Recuperação de senha      | Usuário, servidor e serviço de notificação               | E-mail, telefone e código de recuperação                                     |
| Consulta ao cardápio      | Cliente, aplicativo e estabelecimento                    | Produtos, preços e disponibilidade                                           |
| Gerenciamento do cardápio | Estabelecimento, aplicativo e servidor                   | Produtos, descrições, preços e disponibilidade                               |
| Realização do pedido      | Cliente, estabelecimento e servidor                      | Produtos, quantidades, valores e endereço de entrega                         |
| Pagamento                 | Cliente, sistema e gateway de pagamento                  | Valor, forma de pagamento, token da transação e identificação do pedido      |
| Aceitação do pedido       | Estabelecimento e sistema                                | Informações do pedido e tempo estimado de preparo                            |
| Cancelamento e reembolso  | Cliente, estabelecimento, suporte e gateway de pagamento | Motivo do cancelamento, situação do pedido e valor do reembolso              |
| Solicitação de entrega    | Sistema e entregador                                     | Informações do pedido, endereços e localização                               |
| Atualização da entrega    | Entregador, aplicativo e servidor                        | Situação do pedido e confirmação da entrega                                  |
| Acompanhamento da entrega | Cliente, entregador, aplicativo e serviço de GPS         | Localização e andamento da entrega                                           |
| Troca de mensagens        | Cliente, entregador, estabelecimento e suporte           | Mensagens e informações relacionadas ao pedido                               |
| Avaliação do serviço      | Cliente, estabelecimento, entregador e sistema           | Nota e comentário                                                            |
| Atendimento de suporte    | Usuário, atendente e sistema                             | Dados do pedido, reclamações, mensagens e solicitações                       |
| Painel administrativo     | Administrador, servidor e banco de dados                 | Dados de usuários, pedidos, configurações e registros de operações           |

Esses pontos de interação devem utilizar mecanismos adequados de autenticação, autorização, criptografia e validação das informações. Também é necessário registrar as operações importantes para permitir a identificação e a investigação de possíveis fraudes ou incidentes de segurança.
