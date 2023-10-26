// Seleccione el elemento del botón usando document.getElementById
var toggleButton = document.getElementById('toggle_header');

// Seleccione el elemento del encabezado usando document.querySelector
var headerElement = document.querySelector('header');

// Agregue un event listener para manejar el clic en el botón
toggleButton.addEventListener('click', function() {
  // Verifique la clase actual del encabezado y alternarla
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});






