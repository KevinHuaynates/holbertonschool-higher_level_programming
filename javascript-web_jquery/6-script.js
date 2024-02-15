$(document).ready(function() {
    // Selecciona el elemento <div> con el identificador 'update_header' usando jQuery
    var $updateHeaderDiv = $('#update_header');

    // Agrega un controlador de eventos 'click' al elemento <div> seleccionado
    $updateHeaderDiv.click(function() {
        // Selecciona el elemento <header> y actualiza su texto
        $('header').text('New Header!!!');
    });
});
