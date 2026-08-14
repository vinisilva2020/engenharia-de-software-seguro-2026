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


## 5. Regras de detecção

### 5.1 RD01 - Tentativas suspeitas de acesso administrativo

| Item | Definição |
| --- | --- |
| **Risco observado** | **R04 - Comprometimento de conta administrativa**, com relação adicional aos riscos R01, R02 e R03 de comprometimento de contas. |
| **Fonte dos dados/log** | Logs do serviço de autenticação, do MFA, do Backend/API e do gerenciador de sessões. Eventos principais: falha de login, login bem-sucedido, falha de MFA, criação de sessão e revogação de token. |
| **Condição de alerta** | Gerar alerta quando ocorrerem **5 ou mais falhas de login para a mesma conta administrativa ou originadas do mesmo IP em até 5 minutos**. Elevar a severidade se ocorrer um login administrativo bem-sucedido nos 10 minutos seguintes a 3 ou mais falhas da mesma origem. |
| **Resposta inicial** | Aplicar limitação temporária à origem, exigir nova verificação de MFA, avisar o responsável pela conta e a equipe de segurança e preservar os identificadores das requisições. Se houve login bem-sucedido após as falhas, revogar as sessões administrativas ativas até a validação da identidade. |

A regra busca identificar força bruta, preenchimento automatizado de credenciais ou uso de senha comprometida. A limitação deve priorizar a origem da atividade e não bloquear permanentemente a conta apenas pelas falhas, pois um atacante poderia provocar negação de serviço contra o administrador.

A severidade inicial será **alta** para a sequência de falhas e **crítica** quando houver autenticação administrativa bem-sucedida após o comportamento suspeito.

### 5.2 RD02 - Tentativas de acesso indevido a dados ou funções restritas

| Item | Definição |
| --- | --- |
| **Risco observado** | **R11 - Exposição de dados dos clientes**, **R17 - Elevação de privilégio de cliente** e **R19 - Acesso de usuário comum a funções administrativas**. |
| **Fonte dos dados/log** | Logs de autorização do Backend/API, respostas 401 e 403, trilha de auditoria de acesso a dados pessoais e registros de consulta do banco de dados. Eventos principais: acesso recusado, acesso a dado pessoal e chamada de endpoint administrativo. |
| **Condição de alerta** | Gerar alerta quando a mesma conta ou sessão produzir **3 ou mais recusas de autorização em até 10 minutos** ao tentar acessar endpoints administrativos ou dados de terceiros. Também gerar alerta quando uma conta consultar **5 ou mais registros de clientes sem relação com pedido, entrega ou chamado autorizado em até 5 minutos**. |
| **Resposta inicial** | Interromper ou revogar a sessão suspeita, aplicar bloqueio temporário, preservar os registros correlacionados e verificar se algum dado foi efetivamente retornado. Confirmar se a conta foi comprometida e, em caso de exposição, acionar o responsável pela proteção de dados e o processo de resposta a incidentes. |

A regra detecta tentativas de alterar identificadores de recursos, enumerar dados de clientes ou acessar funções incompatíveis com o perfil. Contas de suporte e administração também devem possuir justificativa de negócio, como um chamado ou operação autorizada, para consultas em sequência.

A severidade inicial será **alta** quando os controles recusarem todas as tentativas e **crítica** se a análise confirmar que informações protegidas foram retornadas ou exportadas.

### 5.3 RD03 - Sobrecarga ou negação de serviço contra a aplicação

| Item | Definição |
| --- | --- |
| **Risco observado** | **R15 - Indisponibilidade da aplicação por Denial of Service**. |
| **Fonte dos dados/log** | Logs do API Gateway ou WAF, registros de rate limiting, métricas do Backend/API, códigos HTTP, latência, uso de CPU e memória e monitoramento de disponibilidade. |
| **Condição de alerta** | Gerar alerta quando uma mesma origem ou token ultrapassar **120 requisições por minuto durante 2 minutos consecutivos**. Para ataques distribuídos, gerar alerta quando o volume agregado permanecer acima de **3 vezes a média móvel dos 30 minutos anteriores durante 5 minutos** e, simultaneamente, a taxa de erros 5xx superar 10% ou a latência aumentar de forma anormal. |
| **Resposta inicial** | Aplicar ou reforçar rate limiting, bloquear temporariamente origens claramente maliciosas, ativar o mecanismo de mitigação de DDoS e ajustar a capacidade quando necessário. Preservar amostras dos registros e acompanhar erros e latência para confirmar a recuperação sem interromper usuários legítimos. |

