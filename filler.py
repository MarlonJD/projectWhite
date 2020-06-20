import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django

django.setup()

from main.models import Stock, Product, Category
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


def fillProducts():
    products = [
        {
            "Isim": "Domates",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Türk-Patlican",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Patlican",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Salatalik",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Sivribiber",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Carli",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kirmizi Sivri Biber",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kirmizi Paprika",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Dolmalik Biber",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Eisberg",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Roka",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Maydanos",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kirmizi Turp-mini Radleschen",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Taze Sogan",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kirmizi Eisberg-Raditchio",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kabak",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Mantar",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kirmizi Kuru Sogan",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Beyaz Kuru Sogan",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Patates Festkochend",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Beyaz Lahana Weisskohl",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Rotkohl",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Taze Fasulye",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Lolo-Bionda",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "At Havucu",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Limon",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Portakal",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Üzüm",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kara Üzüm",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kivi",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Mango",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Avakado",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Karpuz",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Kavun",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Ananas",
            "Kategori": "Gemüse Obst"
        },
        {
            "Isim": "Eier L 360 St.",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Podravka Vegata 10kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pommes-Frites Würzsalz Fuchs 2 kg.",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pfeffer weis gemahlen 1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Knoblauch Granulat 1 Kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Edelsüss 1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Dillspitze gerebelt 1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Croissant Lunch Brd(82881)",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Spinat Blok",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Broccoli",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Edamer Block",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pommes Frisch 10mm",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Salatmayaonnaise Hormann 10kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Likrema feines Pflanzenfett",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Passierte Tomaten 12*1l",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Ananas geschnitten 12*850ml",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Tafelessig aus Brantwein",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Mehl Typ550 Gloria 25 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "H-Milch 3,5% 12*1L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Steinspeise Salz 25 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Thunfischstücke in Öl 6*1705g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Curry Sauce Wernsing 2kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Sahne 30% Ramli 12*1L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Deutsche Markenbutter 250g*40 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Nutella 120*15g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Port. Tom. Ketchup Gyma 120*20ml",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Port. Tom. Mayonnaise Gyma 120*20ml",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Honig 8*500g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Mondamin Roux Hell 10kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Zucker 10* 1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Mais 12*425g Dosen",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Hefe DHW Gewürfelt 24*42g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Sesarn 5kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Mozerella 1kg Packung",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Reis 25 Kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Barilla Tortiglioni No 83 5 Kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Eigelb Wiesenhof 1x1L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Barilla Penne No 83 5 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Irmik 1 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Tel Sehriyesi 20x500g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Arpa Sehriyesi 20x500g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pilavlik Bulgur 5kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Fasulye 5k",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Gouda Scheiben 6x1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Kaffeeportilionssahne turm 7,5%fett 240 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Karamellgebäck 300 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pizzasause 6x4250 Dosen",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Olivenöl 5L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Kekik",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Mevlana Tee 10x1000g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Oragano",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Sumak 1 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Chilies Geschrotten Ohne Kern 25kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Minze gerebelt Nane 1 KG",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Chilies Geschrotten mit Kern 25kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Chillies ganz 500g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Oliven Schwarz in Scheiben 6x4250g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Kreuzkümmel(Kimyon) 1kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Öncü tatli biber salcasi 4300g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Sele Zeytin(oliven)9kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Senf mittelscharf 12x1000g Tuben",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Danklorix 2x5L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Holzkohle 15kg Sommerhit",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Holzkohle Black Sellig 10kg",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Schaschliksplesse 20cm Bambus 1000 Stk",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Lunch-Box IP 9 weiß 1675 4x50 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Menüschale 603 Gr.a 3 fach geteilt 4x500 st",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Men bx 2f getlt. 1630 Chmpgnr. 2x100 st.",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Dönertüte 3200 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Hemdchentragetaschen_geblokt 300+180+550mm 20x100 st",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Hemdchentragetaschen_geblokt 280+140+480mmmm 20x100 st",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Müllsäcke 135L 10x15 Rollen",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Aliminiumfolie 30cm.100m 1200g",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Servietten Luxus 4000 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Aliminium Platten klein 100 stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Aliminium Platten mittel 60 stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Baklava Schale 100 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Dress box Verp.becher 125 ml 250 Bechr",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Geschirrspüllmittel 12x1L",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Glasreiniger 10x1L Flaschen",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Pizza Karton 31x31 100 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Aluschale R28l 100 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Aludeckel 28L 100 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Latex Handschuhe Ungepudert L 100",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Latex Handschuhe Ungepudert M 100",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Iso Teller 600 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Hamburger Box 6 Champagner 4x 125 St.",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Suppenbecher mit Deckel 11x40 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Backtrennpapier 40x60 500 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Esspressobecher 0,1L 100 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Kaffeebecher 8 OZ 0,2 20x50 Stück",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Edelstahl Topfreiniger 10 St.",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Zahnstocher 1000 Stück Packung",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Frischhaltefolie 4x30cm",
            "Kategori": "Frischdienst Lange GmbH"
        },
        {
            "Isim": "Dönerbox 26 OZ 20x50 St.",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "%70 Döner Drehspiess",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "%70 Döner Drehspiess",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "Hähnchen Döner",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "Kalbfleisch",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "Hänchenkeule ohne Knocken mit Haut",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "Kalbsfett",
            "Kategori": "Dönerci"
        },
        {
            "Isim": "Coca Cola Lig.Sle.Can 24x0,33l",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Bionade Holunder 24x0,33l",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola PET EWP 12x0,50l",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola PRT MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola Sleek C.DS 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola Zero DS 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca Cola Zero Pet WE 12x0,50L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola ZERO PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca-Cola Light PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Coca Cola Light PET WEP 12x0,50L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fanta DSP 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fanta Orange PET EWP 12x0,50L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fanta PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fuze Tea Pfirs. 12x0,4L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fuze Tea Pfirs. Hibiskus 12x0,4L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Fuze Tea Zitrone 12x0,4L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Klindw.Apfel Klar direkt 6x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Klindw. Bananen-Nektar 6x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Klindw. Orangensaft MW 6x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Lift Apfelschor. Pet WEP 12x0,5L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Lift Apfelschorle PET MW 12x1L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Mezzo Mix EWP 12x0,5L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Mezzo Mix Sle.Can DSP 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Mezzo Mix Orange PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Mineau Classic PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Schwepp Bitter Lemon PRT 6x1,0 L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Sprite DSP 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Sprite PET MW 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Uludag Gazoz DS-P 24x0,33L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Uludag GazozEWP 12x1,0L",
            "Kategori": "Salli Getraenke"
        },
        {
            "Isim": "Uludag Gazoz EWP 24x0,5L",
            "Kategori": "Salli Getraenke"
        }
    ]

    for product in products:
        isim = product['Isim']
        kategori = product['Kategori']

        print("Creating: ", isim, kategori)
        category_obj = Category.objects.get_or_create(name=kategori)[0]
        product_obj = Product.objects.get_or_create(name=isim,
                                                    category=category_obj)[0]
        Stock.objects.get_or_create(product=product_obj)
        print("Created: ", isim, kategori)


if __name__ == '__main__':
    print("Filling data")
    # fillIl()
    # fillStock(50)
    # fillImages()
    fillProducts()
    print("Filling done!")
