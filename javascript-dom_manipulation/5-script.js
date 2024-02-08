// Selección del elemento con ID update_header
const updateHeaderElement = document.getElementById('update_header');

// Función que se ejecuta cuando se hace clic en el elemento con ID update_header
function updateHeader() {
    // Selección del elemento de encabezado
    const headerElement = document.querySelector('header');
    
    // Actualización del texto del elemento de encabezado
    headerElement.textContent = 'New Header!!!';
}

// Agregar un evento de clic al elemento con ID update_header
updateHeaderElement.addEventListener('click', updateHeader);
