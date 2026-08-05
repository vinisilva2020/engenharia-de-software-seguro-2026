# 2. Usuários, ativos e pontos de interação

O sistema que o grupo escolheu é uma plataforma de delivery de alimentos. Ele conecta clientes, estabelecimentos e entregadores, permitindo consultar cardápios, realizar pedidos, efetuar pagamentos, acompanhar entregas e avaliar os serviços prestados.

## 2.1 Usuários e perfis de acesso

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

Os ativos são recursos que precisam ser protegidos. O acesso, a alteração, a destruição ou a indisponibilidade desses elementos pode provocar prejuízos aos usuários e à plataforma.

Ativo	Descrição	Importância	Possível prejuízo
Dados pessoais	Nome, CPF, telefone e e-mail dos usuários	Alta	Violação de privacidade e utilização indevida dos dados
Credenciais	E-mail, senha e códigos de acesso	Alta	Invasão e roubo de contas
Dados de pagamento	Informações utilizadas para realizar o pagamento	Alta	Fraudes e prejuízos financeiros
Endereço do cliente	Local informado para a entrega do pedido	Alta	Exposição da residência e risco à segurança
Localização do entregador	Posição obtida por GPS durante a entrega	Alta	Rastreamento indevido e violação de privacidade
Pedidos	Produtos, quantidades, valores, endereço e estado do pedido	Alta	Alteração indevida, cobrança incorreta ou entrega errada
Cardápios e preços	Produtos e valores cadastrados pelos estabelecimentos	Alta	Cobranças incorretas e prejuízo financeiro
Mensagens	Comunicação entre cliente, entregador, estabelecimento e suporte	Média	Exposição de informações e aplicação de golpes
Avaliações	Notas e comentários publicados pelos clientes	Média	Manipulação das avaliações e danos à reputação
Documentos	Documentos de identificação de entregadores e estabelecimentos	Alta	Fraude de identidade e cadastro de usuários falsos
Banco de dados	Armazena usuários, pedidos, pagamentos e avaliações	Alta	Vazamento, alteração ou perda de informações
Histórico de operações	Registros de acessos, pedidos, pagamentos e alterações	Alta	Dificuldade para identificar fraudes e responsabilizar usuários
Servidores	Mantêm o sistema disponível e processam as operações	Alta	Interrupção ou indisponibilidade do serviço
APIs	Permitem a comunicação entre aplicativos, servidores e serviços externos	Alta	Vazamento, interceptação ou alteração de dados
Aplicativo móvel	Interface utilizada pelos clientes e entregadores	Alta	Acesso indevido às funcionalidades ou indisponibilidade do serviço

Os ativos considerados mais críticos são os dados pessoais, as credenciais, os dados de pagamento, os endereços, a localização, os pedidos e o banco de dados.

# 2.3 Serviços externos

O sistema de delivery também depende de serviços fornecidos por outras empresas.

Serviço externo	Finalidade	Risco relacionado
Gateway de pagamento	Processar pagamentos	Fraude, vazamento de informações ou indisponibilidade
Serviço de mapas e GPS	Calcular rotas e acompanhar entregas	Exposição da localização ou fornecimento de rotas incorretas
Serviço de notificações	Enviar atualizações sobre os pedidos	Mensagens falsas, atrasadas ou não entregues
Provedor de autenticação	Permitir acesso por contas como Google ou Apple	Acesso indevido caso a conta externa seja comprometida
Serviço de armazenamento em nuvem	Armazenar dados e arquivos do sistema	Vazamento, alteração ou perda de dados

# 2.4 Pontos de interação

Os pontos de interação representam os locais ou funcionalidades pelos quais usuários, componentes internos e serviços externos trocam informações.

Ponto de interação	Envolvidos	Informações utilizadas
Cadastro de usuário	Usuário, aplicativo e servidor	Dados pessoais, documentos e credenciais
Login	Usuário, aplicativo e servidor	E-mail, telefone e senha
Recuperação de senha	Usuário, servidor e serviço de notificação	E-mail, telefone e código de recuperação
Consulta ao cardápio	Cliente, aplicativo e estabelecimento	Produtos, preços e disponibilidade
Realização do pedido	Cliente, estabelecimento e servidor	Produtos, valores e endereço
Pagamento	Cliente, sistema e gateway de pagamento	Valor, forma de pagamento e identificação do pedido
Aceitação do pedido	Estabelecimento e sistema	Informações do pedido e tempo de preparo
Solicitação de entrega	Sistema e entregador	Dados do pedido, localização e endereços
Acompanhamento da entrega	Cliente, entregador, aplicativo e GPS	Localização e andamento da entrega
Troca de mensagens	Cliente, entregador, estabelecimento e suporte	Mensagens e informações do pedido
Avaliação do serviço	Cliente, estabelecimento e entregador	Nota e comentário
Atendimento de suporte	Usuário, atendente e sistema	Pedido, reclamação e mensagens
Painel administrativo	Administrador, servidor e banco de dados	Dados de usuários, pedidos e configurações