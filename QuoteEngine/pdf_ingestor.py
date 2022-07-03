# the respective imports
from .quotemodel import QuoteModel
from .ingestor_interface import IngestorInterface
import subprocess
from typing import List


class PDFIngestor(IngestorInterface):
    """
    This class utilizes the subprocess module \
    to call the pdftotext CLI utility -\
    creating a pipeline that converts PDFs\
    to text and the ingest the texts.
    Note: this class deletes temporary files.
    """

    allowed_exts = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if(cls.can_ingest(path)):
            # Use the subprocess module to read pdf
            txt = './temp/file_test.txt'
            # from Stack Overflow
            # https://stackoverflow.com/questions/45368593/
            # python-subprocess-call-to-xpdfs-pdftotext-not
            # -working-with-encoding
            cmd = r"""{} "{}" "{}" -enc UTF-8""".format('pdftotext', path, txt)
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
            # now it is the same procedure as we did
            # in the CSVIngestor class
            with open(txt, 'r') as file_txt:
                txt_quotes = []
                for line in file_txt.read().splitlines():  # .readlines():
                    if(line.split("-")[0] == ''):
                        break
                    print(line)
                    body = line.split("-")[0]
                    author = line.split("-")[1]
                    txt_quotes.append(QuoteModel(body, author))
                return txt_quotes
        else:
            raise Exception("could not handle this.")
