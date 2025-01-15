from abc import ABC, abstractmethod
import logging
from typing import Any, Dict

class BaseModule(ABC):
    """Base class for all system modules."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize module resources."""
        pass
        
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup module resources."""
        pass
        
    @abstractmethod
    async def health_check(self) -> bool:
        """Check module health status."""
        pass

    def log_error(self, message: str, error: Exception) -> None:
        """Log error with details."""
        self.logger.error(f"{message}: {str(error)}")
        
    def log_info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)