from pathlib import Path
from PIL import Image
import io
import base64

ROOT = str(Path(__file__).parent.parent.absolute())


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
    # Разделим строку data URI на части
    header, encoded_data = data_uri.split(',', 1)

    # Получим MIME тип изображения и кодировку (base64)
    mime_type = header.split(';')[0].split(':')[1]

    # Декодируем base64 данные
    decoded_data = base64.b64decode(encoded_data)

    # Создаем байтовый поток для чтения данных
    image_stream = io.BytesIO(decoded_data)

    # Открываем изображение с помощью PIL
    pil_image = Image.open(image_stream)

    return pil_image
