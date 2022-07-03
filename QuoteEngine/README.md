# About the files of this folder


1. quotemodel.py

Encapsulates the body and author. 
It overrides the correct methods to instantiate the class and print the model content as "body text" - author

2. ingestor.py

It selects the appropriate helper for a given file, based on file type.

3. ingestor_interface.py

It defines the common functionalities, or rather methods, that need to be implemented by the interface classes. 
This part is rather architectural (at least the abstract method).

4. csv_ingestor.py

It uses pandas library to complete defined, abstract method signatures to parse CSV files.

5. pdf_ingestor.py

It uses xpdf to complete defined, abstract method signatures to parse CSV files.

6. docx_ingestor.py

It uses python-docx to complete defined, abstract method signatures to parse CSV files.


7. txt_ingestor.py

It uses python native libraries to complete defined, abstract method signatures to parse CSV files.


