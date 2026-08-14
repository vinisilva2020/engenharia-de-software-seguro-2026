# Etapa 6 - Monitoramento e Detecção de Intrusões

## 1. Objetivo e escopo

Esta etapa apresenta uma proposta de monitoramento e detecção para o sistema de delivery analisado pelo grupo. O objetivo é definir quais atividades relevantes devem ser registradas, como os registros podem revelar comportamentos suspeitos e quais ações iniciais devem ocorrer quando um alerta for gerado.

A proposta é conceitual e não exige a implementação de um IDS. Ela utiliza como base os usuários, ativos, pontos de interação, ameaças STRIDE e riscos já identificados nas etapas anteriores, especialmente os riscos relacionados ao comprometimento de contas, à exposição de dados, à elevação de privilégios e à indisponibilidade da aplicação.

## 2. O que é detecção de intrusões

Detecção de intrusões é o processo de observar eventos produzidos por aplicações, APIs, serviços, bancos de dados e componentes de infraestrutura para identificar tentativas de ataque, violações de políticas ou comportamentos incompatíveis com o uso esperado do sistema.

No sistema de delivery, a detecção pode revelar, por exemplo, repetidas tentativas de acesso a uma conta administrativa, consultas indevidas a dados de clientes ou um volume anormal de requisições capaz de degradar a aplicação. Para isso, os registros de diferentes fontes devem ser centralizados, correlacionados e analisados por regras com condições objetivas de alerta.

Um alerta representa um indício que precisa ser validado. Ele não comprova automaticamente que ocorreu um incidente, pois também pode ter sido provocado por erro de configuração, falha operacional ou uso legítimo fora do padrão.

## 3. Diferença entre prevenir e detectar

| Aspecto                  | Prevenção                                                                         | Detecção                                                                                                  |
| ------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Objetivo**             | Impedir ou dificultar que uma ameaça seja concretizada.                           | Identificar rapidamente uma tentativa, violação ou incidente em andamento ou já ocorrido.                 |
| **Momento de atuação**   | Antes ou durante a tentativa de ataque.                                           | Durante ou depois do evento suspeito.                                                                     |
| **Exemplos no delivery** | MFA, RBAC, menor privilégio, validação no servidor, rate limiting e criptografia. | Análise de falhas de login, acessos negados, consultas anormais a dados, erros da API e picos de tráfego. |
| **Resultado esperado**   | Reduzir a probabilidade de sucesso do ataque.                                     | Diminuir o tempo de descoberta, apoiar a contenção e preservar evidências para investigação.              |

Prevenção e detecção são complementares. Mesmo controles preventivos bem configurados podem ser contornados, apresentar falhas ou não cobrir todas as situações. Por esse motivo, os mesmos componentes que aplicam controles de segurança também devem produzir registros suficientes para demonstrar o que ocorreu e permitir uma resposta rápida.

## 4. Eventos do sistema que devem gerar logs

Os eventos devem ser registrados de forma estruturada e enviados para um ponto central de monitoramento. A tabela abaixo define os principais registros necessários para o sistema de delivery.

