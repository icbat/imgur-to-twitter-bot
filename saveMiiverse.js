// Gets a array of URLs when run on the miiverse page
// Paste that array into saveurls.py to get local copies

var x = $('div.album-dialog > .dialog-inner > .window > .window-body > .img-wrapper > img');
var y = x.map((a, b) => {return b.src;});
y.each((a, b) => {
    window.open(b, '_blank');
});
