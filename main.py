#!/bin/python3
import gradio as gr
from resynthesizer.getIframe import getIframe, onIframeLoadedJS


with gr.Blocks(title="Resynthesizer", analytics_enabled=False) as iface:
    with gr.Blocks(analytics_enabled=False) as blocks:
        html = gr.HTML(getIframe())
    blocks.load(fn=lambda: None, inputs=[], outputs=[], js=onIframeLoadedJS)

iface.launch(server_name="0.0.0.0")

