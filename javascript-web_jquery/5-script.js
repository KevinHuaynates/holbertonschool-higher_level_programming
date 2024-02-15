$(document).ready(function() {
    // Selecciona el elemento <div> con el identificador 'add_item' usando jQuery
    var $addItemDiv = $('#add_item');

    // Agrega un controlador de eventos 'click' al elemento <div> seleccionado
    $addItemDiv.click(function() {
        // Selecciona la lista <ul> con la clase 'my_list' y agrega un nuevo elemento <li>
        $('ul.my_list').append('<li>Item</li>');
    });
});
