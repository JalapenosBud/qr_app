import qrcode
from django.db import models


class FileHandler(models.Model):
    text = models.FileField(max_length=100, upload_to='.')
    contents = []

    def __init__(self):
        pass

    @classmethod
    def savenewfile(cls, url):
        handle1 = open('file.txt', 'w')
        handle1.write(url)
        handle1.close()

    @classmethod
    def loadfile(cls):
        with open('file.txt','r') as fp:
            for line in fp:
                cls.contents.append(line)

    @classmethod
    def generateQR(cls, link_input):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link_input)
        qr.make(fit=True)
        #print(qr)
        img = qr.make_image(fill_color="black", back_color="white")
       #print(img)
        img.save("\\media\\firstqr.png")

