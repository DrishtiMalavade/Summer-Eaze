let darkMode = false;

function toggleDarkMode() {
    const body = document.body;
    const container = document.querySelector('.container');
    const title = document.querySelector('.title');
    const input = document.querySelector('input[type="text"]');
    const button = document.querySelector('button');
    const summaryDiv = document.getElementById('summary-text');
    
    darkMode = !darkMode;

    if (darkMode) {
        body.style.backgroundColor = '#121212';
        container.style.backgroundColor = '#121212';
        container.style.color = '#ffffff';
        title.style.color = '#ffffff';
        input.style.backgroundColor = '#121212';
        input.style.color = '#ffffff';
        button.style.backgroundColor = '#333333';
        button.style.color = '#ffffff';
        summaryDiv.style.backgroundColor = '#121212';
        summaryDiv.style.color = '#ffffff';
    } else {
        body.style.backgroundColor = '#ffffff';
        container.style.backgroundColor = '#ffffff';
        container.style.color = '#000000';
        title.style.color = '#000000';
        input.style.backgroundColor = '#ffffff';
        input.style.color = '#000000';
        button.style.backgroundColor = 'red';
        button.style.color = '#ffffff';
        summaryDiv.style.backgroundColor = '#ffffff';
        summaryDiv.style.color = '#000000';
    }
}

function getSummary() {
    const youtubeLink = document.getElementById('youtubeLink').value;
    const videoId = youtubeLink.split("=")[1];
    const videoThumbnail = document.getElementById('videoThumbnail');
    const summaryDiv = document.getElementById('summary-text');

    videoThumbnail.src = `http://img.youtube.com/vi/${videoId}/0.jpg`;

    fetch(`/get_summary?youtube_link=${youtubeLink}`)
        .then(response => response.json())
        .then(data => {
            summaryDiv.innerHTML = data.summary;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
