# Configuration module for enhanced project architecture
import os
from enum import Enum
from typing import Optional

class Environment(Enum):
    """Application environment configurations"""
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

class Config:
    """Base configuration class with environment-based settings"""
    
    # Application settings
    APP_NAME = "FastAPI Application"
    APP_VERSION = "2.0.0"
    DEBUG = False
    
    # Database settings
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    DATABASE_ECHO = False
    
    # Logging settings
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    # API settings
    API_PREFIX = "/api/v2"
    ALLOW_ORIGINS = ["*"]
    ALLOW_METHODS = ["*"]
    ALLOW_HEADERS = ["*"]

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    DATABASE_ECHO = True

class TestingConfig(Config):
    """Testing environment configuration"""
    DEBUG = True
    DATABASE_URL = "sqlite:///:memory:"
    LOG_LEVEL = "DEBUG"

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    LOG_LEVEL = "WARNING"
    ALLOW_ORIGINS = os.getenv("ALLOWED_ORIGINS", "https://example.com").split(",")

def get_config(env: str = None) -> Config:
    """Get configuration object based on environment"""
    if env is None:
        env = os.getenv("ENV", "development")
    
    config_mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    
    return config_mapping.get(env.lower(), DevelopmentConfig)()

# Export default configuration
config = get_config()
