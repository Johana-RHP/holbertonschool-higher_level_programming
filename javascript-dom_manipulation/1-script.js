// Obtén el elemento con id "red_header"
var redHeaderElement = document.getElementById('red_header');

// Agrega un event listener para el evento de clic
redHeaderElement.addEventListener('click', function() {
  // Selecciona el elemento del encabezado usando document.querySelector
  var headerElement = document.querySelector('header');

  // Actualiza el color del texto del encabezado a rojo (#FF0000)
  headerElement.style.color = '#FF0000';
});
