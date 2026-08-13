# Configuração e Execução do ZAP

**Ferramenta:** OWASP ZAP (Zed Attack Proxy) versão 2.17.0.

**Modo de operação:** funcionalidade _Automated Scan_ (aba "Início Rápido"), que combina spidering (descoberta de URLs) e _Active Scan_ (varredura ativa) contra a aplicação, além da análise passiva sobre todo o tráfego capturado.

**Alvo:** aplicação rodando localmente em `http://127.0.0.1:8000`.

**Procedimento:**

1. Instalação do OWASP ZAP e abertura de uma nova sessão.
2. Na aba _Início Rápido_, uso do recurso _Automated Scan_, informando a URL alvo (`http://127.0.0.1:8000`) e a _Scan Policy_ padrão (`Default Policy`).
3. Habilitação do _traditional spider_ e do _modern spider_ (_Client Spider_, usando o navegador Firefox no modo "If Modern") para descoberta automática das URLs da aplicação.
4. Execução do ataque (_Attack_): o ZAP percorreu as páginas descobertas (incluindo recursos estáticos e endpoints de API, como `/api/v1/auth/register/clientes`) e realizou a varredura ativa sobre elas, gerando centenas de requisições (666 solicitações registradas durante a varredura).
5. Análise passiva automática do ZAP sobre todo o tráfego capturado, gerando os alertas da sessão.

**Resultado da sessão:** 8 alertas identificados ao todo. Deste conjunto, foram selecionados os 3 alertas descritos em A01, A02 e A03 para análise detalhada.

## A01 — Information Disclosure: Sensitive Information in URL

**Alerta:** _Information Disclosure - Sensitive Information in URL_

**Evidência:**

- Requisições GET capturadas com dados sensíveis diretamente na URL:
  - `GET http://127.0.0.1:8000/cadastro (email, name, password, ...)`
  - `GET http://127.0.0.1:8000/login (email, password)`
- Endereço de e-mail identificado pelo ZAP como evidência: `zaproxy@example.com`
- CWE ID: 598 · WASC ID: 13 · Fonte: Passivo (10024 - Information Disclosure - Sensitive Information in URL)

**Impacto potencial:**
Dados sensíveis (e-mail, senha, nome) trafegando na URL ficam expostos em vários pontos fora do controle da aplicação: histórico do navegador, logs de servidor/proxy/CDN, e o cabeçalho `Referer`, que pode vazar essas informações para sites de terceiros quando um link é clicado. Isso pode resultar em vazamento de credenciais e violação de políticas de conformidade (ex.: PCI-DSS), independentemente do uso de HTTPS.

**Relação com OWASP/CWE:**
CWE-598 (_Use of GET Request Method With Sensitive Query Strings_) está mapeado pela OWASP em **A02:2021 – Cryptographic Failures** (categoria que sucedeu a antiga A3:2017 – Sensitive Data Exposure), tratando da exposição indevida de dados sensíveis.

**Correção proposta:**
Enviar dados sensíveis (e-mail, senha, etc.) no corpo (_body_) da requisição via método POST, nunca como parâmetro de query string na URL, e manter HTTPS em todos os endpoints da aplicação.

# A02 — Missing Anti-clickjacking Header

**Alerta:** _Missing Anti-clickjacking Header_

**Evidência:**

- Requisições afetadas: `GET http://127.0.0.1:8000/`, `/cadastro`, `/cadastro (email, name, password...)`, `/login`
- CWE ID: 1021 · WASC ID: 15 · Fonte: Passivo (10020 - Anti-clickjacking Header)
- Descrição do ZAP: a resposta não protege contra ataques de _ClickJacking_; deveria incluir `Content-Security-Policy` com a diretiva `frame-ancestors` ou o cabeçalho `X-Frame-Options`.

**Impacto potencial:**
Sem esse cabeçalho, a aplicação pode ser embutida em um `<iframe>` dentro de um site malicioso controlado por um atacante. Isso viabiliza ataques de _clickjacking_, nos quais o usuário acredita estar interagindo com a página legítima, mas na verdade clica em elementos invisíveis sobrepostos — por exemplo, sendo induzido a submeter o formulário de login ou cadastro sem perceber.

**Relação com OWASP/CWE:**
CWE-1021 (_Improper Restriction of Rendered UI Layers or Frames_) está associado à categoria **A05:2021 – Security Misconfiguration** da OWASP.

**Correção proposta:**
Configurar o servidor/aplicação para enviar em todas as respostas o cabeçalho `X-Frame-Options: DENY` (ou `SAMEORIGIN`, caso o _framing_ interno seja necessário) e/ou `Content-Security-Policy: frame-ancestors 'none'`.
