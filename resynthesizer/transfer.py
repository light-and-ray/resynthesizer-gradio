import os
from PIL import Image
import gradio as gr
from .tools import loadJsCallback, ROOT, convert_data_uri_to_pil_image

def doSendToResynthesizer(image: Image.Image):
    if not image:
        raise gr.Error("Image wasn't provided")
    image.save(os.path.join(ROOT, 'upload.ppm'))

doSendToResynthesizerJS = loadJsCallback(os.path.join(ROOT, 'resynthesizer', 'transferTo.js'))


def doGetFromResynthesizer(image):
    return convert_data_uri_to_pil_image(image)

doGetFromResynthesizerJS = loadJsCallback(os.path.join(ROOT, 'resynthesizer', 'transferFrom.js'))
