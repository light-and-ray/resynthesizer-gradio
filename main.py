#!/bin/python3
import gradio as gr
from resynthesizer.gradio import getResynthesizerBlock


with gr.Blocks(title="Resynthesizer", analytics_enabled=False) as iface:
    getResynthesizerBlock()

iface.launch(server_name="0.0.0.0")

