from pathlib import Path
from PIL import Image
import io
import base64

ROOT = str(Path(__file__).parent.parent.absolute()).replace('\\', '/')


def wrapJsCallback(code):
    func = ('(...args) => {'
    f'   {code}'
    '    return [...args];'
    '}')
    return func


def loadJsCallback(file):
    with open(file) as f:
        code = f.read()
    return wrapJsCallback(code)


def convert_data_uri_to_pil_image(data_uri):
    header, encoded_data = data_uri.split(',', 1)
    decoded_data = base64.b64decode(encoded_data)
    image_stream = io.BytesIO(decoded_data)
    pil_image = Image.open(image_stream)

    return pil_image
