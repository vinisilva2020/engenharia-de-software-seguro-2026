# Configuração e Execução do ZAP

**Ferramenta:** OWASP ZAP (Zed Attack Proxy) versão 2.17.0.

**Modo de operação:** funcionalidade *Automated Scan* (aba "Início Rápido"), que combina spidering (descoberta de URLs) e *Active Scan* (varredura ativa) contra a aplicação, além da análise passiva sobre todo o tráfego capturado.

**Alvo:** aplicação rodando localmente em `http://127.0.0.1:8000`.

**Procedimento:**
1. Instalação do OWASP ZAP e abertura de uma nova sessão.
2. Na aba *Início Rápido*, uso do recurso *Automated Scan*, informando a URL alvo (`http://127.0.0.1:8000`) e a *Scan Policy* padrão (`Default Policy`).
3. Habilitação do *traditional spider* e do *modern spider* (*Client Spider*, usando o navegador Firefox no modo "If Modern") para descoberta automática das URLs da aplicação.
4. Execução do ataque (*Attack*): o ZAP percorreu as páginas descobertas (incluindo recursos estáticos e endpoints de API, como `/api/v1/auth/register/clientes`) e realizou a varredura ativa sobre elas, gerando centenas de requisições (666 solicitações registradas durante a varredura).
5. Análise passiva automática do ZAP sobre todo o tráfego capturado, gerando os alertas da sessão.

**Resultado da sessão:** 8 alertas identificados ao todo. Deste conjunto, foram selecionados os 3 alertas descritos em A01, A02 e A03 para análise detalhada.