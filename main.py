#!/bin/python3
from resynthesizer.gradio import getIface
from resynthesizer.tools import ROOT


getIface().launch(server_name="0.0.0.0", allowed_paths=[ROOT])

