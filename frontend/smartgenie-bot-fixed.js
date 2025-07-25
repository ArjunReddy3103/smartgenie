
// SmartGenie Chatbot Loader
(function() {
    const style = document.createElement('link');
    style.rel = 'stylesheet';
    style.href = 'https://funny-beijinho-d8d7ce.netlify.app/style.css';
    document.head.appendChild(style);

    const chatContainer = document.createElement('div');
    chatContainer.id = 'smartgenie-chat-container';
    document.body.appendChild(chatContainer);

    const audio = new Audio('https://funny-beijinho-d8d7ce.netlify.app/genie.mp3');

    function sendMessage(msg) {
        fetch("https://smartgenie-3e9t.onrender.com/ask_ai", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: msg, company_name: "SmartGenie" })
        })
        .then(res => res.json())
        .then(data => {
            audio.play();
            const reply = document.createElement('div');
            reply.className = 'sg-bot-reply';
            reply.innerHTML = `<img src="/lamp.png" class="sg-avatar" /> <span>${data.response}</span>`;
            chatContainer.appendChild(reply);
        })
        .catch(err => {
            console.error("Chatbot error:", err);
        });
    }

    // UI Toggle Button
    const toggleBtn = document.createElement('button');
    toggleBtn.innerText = "🤖";
    toggleBtn.id = "smartgenie-toggle";
    toggleBtn.onclick = function() {
        const input = prompt("Ask SmartGenie:");
        if (input) sendMessage(input);
    };
    document.body.appendChild(toggleBtn);
})();