| Categoria                      | Eventos que devem ser registrados                                                                                                                                                          | Relação com os riscos |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| **Autenticação e sessões**     | Login bem-sucedido ou malsucedido; falha de MFA; recuperação de acesso; criação, renovação, revogação e encerramento de sessão; tentativa de reutilizar token revogado.                    | R01, R02, R03 e R04   |
| **Autorização e privilégios**  | Respostas 401 e 403; tentativa de acessar endpoint restrito; concessão ou revogação de papel; mudança de permissão; operação administrativa permitida ou recusada.                         | R04, R17, R18 e R19   |
| **Dados pessoais e sensíveis** | Consulta, alteração, exportação ou exclusão de dados pessoais; perfil utilizado; recurso consultado; resultado da autorização; acesso a documentos e localização.                          | R11, R12, R13 e R14   |
| **Pedidos e cardápios**        | Criação, confirmação, alteração e cancelamento de pedido; mudança de produtos, quantidades, preços, promoções e status; valores anterior e novo quando aplicável.                          | R05, R07 e R09        |
| **Pagamentos e reembolsos**    | Início e resultado da transação; valor e identificador; confirmação, recusa, estorno ou reembolso; validação de webhook; timeout; erro do provedor; abertura do circuit breaker.           | R06, R08, R14 e R16   |
| **Entregas**                   | Aceitação da entrega; alterações de status; conta responsável; confirmação de entrega; uso do código de confirmação; acesso à localização e tentativa de acesso após a conclusão.          | R03, R10 e R13        |
| **Suporte e administração**    | Consulta de chamado; bloqueio ou desbloqueio de conta; reembolso manual; mudança de configuração; alteração de limite; operação de suporte ou administrativa e eventual segunda aprovação. | R04, R08, R18 e R19   |
| **Arquivos e documentos**      | Envio, consulta e exclusão de arquivo; tipo, tamanho e hash; resultado da validação de formato e da verificação contra conteúdo malicioso.                                                 | R11, R12 e R13        |
| **APIs e disponibilidade**     | Quantidade de requisições; origem; rota normalizada; método; tempo de resposta; códigos 4xx e 5xx; acionamento de rate limiting; uso de CPU e memória; falha de dependência externa.       | R15 e R16             |
| **Eventos de segurança**       | Violação de política; entrada rejeitada; assinatura inválida de webhook; tentativa de repetição; parâmetro sensível detectado em URL; alteração ou indisponibilidade do mecanismo de logs. | R06, R11, R14 e R15   |

### 4.1 Campos mínimos de cada registro

Sempre que forem aplicáveis, os registros devem conter:

- data e hora sincronizadas, preferencialmente em UTC;
- identificador único do evento;
- identificador da requisição ou de correlação;
- identificador do usuário e seu perfil, sem expor credenciais;
- endereço IP e identificação de origem ou dispositivo;
- ação realizada e recurso afetado;
- resultado da ação: sucesso, falha, bloqueio ou recusa;
- motivo técnico da falha ou da recusa;
- valores anterior e novo em alterações críticas, com mascaramento de dados;
- componente que produziu o registro e nível de severidade.

Esses campos permitem relacionar eventos produzidos pelo aplicativo, Backend/API, serviço de autenticação, gateway de pagamento, banco de dados e infraestrutura.

### 4.2 Proteção e privacidade dos logs

Os logs também são ativos importantes e devem possuir controle de acesso, proteção contra alteração e exclusão indevida, cópias de segurança e prazo de retenção definido. Somente pessoas autorizadas devem consultar os registros completos.

Senhas, códigos de MFA, chaves de API, tokens completos, dados completos de cartão e conteúdo integral de documentos nunca devem ser gravados. Dados pessoais devem ser mascarados ou substituídos por identificadores quando o valor completo não for necessário para a investigação.

O achado do OWASP ZAP sobre informações sensíveis em URL reforça esse cuidado. O sistema deve usar POST para enviar credenciais e outros dados sensíveis e, no monitoramento, registrar apenas a rota normalizada e o nome do parâmetro detectado, nunca o valor da query string. O corpo de uma requisição também não deve ser copiado integralmente para o log quando contiver informações confidenciais.

# Etapa 6 - Monitoramento e Detecção de Intrusões

## 1. Objetivo e escopo

Esta etapa apresenta uma proposta de monitoramento e detecção para o sistema de delivery analisado pelo grupo. O objetivo é definir quais atividades relevantes devem ser registradas, como os registros podem revelar comportamentos suspeitos e quais ações iniciais devem ocorrer quando um alerta for gerado.

A proposta é conceitual e não exige a implementação de um IDS. Ela utiliza como base os usuários, ativos, pontos de interação, ameaças STRIDE e riscos já identificados nas etapas anteriores, especialmente os riscos relacionados ao comprometimento de contas, à exposição de dados, à elevação de privilégios e à indisponibilidade da aplicação.

## 2. O que é detecção de intrusões

