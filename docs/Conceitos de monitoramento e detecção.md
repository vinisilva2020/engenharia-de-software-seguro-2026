# Etapa 6 - Monitoramento e Detecção de Intrusões

## 1. Objetivo e escopo

Esta etapa apresenta uma proposta de monitoramento e detecção para o sistema de delivery analisado pelo grupo. O objetivo é definir quais atividades relevantes devem ser registradas, como os registros podem revelar comportamentos suspeitos e quais ações iniciais devem ocorrer quando um alerta for gerado.

A proposta é conceitual e não exige a implementação de um IDS. Ela utiliza como base os usuários, ativos, pontos de interação, ameaças STRIDE e riscos já identificados nas etapas anteriores, especialmente os riscos relacionados ao comprometimento de contas, à exposição de dados, à elevação de privilégios e à indisponibilidade da aplicação.

## 2. O que é detecção de intrusões

Detecção de intrusões é o processo de observar eventos produzidos por aplicações, APIs, serviços, bancos de dados e componentes de infraestrutura para identificar tentativas de ataque, violações de políticas ou comportamentos incompatíveis com o uso esperado do sistema.

No sistema de delivery, a detecção pode revelar, por exemplo, repetidas tentativas de acesso a uma conta administrativa, consultas indevidas a dados de clientes ou um volume anormal de requisições capaz de degradar a aplicação. Para isso, os registros de diferentes fontes devem ser centralizados, correlacionados e analisados por regras com condições objetivas de alerta.

Um alerta representa um indício que precisa ser validado. Ele não comprova automaticamente que ocorreu um incidente, pois também pode ter sido provocado por erro de configuração, falha operacional ou uso legítimo fora do padrão.

## 3. Diferença entre prevenir e detectar

| Aspecto | Prevenção | Detecção |
| --- | --- | --- |
| **Objetivo** | Impedir ou dificultar que uma ameaça seja concretizada. | Identificar rapidamente uma tentativa, violação ou incidente em andamento ou já ocorrido. |
| **Momento de atuação** | Antes ou durante a tentativa de ataque. | Durante ou depois do evento suspeito. |
| **Exemplos no delivery** | MFA, RBAC, menor privilégio, validação no servidor, rate limiting e criptografia. | Análise de falhas de login, acessos negados, consultas anormais a dados, erros da API e picos de tráfego. |
| **Resultado esperado** | Reduzir a probabilidade de sucesso do ataque. | Diminuir o tempo de descoberta, apoiar a contenção e preservar evidências para investigação. |

Prevenção e detecção são complementares. Mesmo controles preventivos bem configurados podem ser contornados, apresentar falhas ou não cobrir todas as situações. Por esse motivo, os mesmos componentes que aplicam controles de segurança também devem produzir registros suficientes para demonstrar o que ocorreu e permitir uma resposta rápida.

