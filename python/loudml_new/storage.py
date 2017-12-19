"""
Base interface for LoudML storage
"""

from abc import (
    ABCMeta,
    abstractmethod,
)

class Storage(metaclass=ABCMeta):
    """
    Abstract class for LoudML storage
    """

    @abstractmethod
    def get_model(self, name):
        """Get model"""

    @abstractmethod
    def create_model(self, model):
        """Create model"""

    @abstractmethod
    def delete_model(self, name):
        """Delete model"""

    @abstractmethod
    def set_threshold(self, name, threshold):
        """Set model threshold"""

    @abstractmethod
    def get_times_data(
        self,
        model,
        from_date=None,
        to_date=None,
    ):
        """Get numeric data"""

    @abstractmethod
    def save_model(self, model):
        """Save model"""