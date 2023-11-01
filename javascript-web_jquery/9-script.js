$(document).ready(function() {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  const $helloDiv = $("#hello");

  $.get(url, function(data) {
    $helloDiv.text(data.hello);
  });
});

