// Realizar una solicitud a la API utilizando Fetch
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Verificar si la solicitud fue exitosa (código de estado 200)
    if (response.ok) {
      // Parsear la respuesta JSON
      return response.json();
    }
    // En caso de error, lanzar una excepción
    throw new Error('Network response was not ok.');
  })
  .then(data => {
    // Obtener el nombre del personaje desde los datos obtenidos
    const characterName = data.name;

    // Seleccionar la etiqueta con id "character" y mostrar el nombre del personaje
    const characterElement = document.getElementById('character');
    characterElement.textContent = `Character Name: ${characterName}`;
  })
  .catch(error => {
    // Capturar y manejar errores de la solicitud
    console.error('There has been a problem with your fetch operation:', error);
  });
