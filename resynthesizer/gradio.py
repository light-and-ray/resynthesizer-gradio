import gradio as gr
from .iframe import getIframe, onIframeLoadedJS


def getResynthesizerBlocks(isGradio3=False):
    with gr.Blocks(analytics_enabled=False) as blocks:
        gr.HTML(getIframe())
        if isGradio3:
            js_kwargs = {'_js': onIframeLoadedJS}
        else:
            js_kwargs = {'js': onIframeLoadedJS}
        blocks.load(fn=lambda: None, inputs=[], outputs=[], **js_kwargs)
    return blocks
