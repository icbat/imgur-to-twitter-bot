// This will delete the first image on your miiverse.
// Since you only have space for 100, you may want to spam this to clear up more room
//   ideally, after you've backed them up.
var buttons = $('input.js-album-delete-button').toArray();
i = 0;
buttons[i].click();
$('button.ok-button').click();
