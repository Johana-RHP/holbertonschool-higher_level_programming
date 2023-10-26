// Realiza una solicitud para obtener el valor de "hello" desde la URL proporcionada
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json()) // Convierte la respuesta a JSON
  .then(data => {
    // Obtiene el valor de "hello" del objeto JSON recibido
    var helloValue = data.hello;

    // Actualiza el contenido del elemento con id "hello" con el valor obtenido
    document.getElementById('hello').textContent = helloValue;
  })
  .catch(error => {
    // Maneja errores si la solicitud no se puede completar
    console.error('Error:', error);
  });
