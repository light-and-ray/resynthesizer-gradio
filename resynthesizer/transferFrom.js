
const frame = document.getElementById('resynthesizer_iframe');
const idocument = frame.contentWindow.document;
const canvas = idocument.getElementById('canvas')
return canvas.toDataURL();
