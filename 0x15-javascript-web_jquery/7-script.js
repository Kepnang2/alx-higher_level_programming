$(document).ready(function () {
  endPoint = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(endPoint, function (data) {
    $('DIV#character').text(data.name);
  });
});
