document.addEventListener("DOMContentLoaded", function() {
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const outputDiv = document.getElementById("output");

let recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.interimResults = false;
recognition.lang = 'en-US';

let transcript = "";

startBtn.addEventListener("click", function() {
    startBtn.disabled = true;
    stopBtn.disabled = false;

    outputDiv.innerHTML = "Listening...";
    outputDiv.innerHTML += "<br>"; // Add a line break

    recognition.start();
});

stopBtn.addEventListener("click", function() {
    startBtn.disabled = false;
    stopBtn.disabled = true;

    recognition.stop();
    outputDiv.innerHTML += "<br>Recording stopped.";
});

recognition.onresult = function(event) {
    transcript += event.results[0][0].transcript + " ";
    outputDiv.innerHTML = transcript;
};

recognition.onerror = function(event) {
    outputDiv.innerHTML += "<br>Error occurred while recording: " + event.error;
    recognition.stop();
};

recognition.onend = function() {
    outputDiv.innerHTML += "<br>Recorded: " + transcript;

    fetch('/save_transcript', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: transcript}),
    });

    transcript = ""; // Reset transcript for next recording
};
});
