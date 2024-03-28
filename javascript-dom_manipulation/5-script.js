// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Select the tag with id update_header and header element
  const header = document.querySelector('header')
  const updateHeader = document.querySelector('#update_header')
  updateHeader.addEventListener('click', () => {
    // Updates the text of the header element to 'New Header!!!' when the user clicks
    header.textContent = 'New Header!!!'
  })
})
