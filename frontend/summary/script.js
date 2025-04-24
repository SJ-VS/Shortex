// script.js

document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const summaryText = document.getElementById('summaryText');
    const copyBtn = document.getElementById('copyBtn');
    const inputTextarea = document.querySelector('textarea');

    // Handle file upload
    fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        if (file && file.type === "text/plain") {
            const reader = new FileReader();
            reader.onload = function(e) {
                inputTextarea.value = e.target.result;
            };
            reader.readAsText(file);
        } else {
            alert("Please upload a valid .txt file.");
        }
    });

    // Dummy summarize action
    summarizeBtn.addEventListener('click', () => {
        const input = inputTextarea.value.trim();
        if (!input) {
            alert("Please enter some text to summarize.");
            return;
        }

        // Placeholder for real AI summary logic
        summaryText.textContent = "This is a placeholder summary. Once the AI is connected, the summary will appear here based on the input.";
    });

    // Copy summary to clipboard
    copyBtn.addEventListener('click', () => {
        const text = summaryText.textContent;
        navigator.clipboard.writeText(text).then(() => {
            copyBtn.textContent = "Copied!";
            setTimeout(() => {
                copyBtn.textContent = "Copy Summary";
            }, 1500);
        }).catch(err => {
            alert("Failed to copy text: " + err);
        });
    });
});
