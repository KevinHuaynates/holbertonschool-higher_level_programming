// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Select HTML elements
  const languageSelect = document.querySelector('#language_code')
  const translateBtn = document.querySelector('#btn_translate')
  const helloElement = document.querySelector('#hello')

  const fetchTranslation = () => {
    // Get the selected language code
    const languageCode = languageSelect.value
    // URL for the fetching data
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        helloElement.textContent = data.hello
      })
  }

  // Event listener for the translate button
  translateBtn.addEventListener('click', fetchTranslation)
})
