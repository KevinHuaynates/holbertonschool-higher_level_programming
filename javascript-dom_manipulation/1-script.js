// Selección del elemento con ID red_header
const redHeaderElement = document.getElementById('red_header');

// Función que se ejecuta cuando se hace clic en el elemento con ID red_header
function changeHeaderColor() {
    // Selección del elemento de encabezado
    const headerElement = document.querySelector('header');

    // Actualización del color de texto del elemento de encabezado a rojo
    headerElement.style.color = '#FF0000';
}

// Agregar un evento de clic al elemento con ID red_header
redHeaderElement.addEventListener('click', changeHeaderColor);
