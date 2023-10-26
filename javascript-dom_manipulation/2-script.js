// Seleccione el elemento con el id red_header
var redHeaderElement = document.getElementById('red_header');

// Agregue un evento de clic al elemento con id red_header
redHeaderElement.addEventListener('click', function() {
  // Seleccione el elemento del encabezado usando document.querySelector
  var headerElement = document.querySelector('header');
  
  // Agregue la clase 'red' al elemento del encabezado
  headerElement.classList.add('red');
});
