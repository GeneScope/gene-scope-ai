async function predictAI() {
    const input = document.getElementById('aiInput').value;
    const resultElement = document.getElementById('aiResult');

    if (!input) {
        resultElement.innerText = "Please provide an input.";
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: parseFloat(input) })
        });
        const data = await response.json();
        resultElement.innerText = `Prediction: ${data.prediction}`;
    } catch (error) {
        resultElement.innerText = "Error: " + error.message;
    }
}

async function traceBlockchain() {
    const input = document.getElementById('blockchainInput').value;
    const resultElement = document.getElementById('blockchainResult');

    if (!input) {
        resultElement.innerText = "Please provide data.";
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/trace', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: input })
        });
        const data = await response.json();
        resultElement.innerText = `Blockchain Hash: ${data.block_hash}`;
    } catch (error) {
        resultElement.innerText = "Error: " + error.message;
    }
}
