$(document).ready(function() {
    // Selecciona el elemento <div> con el identificador 'red_header' usando jQuery
    var $redHeaderDiv = $('#red_header');

    // Agrega un controlador de eventos 'click' al elemento <div> seleccionado
    $redHeaderDiv.click(function() {
        // Selecciona el elemento <header> y añade la clase .red
        $('header').addClass('red');
    });
});
