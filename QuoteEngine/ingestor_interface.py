# the respective imports
from typing import List
from abc import ABC, abstractmethod
from .quotemodel import QuoteModel

class IngestorInterface(ABC):
    """Abstract class that ingest and parse.
    
    This class defines the common functionalities, \
    or rather methods, that need to be implemented \
    by the interface classes. This part is rather \
    architectural (at least the abstract method).
    """

    #def __init__(self, path):
    #    self.path = path
    # all the possible file types
#    allowed_exts = ['csv','docx','pdf','txt']
    allowed_exts = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Decide whether can ingest the file.
        
        This class method verifies if the file type \
        is compatible with the ingestor class.
        """
    # taking the last element of the file path
    # which is the extension
        ext = path.split('.')[-1]
        return ext in cls.allowed_exts
        
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the files.
        
        This abstract method parses the file \
        content and outputs it to a "Quote" object.
        """
        pass
