import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django

django.setup()

from main.models import Stock, Product
from django.contrib.auth.models import User
from random import randint
from faker import Faker

import json

# import locale
# locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
IMGFOLDER = os.getcwd() + '/images/'


class BingImage(object):
    """docstring for BingImage"""
    BINGURL = 'http://www.bing.com/'
    JSONURL = 'HPImageArchive.aspx?format=js&idx=0&n=1&mkt=pt-BR'
    LASTIMG = None

    def __init__(self):
        super(BingImage, self).__init__()
        try:
            self.downloadimg()
        except:
            pass

    def getdailyimg(self):
        import json
        import urllib.request
        with urllib.request.urlopen(self.BINGURL + self.JSONURL) as response:
            rawjson = response.read().decode('utf-8')
            parsedjson = json.loads(rawjson)
            return self.BINGURL + parsedjson['images'][0]['url'][1:]

    def downloadimg(self):
        import datetime
        imgurl = self.getdailyimg();
        imgfilename = datetime.datetime.today().strftime('%Y%m%d') + '_' + imgurl.split('/')[-1]
        with open(IMGFOLDER + imgfilename, 'wb') as f:
            f.write(self.readimg(imgurl))
        self.LASTIMG = IMGFOLDER + imgfilename

    def checkfolder(self):
        d = os.path.dirname(IMGFOLDER)
        if not os.path.exists(d):
            os.makedirs(d)

    def readimg(self, url):
        import urllib.request
        with urllib.request.urlopen(url) as response:
            return response.read()


def get_random_item(model):
    count = model.objects.count()
    return model.objects.all()[randint(0, count - 1)]


def fillStock(N=1):
    locales = [
        'de_DE', ]
    faker = Faker(locales)

    for i in range(N):
        print("- - - - -")
        fake = faker['de-DE']

        product_obj = Product.objects.create(name=fake.company(),
                                             price=randint(100, 1500))
        stock_obj = Stock.objects.create(product=product_obj,
                                         quantity=randint(0, 1500))

        print("Created:", stock_obj)
        print("- - - - -")


def fillImages(N=1):
    for stock in Stock.objects.all():
        img = BingImage()
        stock.image = img.LASTIMG
        stock.save()

        print("Created:", stock.image.url)
        print("- - - - -")


if __name__ == '__main__':
    print("Filling data")
    # fillIl()
    fillStock(50)
    # fillImages()
    print("Filling done!")
