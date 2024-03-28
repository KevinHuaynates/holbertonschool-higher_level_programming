// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // URL for the fetching data
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
  const hello = document.querySelector('#hello')

  fetch(url)
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello
    })
})
