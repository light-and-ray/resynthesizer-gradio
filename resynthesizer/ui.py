import os
import gradio as gr
from .iframe import getIframe, onIframeLoadedJS
from .tools import ROOT
from .transfer import doSendToResynthesizerJS, doSendToResynthesizer, doGetFromResynthesizerJS, doGetFromResynthesizer


def removeUploadFile():
    file = os.path.join(ROOT, 'upload.ppm')
    if os.path.exists(file):
        os.unlink(file)


def getResynthesizerBlocks(isSDWEBUI):
    blocks_kwargs = {}
    if not isSDWEBUI:
        blocks_kwargs['css'] = os.path.join(ROOT, 'style.css')

    with gr.Blocks(analytics_enabled=False, **blocks_kwargs) as blocks:
        gr.HTML(getIframe(), elem_classes=["resynthesizer-html-component"])
        load_kwargs = {}
        if isSDWEBUI:
            load_kwargs['_js'] = onIframeLoadedJS
        else:
            load_kwargs['js'] = onIframeLoadedJS
        blocks.load(fn=removeUploadFile, inputs=[], outputs=[])\
                .then(fn=lambda: None, inputs=[], outputs=[], **load_kwargs)
    return blocks


def getIface(isSDWEBUI=False):
    with gr.Blocks(title="Resynthesizer", analytics_enabled=False, css="style.css") as iface:
        with gr.Row():
            with gr.Column(scale=2):
                uploadImage = gr.Image(label="Upload image", type="pil", sources=["upload"], height=300)
                with gr.Row():
                    sendButton = gr.Button(value="Send to Resynthesizer")
                    getButton = gr.Button(value="Get Result")
                resultImage = gr.Image(label="Result image", type="pil", interactive=False)
                gr.Markdown("To change brush size, use `[` and `]` keys after the first click")
            with gr.Column(scale=4):
                getResynthesizerBlocks(isSDWEBUI)

        dummy = gr.Textbox(visible=False)

        sendButton.click(fn=doSendToResynthesizer, inputs=[uploadImage], outputs=[]).then(fn=None, js=doSendToResynthesizerJS)
        getButton.click(fn=doGetFromResynthesizer, inputs=[dummy], outputs=[resultImage], js=doGetFromResynthesizerJS)
    return iface

