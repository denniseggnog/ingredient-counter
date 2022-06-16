# ingredient-counter

INGREDIENT COUNTER SCRIPT

The goal of this project is to create a python script that can count
the occurrences of every ingredient in a cook book or collection of
recipes. 

There are two aspects of the project:
    1. Be able to analyze the text in pictures (because a readable pdf
    is not always available).
    2. Count all of the ingredients mentioned.

Project Description:

This project works by uploading images into the "pics" folder. After 
the upload, the project uses the cv2, pytesseract, collections, re, 
os, and imghdr libraries to:
    1. Check if the image is compatible.
    2. Resize and process the picture for readability.
    3. Use pytesseract to extract the text.
    4. Create a Counter with all of the unigrams, bigrams, and
    trigrams present in the text. 

After counting, the project creates an excel file with ingredients.

Installation:

You will need to have all of the libraries. Honestly, this is the first
README.md I have ever written, so I have no idea how to install the
program. Just clone my repo?

You will need to link the directory of your tesseract on line 9.

Future Goals:

    1. Handle the ingredient lists better. For example: remove plurality so
    "onion" and "onions" do not get counted separately and remove duplicates 
    across ngrams (i.e "mackerel" = "mackerel fillet")
    2. Create a .JSON file with the ingredients and their categorization.
    3. Provide more in-depth analysis and be able to handle cooking steps
    and processes to find patterns for recipe architecture.
    4. I hope I can find a faster way to process pictures.
