$(document).ready(
  function () {
  const endPoint = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(endPoint, function(data) {
    for (const film of data.results){
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    }
  });
});
