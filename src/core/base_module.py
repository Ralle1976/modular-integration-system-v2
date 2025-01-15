from abc import ABC, abstractmethod
import logging
from typing import Any, Dict

class BaseModule(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the module."""
        pass
        
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup resources."""
        pass
        
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the module is healthy."""
        pass

    def log_error(self, message: str, error: Exception) -> None:
        """Log error messages."""
        self.logger.error(f"{message}: {str(error)}")
        
    def log_info(self, message: str) -> None:
        """Log info messages."""
        self.logger.info(message)