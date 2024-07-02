#!/bin/python3
import gradio as gr
from resynthesizer.gradio import getResynthesizerBlocks
from resynthesizer.tools import ROOT


with gr.Blocks(title="Resynthesizer", analytics_enabled=False, css="style.css") as iface:
    getResynthesizerBlocks()

iface.launch(server_name="0.0.0.0", allowed_paths=[ROOT])

