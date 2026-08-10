"""Configurações centrais da aplicação.

Os valores serão externalizados por variáveis de ambiente quando a API
receber autenticação e autorização reais.
"""


class Settings:
    """Configurações mínimas para a etapa de implementação."""

    app_name = "Delivery Seguro API"
    environment = "development"


settings = Settings()

