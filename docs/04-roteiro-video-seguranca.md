# Roteiro do Vídeo Final — Segurança do Sistema

O vídeo final apresentará a evolução do projeto de segurança do sistema de delivery.

## Sistema escolhido

Apresentar brevemente o sistema de delivery, composto por clientes, empresas/restaurantes, entregadores e administradores, além da integração com o serviço de pagamentos.

## Principais ameaças e casos de abuso

Apresentar as principais ameaças identificadas com o STRIDE:

- comprometimento de contas;
- alteração indevida de pedidos;
- acesso indevido ao painel administrativo;
- exposição de dados pessoais;
- problemas relacionados aos pagamentos.

## Riscos prioritários

- **R04:** comprometimento de conta administrativa;
- **R11:** exposição de dados pessoais dos clientes;
- **R16:** indisponibilidade da API de pagamentos.

Explicar que esses riscos foram priorizados considerando probabilidade e impacto.

## Decisões de arquitetura

Mostrar o diagrama de arquitetura segura e explicar suas decisões.

## Práticas de código seguro

Apresentar as práticas de código seguro desenvolvidas no projeto, destacando autenticação, autorização no servidor, RBAC e princípio do menor privilégio.

Mostrar brevemente a implementação e os testes realizados.
