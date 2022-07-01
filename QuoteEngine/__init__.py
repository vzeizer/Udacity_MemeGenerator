# here goes the __init__ of the module
# import the modules to be used
# in order to create a package

from .quotemodel import QuoteModel

from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .docx_ingestor import DocxIngestor
from .txt_ingestor import TextIngestor

from .ingestor import Ingestor
from .ingestor_interface import IngestorInterface
