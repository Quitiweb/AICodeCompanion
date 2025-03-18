document.getElementById('generateForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const generateBtn = document.getElementById('generateBtn');
    const results = document.getElementById('results');
    const error = document.getElementById('error');

    // Reset UI
    error.classList.add('d-none');
    generateBtn.disabled = true;
    generateBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Generating...';

    try {
        const response = await fetch('/api/generate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({
                prompt: document.getElementById('prompt').value,
                filename: document.getElementById('filename').value
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to generate code');
        }

        // Display results
        results.classList.remove('d-none');
        document.getElementById('codeOutput').textContent = data.code;
        document.getElementById('testOutput').textContent = data.tests;

        // Format test results
        const testResults = document.getElementById('testResults');
        testResults.textContent = data.test_results.output;
        testResults.className = data.test_results.success ? 'text-success' : 'text-danger';

    } catch (err) {
        error.textContent = err.message;
        error.classList.remove('d-none');
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Code';
    }
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}