$(document).ready(function() {
  const $addItem = $("#add_item");
  const $myList = $(".my_list");

  $addItem.click(function() {
    const newItem = $("<li></li>").text("Item");
    $myList.append(newItem);
  });
});

