import os
from .tools import loadJsCallback, ROOT

doSendToResynthesizerJS = loadJsCallback(os.path.join(ROOT, 'resynthesizer', 'transfer.js'))
