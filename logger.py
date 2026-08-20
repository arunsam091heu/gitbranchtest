# Logging configuration for FastAPI application
import logging
import sys
from datetime import datetime

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
    
    def get_logger(self):
        return self.logger

# Create logger instance
app_logger = Logger('FastAPI-App').get_logger()

def log_request(request_data: dict):
    """Log incoming requests"""
    app_logger.info(f"Request: {request_data}")

def log_response(response_data: dict):
    """Log outgoing responses"""
    app_logger.info(f"Response: {response_data}")
