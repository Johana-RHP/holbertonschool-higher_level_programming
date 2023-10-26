// Selecciona el elemento con id "update_header"
var updateHeaderElement = document.getElementById('update_header');

// Agrega un evento de clic al elemento con id "update_header"
updateHeaderElement.addEventListener('click', function() {
  // Selecciona el elemento del encabezado
  var headerElement = document.querySelector('header');
  
  // Actualiza el texto del encabezado a "New Header!!!"
  headerElement.textContent = 'New Header!!!';
});
