$(document).ready(function() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  const $listMovies = $("#list_movies");

  $.get(url, function(data) {
    const films = data.results;
    for (const film of films) {
      const title = film.title;
      const listItem = $("<li></li>").text(title);
      $listMovies.append(listItem);
    }
  });
});