A combinação entre volume, duração, erros e latência reduz falsos positivos provocados por horários de pico ou campanhas legítimas. A severidade será **alta** quando houver tentativa de sobrecarga sem impacto relevante e **crítica** quando a disponibilidade ou a conclusão de pedidos for afetada.

## 6. O que acontece após um alerta

Após a geração de um alerta, o grupo responsável pelo monitoramento deve seguir um fluxo de resposta consistente:

1. **Recebimento e correlação:** reunir os eventos relacionados pelo usuário, IP, sessão, recurso, horário e identificador de requisição.
2. **Triagem:** verificar se a condição da regra foi atendida, eliminar duplicidades e analisar a possibilidade de falso positivo.
3. **Classificação:** definir a severidade conforme o ativo afetado, o perfil envolvido, a quantidade de usuários atingidos e a existência de acesso ou dano confirmado.
4. **Contenção inicial:** executar a resposta prevista na regra, como limitar requisições, revogar sessão, bloquear origem ou restringir temporariamente uma operação.
5. **Preservação de evidências:** proteger logs, horários, identificadores e demais registros necessários para reconstruir o evento, evitando alterações no material original.
6. **Investigação:** determinar a origem, o alcance, as contas e os dados afetados, a vulnerabilidade explorada e a duração da atividade.
7. **Comunicação e escalonamento:** avisar infraestrutura, desenvolvimento, administração, responsável pela proteção de dados ou provedor externo conforme a natureza do incidente.
8. **Erradicação e recuperação:** corrigir a causa, remover acessos indevidos, restaurar o serviço ou os dados e acompanhar o ambiente até a normalização.
9. **Lições aprendidas:** registrar o incidente, avaliar a eficácia da resposta e ajustar controles, limites e regras de detecção.

Ações permanentes contra uma conta ou usuário não devem ser tomadas somente com base em um alerta automático. A confirmação humana e a análise do contexto reduzem o risco de bloquear usuários legítimos ou de interpretar uma falha operacional como ataque.

## 7. Responsabilidades e evidências

| Responsável | Atuação principal |
| --- | --- |
| **Infraestrutura/monitoramento** | Receber alertas, correlacionar métricas, conter sobrecarga e preservar registros técnicos. |
| **Desenvolvimento** | Analisar falhas da aplicação, corrigir vulnerabilidades e validar os controles de autenticação e autorização. |
| **Administração da plataforma** | Confirmar operações privilegiadas, apoiar o bloqueio de contas e decidir sobre a continuidade do serviço. |
| **Responsável pela proteção de dados** | Avaliar incidentes com possível exposição de informações pessoais e orientar as comunicações necessárias. |
| **Provedores externos** | Apoiar a investigação e recuperação quando pagamento, autenticação, nuvem ou outro serviço integrado estiver envolvido. |

Como evidência da Etapa 6, o repositório deverá manter este roteiro, o histórico de commits dos integrantes e a relação entre as regras RD01 a RD03 e os riscos R04, R11, R17, R19 e R15 já registrados nas etapas anteriores.

## 8. Considerações finais

A proposta combina registros de autenticação, autorização, acesso a dados, operações do delivery e disponibilidade para identificar comportamentos suspeitos. As três regras priorizam o comprometimento administrativo, o acesso indevido a informações e a negação de serviço, situações com impacto alto ou crítico para o sistema.

Os limites apresentados são valores iniciais para o roteiro acadêmico. Em um ambiente real, eles devem ser ajustados com base no volume normal de uso, nos horários de pico, nos falsos positivos observados e nas características da infraestrutura. A detecção somente será eficaz se os logs forem completos, protegidos, sincronizados e acompanhados por um processo definido de resposta.


