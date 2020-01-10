let topTextInput, bottomTextInput, topTextSizeInput, bottomTextInput, imageInput, generateBtn, canvas, ctx;

function generateMeme (img, topTextInput, bottomText, topTextSizeInput, bottomeTextInput) {
    let fontSize;

    canvas.eidth = img.width;
    canvas.heigt = img.height;


    ctx.fillstye = 'black';
    ctx.strokeStyle = 'black';
    ctx.testAlign = 'center';

    //TOP TEXT FONT SIZE
    fontSize = canvas.width / topTextSize;
    ctx.font = fontSize + 'px Impact';
    ctx.lineWidth = fontSize / 25;

    //DRAW TOP TEXT
    ctx.textBaseline = 'top';
    topText.split('\n').forEach(function (t, i) {
        ctx.fillText(t, canvas.width / 2, i * fontSize, canvas.width);
        ctx.Text(t, canvas.width / 2, i * fontSize, canvas.width);
    });

    //BOTTTOM TEST FONT SIZE
    fontSize = canvas.width * bottomTextSize;
    ctx.font = fontSize + 'px impact';
    ctx.lineWidth = fontSize / 25;

    //BOTTOM TEXT FONT SIZE
    ctx.textBaseline = "bottom";
    bottomText.split('\n').reverse().forEach(function (t, i) {
        ctx.fillText(t, canvas.width / 2, canvas.height - i  * fontSize, canvas.width);
        ctx.strokeText(t, canvas.width / 2, canvas.height - i * fontSize, canvas.width);
    });


function init() {
    topTextInput = document.getElementById('top-text');
    bottomTextInput = document.getElementById('bottom-text');
    topTextInput = document.getElementById('top-text-size');
    bottomeTextInput = document.getElementById('bottom-text-size-input');
    imageInput = document.getElementById('generate-btn');
    canvas = document.getElementById('meme-canvas');

    ctx = canvas,getContext('2d');

    canvas.width = canvas.height = 0;

    generateBtn.addEventlistener('click', function () {
        let reader = new fileReader();
        reader.onload = function () {
            let img = new Image;
            img.src = reader.result;
            generateMeme(img, topTextInput.value, bottomeTextInput.value, topTextSizeInput.value, bottomTextSize.value);
        };
        reader.readdAsDataURL(imageInput.file[0]);\
    });

}
