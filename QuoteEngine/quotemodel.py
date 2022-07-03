from typing import List
from abc import ABC, abstractmethod

# here goes the classes to be used in the
# Quote Engine.


class QuoteModel:
    """Quote model class.

    This class encapsulates the body \
    and author. This class overrides \
    the correct methods to instantiate \
    the class and print the model content \
    as "body text" - author
    """

    # initializing the class
    def __init__(self, body, author):
        """Init function of Quote Model."""
        self.body = body
        self.author = author

    def __str__(self):
        """Informal representation of QuoteModel."""
        return "{0}".format(self.author) + "-" + "{0}".format(self.body)

    def __repr__(self):
        """Formal representation of QuoteModel."""
        return "{0}".format(self.author) + "-" + "{0}".format(self.body)
