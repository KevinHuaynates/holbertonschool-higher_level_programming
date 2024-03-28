// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // create variables for the li element and elements by class and id
  const liElement = '<li>Item</li>'
  const myList = document.querySelector('.my_list')
  const addItem = document.querySelector('#add_item')
  // Add a click event listener to the add_item id tag
  addItem.addEventListener('click', () => {
    // Adds the liElement to myList when the user clicks on addItem
    myList.insertAdjacentHTML('beforeend', liElement)
  })
})
