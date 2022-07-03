import random
from random import randint
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote in quote_files:
        ings = Ingestor.parse(quote)
#        print('ings',ings.body)
        for ing in ings:
            quotes.append([ing.body, ing.author])

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    # From Stackoverflow
    # https://stackoverflow.com/questions/8625991/
    # use-python-os-walk-to-identify-a-list-of-files
    for root, dirnames, filenames in os.walk(images_path):
        for filename in filenames:
            imgs.append(images_path + filename)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
#    print(quote,'lllll')
    path = meme.make_meme(img, quote[0], quote[1])
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    img = request.form.get('image_url')

    try:
        req = requests.get(img, allow_redirects=True)
    except Exception as ex:
        raise Exception('not a vaild url!')

    # temporary file
    temp = './static/temp_{0}.png'.format(randint(0, 10000))

    with open(temp, 'wb') as temp_file:
        temp_file.write(req.content)

    body = request.form['body']
    author = request.form['author']

    try:
        path = meme.make_meme(temp, body, author)
    except Exception as ex:
        raise Exception('not a valid image url')

    os.remove(temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
