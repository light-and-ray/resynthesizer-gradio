import os
from .tools import ROOT, wrapJsCallback

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

with open("frame.html", "w") as frame_html:
    frame_html.write(getHTMLPage())

populateIframeJS = f'''
    const iframe = document.getElementById("resynthesizer_iframe");
    const timestamp = new Date().getTime();
    iframe.src = '/file={ROOT}/frame.html?' + timestamp;
    iframe.contentWindow.location.href = iframe.src;
'''

onIframeLoadedJS = wrapJsCallback(
f'   {populateIframeJS}'
'    console.log("resynthesizer_iframe loaded");'
'    return [...args];'
)

