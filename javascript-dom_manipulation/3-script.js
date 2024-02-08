// Selección del elemento con ID toggle_header
const toggleHeaderElement = document.getElementById('toggle_header');

// Función que se ejecuta cuando se hace clic en el elemento con ID toggle_header
function toggleHeaderClass() {
    // Selección del elemento de encabezado
    const headerElement = document.querySelector('header');

    // Si el elemento de encabezado tiene la clase 'red', cambiarla a 'green'; de lo contrario, cambiarla a 'red'
    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
}

// Agregar un evento de clic al elemento con ID toggle_header
toggleHeaderElement.addEventListener('click', toggleHeaderClass);
