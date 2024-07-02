import os
from PIL import Image
from .tools import loadJsCallback, ROOT

def doSendToResynthesizer(image: Image.Image):
    image.save(os.path.join(ROOT, 'upload.ppm'))

doSendToResynthesizerJS = loadJsCallback(os.path.join(ROOT, 'resynthesizer', 'transfer.js'))
