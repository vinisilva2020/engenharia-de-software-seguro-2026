# Pipeline DevSecOps Proposto

O pipeline DevSecOps foi elaborado considerando o sistema de delivery desenvolvido ao longo do projeto, composto pelos módulos de cliente, empresa/restaurante, entregador, administração e integração com o serviço de pagamentos.

O objetivo do pipeline é garantir que uma nova alteração somente avance para implantação após passar pelas verificações de qualidade e segurança definidas para o projeto.

Os riscos prioritários identificados anteriormente orientam essas verificações, principalmente:

- **R04:** comprometimento de conta administrativa;
- **R11:** exposição de dados pessoais dos clientes;
- **R16:** indisponibilidade da API de pagamentos.

Esses riscos deram origem aos requisitos de segurança **RS01, RS02 e RS03** e às decisões arquiteturais **DA01, DA02 e DA03**, considerados durante as etapas do pipeline.

## Diagrama do Pipeline

O pipeline DevSecOps proposto segue o fluxo:

**Planejamento e análise de ameaças → Requisitos e arquitetura → Implementação segura → Testes automatizados → Testes de pagamento → Análise de código e dependências → Gate de segurança → Teste dinâmico com OWASP ZAP → Gate final → Implantação → Monitoramento e detecção → Resposta a incidentes → Feedback contínuo.**

Figura 1 — Pipeline DevSecOps proposto para o Sistema de Delivery
![Pipeline DevSecOps proposto para o Sistema de Delivery](diagramas/imagens/pipeline.png)

O fluxo possui pontos de controle, chamados de **gates de segurança**, responsáveis por impedir que uma versão avance quando alguma condição de segurança considerada obrigatória não for atendida.

No caso do serviço de pagamentos, os testes de integração devem considerar situações como indisponibilidade do gateway, timeout, repetição de requisições e prevenção de operações duplicadas, de acordo com o risco **R16**, o requisito **RS03** e a decisão arquitetural **DA03**.
