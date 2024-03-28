// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Function to add list item to the list
  const addItemToList = () => {
    const newListItem = '<li>Item</li>'
    const listItems = document.querySelector('.my_list')
    listItems.insertAdjacentHTML('beforeend', newListItem)
  }

  // Functio to remove list item from the list
  const removeItemToList = () => {
    const list = document.querySelector('.my_list')
    const lastListItem = list.lastElementChild
    if (lastListItem) {
      list.removeChild(lastListItem)
    }
  }

  // Function to clear all li elements from the list
  const clearItemList = () => {
    const list = document.querySelector('.my_list')
    list.innerHTML = ''
  }

  // Event listener for adding an item to the list
  const addItem = document.querySelector('#add_item')
  addItem.addEventListener('click', addItemToList)

  // Event listener for removing an item from the list
  const removeItem = document.querySelector('#remove_item')
  removeItem.addEventListener('click', removeItemToList)

  // Event listener for clearing the list
  const clearList = document.querySelector('#clear_list')
  clearList.addEventListener('click', clearItemList)
})
