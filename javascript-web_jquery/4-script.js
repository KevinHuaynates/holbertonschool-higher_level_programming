$(document).ready(function() {
    // Selecciona el elemento <div> con el identificador 'toggle_header' usando jQuery
    var $toggleHeaderDiv = $('#toggle_header');

    // Agrega un controlador de eventos 'click' al elemento <div> seleccionado
    $toggleHeaderDiv.click(function() {
        // Selecciona el elemento <header>
        var $headerElement = $('header');
        
        // Verifica si el elemento <header> tiene la clase 'red'
        if ($headerElement.hasClass('red')) {
            // Si tiene la clase 'red', cambia a 'green'
            $headerElement.removeClass('red').addClass('green');
        } else {
            // Si no tiene la clase 'red', cambia a 'red'
            $headerElement.removeClass('green').addClass('red');
        }
    });
});
