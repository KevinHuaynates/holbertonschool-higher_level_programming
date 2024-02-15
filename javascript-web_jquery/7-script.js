$(document).ready(function() {
    // Realiza una solicitud GET a la API de Star Wars
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
        // Accede al nombre del personaje desde los datos recibidos
        var characterName = data.name;
        // Actualiza el contenido del elemento <div> con el identificador 'character' con el nombre del personaje
        $('#character').text(characterName);
    });
});
