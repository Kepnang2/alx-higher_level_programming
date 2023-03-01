$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
