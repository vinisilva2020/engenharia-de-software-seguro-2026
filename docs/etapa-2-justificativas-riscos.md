# Justificativas das avaliações

## 8.1 Justificativas das avaliações

### R01 - Acesso indevido à conta de cliente

**Probabilidade 3 -  Média-alta:** o comprometimento de credenciais pode ocorrer em situações comuns, como reutilização de senhas, phishing ou vazamento de credenciais.

**Impacto 3 - Alto:** o atacante poderá realizar pedidos em nome do cliente e visualizar seus dados pessoais, causando prejuízo financeiro, violação de privacidade e perda de confiança.

O risco afeta principalmente clientes, suas contas, dados pessoais, histórico de pedidos e funcionalidades de compra. A pontuação **9 - Alto** é adequada pela combinação entre ocorrência plausível e consequências relevantes.

### R02 - Comprometimento de conta empresarial

**Probabilidade 3 - Média-alta:** contas de estabelecimentos também podem sofrer comprometimento de credenciais em situações comuns de ataque.

**Impacto 3 - Alto:** o invasor poderá alterar preços, produtos e informações comerciais ou interferir em pedidos.

São afetados estabelecimentos, clientes, cardápios e pedidos. A pontuação **9 — Alto** representa adequadamente o potencial de prejuízo operacional e financeiro.

### R03 - Comprometimento de conta de entregador

**Probabilidade 3 - Média-alta:** credenciais de entregadores podem ser obtidas por ataques de phishing, reutilização de senha ou outros meios de comprometimento de contas.

**Impacto 3 - Alto:** o atacante poderá aceitar, cancelar ou manipular entregas, gerando atrasos, fraudes e conflitos.

O risco pode afetar entregadores, clientes, empresas e o processo de entrega. A pontuação **9 - Alto** é adequada devido aos impactos operacionais e financeiros.

### R04 - Comprometimento de conta administrativa

**Probabilidade 3 - Média-alta:** contas administrativas são alvos relevantes, e suas credenciais podem ser comprometidas por ataques comuns.

**Impacto 4 - Muito alto:** uma conta administrativa poderá permitir acesso a dados, contas, pedidos e funcionalidades críticas.

O risco pode afetar praticamente todo o sistema e diversos usuários simultaneamente. Por isso, a pontuação **12 - Crítico** representa adequadamente sua gravidade.

### R05 - Manipulação de pedidos

**Probabilidade 3 - Média-alta:** é plausível quando informações enviadas pelo cliente não são devidamente verificadas no servidor.

**Impacto 3 - Alto:** alterações em produtos, preços e quantidades podem causar fraude, perdas financeiras e comprometimento da integridade.

O risco afeta clientes, empresas, pedidos e faturamento. A pontuação **9 - Alto** é compatível com o contexto.

### R06 - Manipulação de transações

**Probabilidade 2 - Média-baixa:** a exploração depende de falha específica no processamento, validação ou comunicação da transação.

**Impacto 4 - Muito alto:** alterações em valores ou destinatários podem resultar em fraudes e perdas financeiras graves.

São afetados clientes, empresas, pagamentos e registros financeiros. A pontuação **8  - Alto** considera a menor probabilidade, mas o impacto elevado.

### R07 - Alteração não autorizada de dados comerciais

**Probabilidade 3 - Média-alta:** o evento é plausível caso existam falhas na validação das permissões de usuários empresariais.

**Impacto 3 - Alto:** alterações em preços e promoções podem causar vendas com valores incorretos e prejuízos.

Afeta estabelecimentos, clientes, cardápios e operações comerciais. A classificação **Alto (9)** é apropriada.

### R08 - Contestação de pagamento ou reembolso

**Probabilidade 3 - Média-alta:** contestações de operações financeiras são situações plausíveis em sistemas comerciais.

**Impacto 3 - Alto:** sem registros adequados, a empresa pode ter dificuldade de demonstrar a realização da operação e sofrer prejuízos.

Afeta clientes, empresas, pagamentos e processos de auditoria. O nível **Alto (9)** é adequado.

### R09 - Contestação da realização de pedido

**Probabilidade 3 - Média-alta:** um cliente poderá contestar um pedido principalmente quando os registros do sistema forem insuficientes.

**Impacto 2 - Moderado:** normalmente a consequência está limitada a pedidos específicos e pode ser investigada ou compensada.

