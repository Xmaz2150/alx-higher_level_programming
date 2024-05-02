$(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.getJSON(url, function(data) {
      const ul = $('UL#list_movies');
      data.results.forEach(function(movie) {
        const li = $('<li></li>').text(movie.title);
        ul.append(li);
      });
    });
  });