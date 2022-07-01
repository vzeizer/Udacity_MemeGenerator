# the respective imports
from .ingestor_interface import IngestorInterface
from .quotemodel import QuoteModel
from typing import List

class TextIngestor(IngestorInterface):
    """Ingestor for text files.
    
    This class does not depend on 3rd party \
    libraries to complete the defined, abstract \
    method signature to parse text files.
    """
    
    # initializing the inherited class
    allowed_exts=['txt']
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if(cls.can_ingest(path)):
            # opening the file in read mode
            with open(path, 'r') as file_txt:
                txt_quotes = []
                for line in file_txt.readlines():
                    body = line.split("-")[0]
                    author = line.split("-")[1]
                    txt_quotes.append(QuoteModel(body,author))
                return txt_quotes
        else:
            raise Exception("unable to ingest file")