Afeta clientes, estabelecimentos e pedidos. O nível **Médio (6)** representa adequadamente uma ocorrência plausível com impacto mais limitado.

### R10 - Falsa confirmação de entrega

**Probabilidade 3 - Média-alta:** sem um mecanismo confiável de confirmação, existe possibilidade real de uma entrega ser declarada concluída indevidamente.

**Impacto 3 - Alto:** poderá haver perdas financeiras, reembolsos, reclamações e conflitos.

Afeta clientes, entregadores, empresas e registros de entrega. O nível **Alto (9)** é adequado.

### R11 - Exposição de dados dos clientes

**Probabilidade 3 - Média-alta:** o sistema armazena e processa constantemente dados pessoais, tornando tentativas de acesso indevido plausíveis.

**Impacto 4 - Muito alto:** uma exposição pode atingir diversos clientes, comprometer sua privacidade e provocar consequências jurídicas e reputacionais.

São afetados dados como CPF, endereço, telefone, e-mail e histórico de pedidos. Por isso, a classificação **Crítico (12)** é adequada.

### R12 - Exposição de dados das empresas

**Probabilidade 2 - Média-baixa:** depende de falha específica no controle de acesso ou na proteção dos documentos.

**Impacto 3 - Alto:** poderá expor informações comerciais, documentos e dados estratégicos.

O risco afeta principalmente empresas cadastradas e seus dados. O nível **Médio (6)** decorre da menor probabilidade, apesar de consequências relevantes.

### R13 - Exposição de dados dos entregadores

**Probabilidade 2 - Média-baixa:** depende de uma condição ou vulnerabilidade específica de acesso aos registros.

**Impacto 3 - Alto:** poderá expor CPF, telefone e dados de veículo, facilitando golpes e engenharia social.

Afeta a privacidade e segurança dos entregadores. A classificação **Médio (6)** é adequada.

### R14 - Exposição de informações financeiras

**Probabilidade 2 - Média-baixa:** depende de vulnerabilidade específica no armazenamento, transmissão ou acesso aos dados de pagamento.

**Impacto 4 - Muito alto:** uma exposição poderá facilitar fraudes e comprometer informações relacionadas às transações.

Afeta clientes, empresas, sistema de pagamento e informações financeiras. O nível **Alto (8)** considera a elevada gravidade mesmo com probabilidade menor.

### R15 - Indisponibilidade da aplicação por DoS

**Probabilidade 3 - Média-alta:** aplicações acessíveis pela Internet podem ser alvo de sobrecarga deliberada.

**Impacto 4 - Muito alto:** a indisponibilidade poderá impedir simultaneamente clientes de realizar pedidos, empresas de receber solicitações e entregadores de trabalhar.

A abrangência do evento justifica a classificação **Crítico (12)**.

### R16 - Indisponibilidade da API de pagamentos

**Probabilidade 3 - Média-alta:** indisponibilidades de serviços externos são condições previsíveis em sistemas dependentes de terceiros.

**Impacto 4 - Muito alto:** sem o serviço de pagamento, pedidos que dependam dessa forma de pagamento poderão não ser concluídos, provocando perda de vendas.

A classificação **Crítico (12)** considera a dependência de uma operação essencial do sistema.

### R17 - Elevação de privilégio de cliente

**Probabilidade 2 - Média-baixa:** depende da existência de uma vulnerabilidade específica na autorização.

**Impacto 4 - Muito alto:** caso obtenha privilégios administrativos, o atacante poderá acessar dados e executar operações críticas.

O risco afeta todo o sistema e usuários administrativos. O nível **Alto (8)** representa a baixa probabilidade combinada ao impacto muito elevado.

### R18 - Elevação de privilégio de funcionário

**Probabilidade 2 - Média-baixa:** depende de configuração incorreta ou vulnerabilidade específica no controle de papéis.

**Impacto 3 - Alto:** poderá permitir alterações indevidas em produtos, preços, pedidos e informações do estabelecimento.

O risco afeta principalmente empresas e suas operações. O nível **Médio (6)** é adequado ao contexto.

### R19 - Acesso de usuário comum a funções administrativas

**Probabilidade 2 - Média-baixa:** depende de vulnerabilidade específica na verificação de autorização.

**Impacto 4 - Muito alto:** poderá resultar em acesso a informações confidenciais e operações administrativas críticas.

O risco afeta a segurança geral do sistema e possui classificação **Alto (8)**.

---