import logging
import os
from config.settings import LOGS_DIR, LOG_LEVEL, LOG_FORMAT

def get_logger(name):
    """Get or create a logger instance"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(LOG_LEVEL)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOG_LEVEL)
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        # File handler
        log_file = os.path.join(LOGS_DIR, f"{name}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger