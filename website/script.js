document.addEventListener('DOMContentLoaded', function() {
    const translateButton = document.getElementById('translate_button');
    translateButton.addEventListener('click', function() {
        translate();
    });
});

function translate() {
    const text = document.getElementById('text').value;
    const targetLanguage = document.getElementById('target_language').value;

    fetch('http://localhost:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text, target_language: targetLanguage })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('translated_text').innerText = data.translated_text;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
