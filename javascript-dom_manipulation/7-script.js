// URL del servicio web para obtener la lista de películas de Star Wars
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Función para obtener y mostrar los títulos de las películas en el HTML
function getStarWarsMovies() {
    // Hacer una solicitud GET a la URL utilizando Fetch API
    fetch(apiUrl)
        .then(response => {
            // Verificar si la solicitud fue exitosa
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Convertir la respuesta a formato JSON
            return response.json();
        })
        .then(data => {
            // Obtener la lista de películas del objeto de datos
            const movies = data.results;
            // Seleccionar el elemento HTML con el ID 'list_movies'
            const listMoviesElement = document.getElementById('list_movies');
            // Recorrer la lista de películas y agregar cada título a la lista HTML
            movies.forEach(movie => {
                const movieTitle = document.createElement('li');
                movieTitle.textContent = movie.title;
                listMoviesElement.appendChild(movieTitle);
            });
        })
        .catch(error => {
            // Manejar errores de la solicitud
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Llamar a la función para obtener y mostrar los títulos de las películas cuando se carga la página
window.onload = getStarWarsMovies;
