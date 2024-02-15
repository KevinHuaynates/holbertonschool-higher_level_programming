$(document).ready(function() {
    // Realiza una solicitud GET a la API de Star Wars para obtener la lista de películas
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
        // Itera sobre los datos recibidos que contienen la información de las películas
        data.results.forEach(function(movie) {
            // Accede al título de la película
            var title = movie.title;
            // Crea un nuevo elemento <li> con el título de la película
            var listItem = $('<li>').text(title);
            // Agrega el elemento <li> al elemento <ul> con el identificador 'list_movies'
            $('#list_movies').append(listItem);
        });
    });
});
