from collections import Counter
import re
import pytesseract
import cv2
import os
import imghdr
import xlsxwriter

# Link your directory
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.1.0/bin/tesseract'

def resizeIMG(path):
    img  = cv2.imread(path) 
    scale_percent = 220 # percent of original size

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImage

#text = pytesseract.image_to_string(blackAndWhiteImage)

def cleanText(text):
    text = text.lower()
    # any whitespace character (tab, space, newline)
    text = re.sub('\s+',' ', text)
    # anything that is not a word or a space
    text = re.sub("[^\w ]", "", text)
    # any number
    text = re.sub("[0-9]", "", text)
    return text


def find_ngrams(text, ngram):
    arr = []
    words = text.split(" ")
    if ngram == 1: return words
    for i in range(len(words) - ngram + 1):
            arr.append(' '.join(words[i:i+ngram]))
    return arr



uni = []
bi = []
tri = []
directory = 'pics'

for pic in os.listdir(directory):
    p = os.path.join(directory, pic)
    if imghdr.what(p) == 'jpeg' or imghdr.what(p) == 'jpg' or imghdr.what(p) == 'JPG':
        img = resizeIMG(p)
        recipe = pytesseract.image_to_string(img)
        recipe = cleanText(recipe)
        uni = uni + find_ngrams(recipe, 1)
        bi = bi + find_ngrams(recipe, 2)
        tri = tri + find_ngrams(recipe, 3)

## print(uni)
## print('\n')
## print(bi)
## print('\n')
## print(tri)
## print('\n')


uni = Counter(uni)
uni = dict(uni)
bi = Counter(bi)
bi = dict(bi)
tri = Counter(tri)
tri = dict(tri)


workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet('uni')

col = 0
row = 0

for key, value in uni.items():
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, value)
    row += 1

worksheet2 = workbook.add_worksheet('bi')

col = 0
row = 0

for key, value in bi.items():
    worksheet2.write(row, col, key)
    worksheet2.write(row, col + 1, value)
    row += 1

worksheet3 = workbook.add_worksheet('tri')

col = 0
row = 0

for key, value in tri.items():
    worksheet3.write(row, col, key)
    worksheet3.write(row, col + 1, value)
    row += 1

workbook.close()








