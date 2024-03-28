// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Select the tag with id red_header and header element
  const header = document.querySelector('header')
  const redHeader = document.getElementById('red_header')
  // Add a click event listener to the red_header tag
  redHeader.addEventListener('click', () => {
    // Adds the class 'red' to the header element when the user clicks
    header.classList.add('red')
  })
})
