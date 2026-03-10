class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Add other configurations specific to development

class ProductionConfig(Config):
    # Add production-specific configurations
    pass