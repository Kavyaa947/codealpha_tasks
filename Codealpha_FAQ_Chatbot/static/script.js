const chatBox = document.getElementById('chatBox');
const questionInput = document.getElementById('questionInput');
const sendButton = document.getElementById('sendButton');
const typingIndicator = document.getElementById('typingIndicator');

function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = message;

    messageDiv.appendChild(bubble);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping(show) {
    typingIndicator.style.display = show ? 'block' : 'none';
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const question = questionInput.value.trim();
    if (!question) {
        return;
    }

    addMessage(question, 'user');
    questionInput.value = '';
    showTyping(true);

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Something went wrong.');
        }

        addMessage(data.answer, 'bot');
    } catch (error) {
        addMessage(error.message || 'Unable to get a response right now.', 'bot');
    } finally {
        showTyping(false);
    }
}

sendButton.addEventListener('click', sendMessage);

questionInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
