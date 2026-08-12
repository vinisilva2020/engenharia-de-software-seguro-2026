# A01 — Information Disclosure: Sensitive Information in URL

**Alerta:** *Information Disclosure - Sensitive Information in URL*

**Evidência:**
- Requisições GET capturadas com dados sensíveis diretamente na URL:
  - `GET http://127.0.0.1:8000/cadastro (email, name, password, ...)`
  - `GET http://127.0.0.1:8000/login (email, password)`
- Endereço de e-mail identificado pelo ZAP como evidência: `zaproxy@example.com`
- CWE ID: 598 · WASC ID: 13 · Fonte: Passivo (10024 - Information Disclosure - Sensitive Information in URL)

**Impacto potencial:**
Dados sensíveis (e-mail, senha, nome) trafegando na URL ficam expostos em vários pontos fora do controle da aplicação: histórico do navegador, logs de servidor/proxy/CDN, e o cabeçalho `Referer`, que pode vazar essas informações para sites de terceiros quando um link é clicado. Isso pode resultar em vazamento de credenciais e violação de políticas de conformidade (ex.: PCI-DSS), independentemente do uso de HTTPS.

**Relação com OWASP/CWE:**
CWE-598 (*Use of GET Request Method With Sensitive Query Strings*) está mapeado pela OWASP em **A02:2021 – Cryptographic Failures** (categoria que sucedeu a antiga A3:2017 – Sensitive Data Exposure), tratando da exposição indevida de dados sensíveis.

**Correção proposta:**
Enviar dados sensíveis (e-mail, senha, etc.) no corpo (*body*) da requisição via método POST, nunca como parâmetro de query string na URL, e manter HTTPS em todos os endpoints da aplicação.
