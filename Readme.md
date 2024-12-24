# Resynthesizer Gradio

Resynthesizer is a very old (2000 year) open-source equivalent to Adobe Photoshop's "Content-Aware Fill" feature

![](/images/animation.webp)

This gradio demo integrates compiled wasm build (i.e. client side) of [61315's standalone C implementation of resynthesizer](https://github.com/61315/resynthesizer) inside iframe and allows interactions with it

### How binary was build?:

read [build.md](build.md)

Todo:
- optimize for big resolution
- make changing of brush more responsible
- hide brush when mouse is out
- do not crop image
- fix result image css
