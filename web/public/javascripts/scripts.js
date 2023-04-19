let inputMessage = document.getElementById("input-message");
let messageBox = document.querySelector(".imessage");
let sendMessageButton = document.getElementById("send-message-button");

function scrollToBottom() {
    console.log(messageBox.scrollHeight - messageBox.clientHeight)
    messageBox.scrollTop = messageBox.scrollHeight - messageBox.clientHeight;
}

function clearMessage() {
    inputMessage.value = "";
    requestAnimationFrame(() => {
        inputMessage.selectionStart = 0;
        inputMessage.selectionEnd = 0;
    });
}

function createMessage(content, classType) {
    let newMessage = document.createElement("p");
    newMessage.setAttribute("class", classType);
    newMessage.innerText = content;
    messageBox.appendChild(newMessage);
}

function sendQuestion() {
    createMessage(inputMessage.value, "from-me");
    const temp = inputMessage.value;
    scrollToBottom();
    clearMessage();
    fetch("/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            content: temp
        })
    })
        .then(async (answer) => {
            createMessage(await answer.text(), "from-them");
            scrollToBottom();
        })
        .catch((err) => {
            createMessage(err, "from-them");
            scrollToBottom();
        })
}

inputMessage.addEventListener("keydown", (event) => {
    if (event.code === "Enter") {
        sendQuestion();
    }
});

sendMessageButton.addEventListener("click", () => {
    sendQuestion();
})
