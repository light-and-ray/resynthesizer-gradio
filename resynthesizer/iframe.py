import os
import urllib.parse
from .tools import ROOT

def getIframe():
    return (
        '<div class="iframe-container"> '
            '<iframe id="resynthesizer_iframe" width="560" height="315" frameborder="0">'
            '</iframe>'
        '</div>'
    )


def getHTMLPage():
    compiledDir = os.path.join(ROOT, 'resynthesizer_wasm_compiled')
    with (open(os.path.join(compiledDir, 'resynthesizer_no_js.html')) as html,
        open(os.path.join(compiledDir, 'script1.js')) as script1,
        open(os.path.join(compiledDir, 'script2.js')) as script2,
        open(os.path.join(compiledDir, 'style.css')) as style,
    ):
        html = html.read()
        html = html.format(style=style.read(), script1=script1.read(), script2=script2.read())
    return html


populateIframeJS = f'''
    const iframe = document.getElementById("resynthesizer_iframe");
    iframe.src = 'data:text/html;charset=utf-8,{urllib.parse.quote(getHTMLPage())}?';
    iframe.contentWindow.location.href = iframe.src;
'''

onIframeLoadedJS = ('(...args) => {'
f'   {populateIframeJS}'
'    console.log("resynthesizer_iframe loaded");'
'    return [...args];'
'}')

