$(document).ready(function() {
    // Realiza una solicitud GET a la API para obtener la traducción de "hello" en francés
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Accede al valor de "hello" desde los datos recibidos
        var helloTranslation = data.hello;
        // Actualiza el contenido del elemento <div> con el identificador 'hello' con la traducción obtenida
        $('#hello').text(helloTranslation);
    });
});
