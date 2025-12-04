async function sendMessage() {
    const inputBox = document.getElementById('user-input');
    const message = inputBox.value;
    if (!message) return;
    
    // Show user message
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
    
    // Send request to chatbot API
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    });
    const data = await response.json();
    chatBox.innerHTML += `<p><b>CookMate AI:</b> ${JSON.stringify(data)}</p>`;
    
    inputBox.value = "";
}
