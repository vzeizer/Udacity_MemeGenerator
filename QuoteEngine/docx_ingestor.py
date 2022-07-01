# the respective imports
from .ingestor_interface import IngestorInterface
from .quotemodel import QuoteModel
from typing import List
#import docx2txt
import docx

class DocxIngestor(IngestorInterface):
    """
    
    Abstract methods to parse DOCX files.
    
    """
    allowed_exts = ['docx']
    
    @classmethod
    def parse(cls,path: str) -> List[QuoteModel]:
        """
        """
        if not cls.can_ingest(path):
            raise Exception("could not handle this")

        #quote_body = []
        #quote_author = []
        quotes=[]
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if (para.text != ""):
                parse = para.text.split('-')
                body = parse[0]
                author = parse[1]
                quotes.append(QuoteModel(body,author))
                # Should I instantiate classes??
        print('docx',quotes)
        return quotes
