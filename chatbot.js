// URL de l'API du chatbot Rasa
var chatbotUrl = 'http://localhost:5005/webhooks/rest/webhook';

// Fonction pour envoyer un message au chatbot et afficher la réponse
function sendMessageToChatbot(message) {
  // Requête POST vers l'API du chatbot avec le message en tant que corps de la requête
  fetch(chatbotUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: message
    })
  })
  .then(response => response.json())
  .then(data => {
    // Ajout de la réponse du chatbot à la liste des messages
    var chatMessages = document.getElementById('chat-messages');
    for (var i = 0; i < data.length; i++) {
      chatMessages.innerHTML += '<p><strong>DrBot :</strong> ' + data[i].text + '</p>';
    }
  })
  .catch(error => console.error(error));
}

// Récupération du champ de saisie de texte et du bouton d'envoi
var chatInput = document.getElementById('chat-input');
var chatSendButton = document.getElementById('chat-send-button');
var chatMessages1 = document.getElementById('chat-messages');
chatMessages1.innerHTML += '<p><strong>DrBot :</strong> Hi, I am Drbot </p>';

// Ajout d'un gestionnaire d'événement pour le bouton d'envoi
chatSendButton.addEventListener('click', function() {
  sendMessage();
});

// Ajout d'un gestionnaire d'événement pour la touche Entrée
chatInput.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    sendMessage();
  }
});

// Fonction pour envoyer un message
function sendMessage() {
  // Récupération du message saisi par l'utilisateur
  var message = chatInput.value;

  // Ajout du message à la liste des messages
  var chatMessages = document.getElementById('chat-messages');
  chatMessages.innerHTML += '<p><strong>Vous :</strong> ' + message + '</p>';

  // Effacement du champ de saisie de texte
  chatInput.value = '';

  // Envoi du message au chatbot
  sendMessageToChatbot(message);
}
