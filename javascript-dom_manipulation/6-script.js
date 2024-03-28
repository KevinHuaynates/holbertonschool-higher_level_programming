// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // URL for the fetching character data
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
  const character = document.querySelector('#character')

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      character.textContent = data.name
    })
    .catch((error) => {
      console.log('Error fetching data from movie api:', error)
    })
})
