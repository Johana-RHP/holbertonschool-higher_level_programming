// Obtiene el elemento ul con id list_movies
const movieList = document.getElementById('list_movies');

// Hace una solicitud a la API utilizando fetch
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Convierte la respuesta a formato JSON
  .then(data => {
    // Itera a través de los resultados y agrega los títulos a la lista
    data.results.forEach(movie => {
      // Crea un elemento de lista <li>
      const listItem = document.createElement('li');
      // Establece el texto del elemento de lista al título de la película
      listItem.textContent = movie.title;
      // Agrega el elemento de lista a la lista de películas
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    // Maneja cualquier error que ocurra durante la solicitud
    console.error('Error fetching data:', error);
  });
