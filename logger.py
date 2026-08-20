# Logging configuration for FastAPI application
import logging
import sys
from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    """Enhanced logging levels with custom configuration"""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class Logger:
    """Refactored Logger with improved architecture and performance monitoring"""
    _instance = None
    
    def __new__(cls, name: str = 'FastAPI-App'):
        """Implement singleton pattern for logger"""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, name: str = 'FastAPI-App'):
        if self._initialized:
            return
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Console handler with enhanced formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        
        # Enhanced formatter with milliseconds and module tracking
        formatter = logging.Formatter(
            '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
        self._initialized = True
    
    def get_logger(self):
        """Get configured logger instance"""
        return self.logger

# Create logger instance
app_logger = Logger('FastAPI-App').get_logger()

def log_request(request_data: dict, user_id: str = None):
    """Log incoming requests with enhanced metadata"""
    metadata = f" [USER: {user_id}]" if user_id else ""
    app_logger.info(f"Request: {request_data}{metadata}")

def log_response(response_data: dict, status_code: int = 200):
    """Log outgoing responses with status tracking"""
    app_logger.info(f"Response: {response_data} [STATUS: {status_code}]")

def log_performance(operation: str, duration_ms: float):
    """Log performance metrics for operations"""
    app_logger.debug(f"Performance: {operation} completed in {duration_ms:.2f}ms")
