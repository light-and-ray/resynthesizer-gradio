
const img = document.getElementById('resynthesizer_upload').querySelector('img');

const idocument = document.getElementById('resynthesizer_iframe').contentWindow.document;
const canvas = idocument.getElementById('canvas');
const ctx = canvas.getContext('2d');

canvas.width = img.width;
canvas.height = img.height;

ctx.drawImage(img, 0, 0, img.width, img.height);
