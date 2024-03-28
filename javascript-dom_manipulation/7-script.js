// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // URL for the fetching movie data
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
  const listMovies = document.querySelector('#list_movies') // container for movies data

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const movies = data.results
      const titles = movies.map(movie => movie.title)

      // Display the movie titles in the list
      titles.forEach(title => {
        const listItem = document.createElement('li')
        listItem.textContent = title
        listMovies.appendChild(listItem)
      })
    })
    .catch(error => {
      console.log('Error fetching data from movie api:', error)
    })
})
