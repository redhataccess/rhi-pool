from insights.configs.base import Settings
settings = Settings()

if not settings.configured:
    settings.configure()
