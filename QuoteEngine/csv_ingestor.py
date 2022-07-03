# the respective imports
from .ingestor_interface import IngestorInterface
from .quotemodel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """
    This class uses pandas library to complete \
    defined, abstract method signatures to \
    parse CSV files.
    """

    allowed_exts = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse if it is a csv file."""
        if(cls.can_ingest(path)):
            # importing the data as a dataframe
            df = pd.read_csv(path)
            # iterating over the dataframe
            csv_quotes = []
            for index, row in df.iterrows():
                # selecting the respective body and author
                body = row['body']
                author = row['author']
                csv_quotes.append(QuoteModel(body, author))
            return csv_quotes
            # instantiate class

        else:
            raise Exception("could not handle this")
