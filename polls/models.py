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