Detecção de intrusões é o processo de observar eventos produzidos por aplicações, APIs, serviços, bancos de dados e componentes de infraestrutura para identificar tentativas de ataque, violações de políticas ou comportamentos incompatíveis com o uso esperado do sistema.

No sistema de delivery, a detecção pode revelar, por exemplo, repetidas tentativas de acesso a uma conta administrativa, consultas indevidas a dados de clientes ou um volume anormal de requisições capaz de degradar a aplicação. Para isso, os registros de diferentes fontes devem ser centralizados, correlacionados e analisados por regras com condições objetivas de alerta.

Um alerta representa um indício que precisa ser validado. Ele não comprova automaticamente que ocorreu um incidente, pois também pode ter sido provocado por erro de configuração, falha operacional ou uso legítimo fora do padrão.

## 3. Diferença entre prevenir e detectar

| Aspecto                  | Prevenção                                                                         | Detecção                                                                                                  |
| ------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Objetivo**             | Impedir ou dificultar que uma ameaça seja concretizada.                           | Identificar rapidamente uma tentativa, violação ou incidente em andamento ou já ocorrido.                 |
| **Momento de atuação**   | Antes ou durante a tentativa de ataque.                                           | Durante ou depois do evento suspeito.                                                                     |
| **Exemplos no delivery** | MFA, RBAC, menor privilégio, validação no servidor, rate limiting e criptografia. | Análise de falhas de login, acessos negados, consultas anormais a dados, erros da API e picos de tráfego. |
| **Resultado esperado**   | Reduzir a probabilidade de sucesso do ataque.                                     | Diminuir o tempo de descoberta, apoiar a contenção e preservar evidências para investigação.              |

Prevenção e detecção são complementares. Mesmo controles preventivos bem configurados podem ser contornados, apresentar falhas ou não cobrir todas as situações. Por esse motivo, os mesmos componentes que aplicam controles de segurança também devem produzir registros suficientes para demonstrar o que ocorreu e permitir uma resposta rápida.

## 4. Eventos do sistema que devem gerar logs

Os eventos devem ser registrados de forma estruturada e enviados para um ponto central de monitoramento. A tabela abaixo define os principais registros necessários para o sistema de delivery.

| Categoria                      | Eventos que devem ser registrados                                                                                                                                                          | Relação com os riscos |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| **Autenticação e sessões**     | Login bem-sucedido ou malsucedido; falha de MFA; recuperação de acesso; criação, renovação, revogação e encerramento de sessão; tentativa de reutilizar token revogado.                    | R01, R02, R03 e R04   |
| **Autorização e privilégios**  | Respostas 401 e 403; tentativa de acessar endpoint restrito; concessão ou revogação de papel; mudança de permissão; operação administrativa permitida ou recusada.                         | R04, R17, R18 e R19   |
| **Dados pessoais e sensíveis** | Consulta, alteração, exportação ou exclusão de dados pessoais; perfil utilizado; recurso consultado; resultado da autorização; acesso a documentos e localização.                          | R11, R12, R13 e R14   |
| **Pedidos e cardápios**        | Criação, confirmação, alteração e cancelamento de pedido; mudança de produtos, quantidades, preços, promoções e status; valores anterior e novo quando aplicável.                          | R05, R07 e R09        |
| **Pagamentos e reembolsos**    | Início e resultado da transação; valor e identificador; confirmação, recusa, estorno ou reembolso; validação de webhook; timeout; erro do provedor; abertura do circuit breaker.           | R06, R08, R14 e R16   |
| **Entregas**                   | Aceitação da entrega; alterações de status; conta responsável; confirmação de entrega; uso do código de confirmação; acesso à localização e tentativa de acesso após a conclusão.          | R03, R10 e R13        |
| **Suporte e administração**    | Consulta de chamado; bloqueio ou desbloqueio de conta; reembolso manual; mudança de configuração; alteração de limite; operação de suporte ou administrativa e eventual segunda aprovação. | R04, R08, R18 e R19   |
| **Arquivos e documentos**      | Envio, consulta e exclusão de arquivo; tipo, tamanho e hash; resultado da validação de formato e da verificação contra conteúdo malicioso.                                                 | R11, R12 e R13        |
| **APIs e disponibilidade**     | Quantidade de requisições; origem; rota normalizada; método; tempo de resposta; códigos 4xx e 5xx; acionamento de rate limiting; uso de CPU e memória; falha de dependência externa.       | R15 e R16             |
| **Eventos de segurança**       | Violação de política; entrada rejeitada; assinatura inválida de webhook; tentativa de repetição; parâmetro sensível detectado em URL; alteração ou indisponibilidade do mecanismo de logs. | R06, R11, R14 e R15   |

