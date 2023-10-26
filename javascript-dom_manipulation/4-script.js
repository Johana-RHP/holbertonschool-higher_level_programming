// Seleccionar el elemento con id 'add_item'
var addItemButton = document.getElementById('add_item');

// Agregar un evento de clic al elemento con id 'add_item'
addItemButton.addEventListener('click', function() {
  // Crear un nuevo elemento li
  var newListItem = document.createElement('li');
  
  // Establecer el texto del nuevo elemento li
  newListItem.textContent = 'Item';
  
  // Seleccionar el elemento ul con clase 'my_list'
  var myList = document.querySelector('.my_list');
  
  // Agregar el nuevo elemento li al elemento ul con clase 'my_list'
  myList.appendChild(newListItem);
});
