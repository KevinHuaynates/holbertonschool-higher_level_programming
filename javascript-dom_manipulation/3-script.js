// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Select the tag with id toggle_header and header element
  const header = document.querySelector('header')
  const toggleHeader = document.getElementById('toggle_header')
  // Add a click event listener to the toggle_header id tag
  toggleHeader.addEventListener('click', () => {
    // Toggles the class 'red' and 'green' to the header element when the user clicks
    const greenClass = header.classList.contains('green')
    if (greenClass) {
      header.classList.replace('green', 'red')
    } else {
      header.classList.replace('red', 'green')
    }
  })
})
