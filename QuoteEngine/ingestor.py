# the respective imports
from .txt_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .docx_ingestor import DocxIngestor
from .quotemodel import QuoteModel
from typing import List
from .ingestor_interface import IngestorInterface


class Ingestor(IngestorInterface):
    """ An ingestor for the file types.

    It selects the appropriate helper for a
    given file, based on file type.
    """
    # def __init__(self, path):
    #    super.__init__(path)

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Select the appropriate ingestor."""
        ingestors = [TextIngestor(), DocxIngestor(),
                     CSVIngestor(), PDFIngestor()]

        for ingestor in ingestors:
            if(ingestor.can_ingest(path)):
                return ingestor.parse(path)