### 4.1 Campos mínimos de cada registro

Sempre que forem aplicáveis, os registros devem conter:

- data e hora sincronizadas, preferencialmente em UTC;
- identificador único do evento;
- identificador da requisição ou de correlação;
- identificador do usuário e seu perfil, sem expor credenciais;
- endereço IP e identificação de origem ou dispositivo;
- ação realizada e recurso afetado;
- resultado da ação: sucesso, falha, bloqueio ou recusa;
- motivo técnico da falha ou da recusa;
- valores anterior e novo em alterações críticas, com mascaramento de dados;
- componente que produziu o registro e nível de severidade.

Esses campos permitem relacionar eventos produzidos pelo aplicativo, Backend/API, serviço de autenticação, gateway de pagamento, banco de dados e infraestrutura.

### 4.2 Proteção e privacidade dos logs

Os logs também são ativos importantes e devem possuir controle de acesso, proteção contra alteração e exclusão indevida, cópias de segurança e prazo de retenção definido. Somente pessoas autorizadas devem consultar os registros completos.

Senhas, códigos de MFA, chaves de API, tokens completos, dados completos de cartão e conteúdo integral de documentos nunca devem ser gravados. Dados pessoais devem ser mascarados ou substituídos por identificadores quando o valor completo não for necessário para a investigação.

O achado do OWASP ZAP sobre informações sensíveis em URL reforça esse cuidado. O sistema deve usar POST para enviar credenciais e outros dados sensíveis e, no monitoramento, registrar apenas a rota normalizada e o nome do parâmetro detectado, nunca o valor da query string. O corpo de uma requisição também não deve ser copiado integralmente para o log quando contiver informações confidenciais.

## 5. Regras de detecção

### 5.1 RD01 - Tentativas suspeitas de acesso administrativo

| Item                    | Definição                                                                                                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Risco observado**     | **R04 - Comprometimento de conta administrativa**, com relação adicional aos riscos R01, R02 e R03 de comprometimento de contas.                                                                                                                                                                    |
| **Fonte dos dados/log** | Logs do serviço de autenticação, do MFA, do Backend/API e do gerenciador de sessões. Eventos principais: falha de login, login bem-sucedido, falha de MFA, criação de sessão e revogação de token.                                                                                                  |
| **Condição de alerta**  | Gerar alerta quando ocorrerem **5 ou mais falhas de login para a mesma conta administrativa ou originadas do mesmo IP em até 5 minutos**. Elevar a severidade se ocorrer um login administrativo bem-sucedido nos 10 minutos seguintes a 3 ou mais falhas da mesma origem.                          |
| **Resposta inicial**    | Aplicar limitação temporária à origem, exigir nova verificação de MFA, avisar o responsável pela conta e a equipe de segurança e preservar os identificadores das requisições. Se houve login bem-sucedido após as falhas, revogar as sessões administrativas ativas até a validação da identidade. |

A regra busca identificar força bruta, preenchimento automatizado de credenciais ou uso de senha comprometida. A limitação deve priorizar a origem da atividade e não bloquear permanentemente a conta apenas pelas falhas, pois um atacante poderia provocar negação de serviço contra o administrador.

A severidade inicial será **alta** para a sequência de falhas e **crítica** quando houver autenticação administrativa bem-sucedida após o comportamento suspeito.
