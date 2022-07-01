from PIL import Image
from PIL.ImageDraw import Draw
from PIL import ImageFont
# import the Quote Engine
# from .QuoteEngine.quotemodel import QuoteModel 
from random import randint

class MemeEngine:
    """Does the Meme's Engine."""

    def __init__(self, output_dir):
        """Initialize the class and subclasses.

        """
        self.output_dir = output_dir

        # initializing inherited classes, from which
        # we can get some class parameters to be used.
#        super().__init__()

    def make_meme(self, image_path, text, author, width = 500) -> str:
        """ Resize img and add quotes.
        
        This class resizes the image according to a \
        maximum width of 500 px and scales the height \
        accordingly.
        
        It adds a quote body and a quote author to \
        the image, and saves it in the output \
        directory.
        
        This function returns the output directory. 
        """
        # load an image using Pillow
#        print('oi',image_path)
        img=Image.open(image_path)
        #resizes the image, so the width
        # is at most 500 px and the height
        # is scaled proportionally
        if width is not None:
            if(width > 500):
                width = 500
            else:
                pass

            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            # resizing the image
            img=img.resize((width,height),Image.NEAREST)
        # it adds a quote body and a
        # quote author to the image
        if(text is not None and author is not None):
 #           print('aaaaa',text,author)
            message = text + "-" + author
            print(message)
            draw = Draw(img)
            font = ImageFont.truetype('./fonts/DejaVuSans.ttf',size=20)
#            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10,20), message, fill='white',font=font)
        # it saves the manipulated image
        name="/image_quoted_{0}.png".format(randint(1,10000))
        img.save(self.output_dir+name)
        # the class must implement the instance method
        # signature, which returns the path to the
        # manipulated image:
        return self.output_dir+name
