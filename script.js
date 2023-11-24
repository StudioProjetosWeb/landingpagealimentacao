document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('/', {
        method: 'POST',
        body: formData
    }).then(response => response.text())
      .then(data => {
          alert(data); // Exibe a mensagem de agradecimento
          window.location.href = 'https://studioprojetosweb.com.br'; // Redireciona para a URL
      });
});
