import os
import gradio as gr
from .iframe import getIframe, onIframeLoadedJS
from .tools import ROOT
from .transfer import doSendToResynthesizerJS, doSendToResynthesizer


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
        blocks.load(fn=lambda: None, inputs=[], outputs=[], **load_kwargs)
    return blocks


def getIface(isSDWEBUI=False):
    with gr.Blocks(title="Resynthesizer", analytics_enabled=False, css="style.css") as iface:
        with gr.Row():
            with gr.Column(scale=2):
                uploadImage = gr.Image(label="Upload image", type="pil", sources=["upload"], elem_id="resynthesizer_upload")
                with gr.Row():
                    sendButton = gr.Button(value="Send to Resynthesizer")
                    getButton = gr.Button(value="Get Result")
                gr.Image(label="Result image", type="pil", interactive=False)
            with gr.Column(scale=4):
                getResynthesizerBlocks(isSDWEBUI)

        sendButton.click(fn=doSendToResynthesizer, inputs=[uploadImage], outputs=[]).then(fn=None, js=doSendToResynthesizerJS)
    return iface

