# Justificativa da escolha do sistema

O sistema escolhido foi um sistema de delivery, devido à sua ampla utilização e à complexidade das interações entre os diferentes atores envolvidos. Esse domínio conta com uma estrutura hierárquica de administração, composta por empresas responsáveis pela oferta dos serviços, funcionários que gerenciam as operações e clientes que realizam pedidos, cada um com diferentes níveis de acesso, permissões e responsabilidades.

Essas características tornam o sistema um cenário adequado para a aplicação dos conceitos de Engenharia de Software Seguro, pois permitem analisar diferentes requisitos de segurança, identificar potenciais vulnerabilidades e desenvolver casos de abuso que representam possíveis ataques ou usos indevidos do sistema. Além disso, é possível avaliar mecanismos de autenticação, autorização, controle de acesso, proteção de dados sensíveis e garantia da confidencialidade, integridade e disponibilidade das informações processadas pela aplicação.


# Descrição do sistema

O sistema de delivery é amplamente utilizado na sociedade, permitindo
que os clientes solicitem produtos e serviços sem a necessidade de se
deslocarem até o estabelecimento. Essa praticidade beneficia tanto os
consumidores, que conseguem atender às suas necessidades de forma rápida
e conveniente, quanto as empresas, que ampliam seu alcance, atendem um
maior número de clientes e organizam melhor seus processos de venda e
entrega.

Os principais atores do sistema são os **clientes**, responsáveis por
realizar pedidos e efetuar pagamentos, e as **empresas**, que
disponibilizam produtos ou serviços, gerenciam os pedidos e realizam o
atendimento aos consumidores. Dependendo da implementação, também podem
existir administradores e entregadores, cada um com diferentes níveis de
acesso e responsabilidades.

Entre as principais funcionalidades do sistema estão:

-   **Cadastro e autenticação de usuários;**

-   **Cadastro e gerenciamento de estabelecimentos e produtos;**

-   **Realização de pedidos;**

-   **Processamento de pagamentos;**

-   **Acompanhamento do status do pedido;**

-   **Gerenciamento de entregas;**

-   **Avaliação dos produtos e serviços.**

Para oferecer essas funcionalidades, o sistema armazena e transmite
diversas informações dos usuários, como nome, CPF, número de telefone,
endereço de e-mail, endereço de entrega e dados de pagamento, como chave
Pix ou informações de cartão de crédito (preferencialmente por meio de
provedores de pagamento especializados, sem armazenar dados completos do
cartão). Parte dessas informações é considerada **dado pessoal** e, em
alguns casos, pode envolver **dados pessoais sensíveis** quando
associada a outras informações previstas na Lei Geral de Proteção de
Dados (LGPD).

Dessa forma, é fundamental que o sistema adote mecanismos de segurança
capazes de garantir a confidencialidade, a integridade e a
disponibilidade dessas informações. Medidas como autenticação segura,
controle de acesso, criptografia, monitoramento e conformidade com a
LGPD são essenciais para prevenir vazamentos, acessos não autorizados e
outros incidentes que possam comprometer a privacidade e a segurança dos
usuários.