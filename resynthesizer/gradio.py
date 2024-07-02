import os
import gradio as gr
from .iframe import getIframe, onIframeLoadedJS
from .tools import ROOT


def getResynthesizerBlocks(isSDWEBUI=False):
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
