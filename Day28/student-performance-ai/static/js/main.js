document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const payload = {
        student_name: document.getElementById('student_name').value,
        prev_marks: parseFloat(document.getElementById('prev_marks').value),
        attendance: parseFloat(document.getElementById('attendance').value),
        assignment_score: parseFloat(document.getElementById('assignment_score').value),
        study_hours: parseFloat(document.getElementById('study_hours').value),
        participation: parseFloat(document.getElementById('participation').value)
    };

    const resultDisplay = document.getElementById('result-display');
    resultDisplay.innerHTML = "<p>Calculating AI prediction...</p>";

    try {
        const response = await fetch('/api/v1/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            const data = result.data;
            resultDisplay.innerHTML = `
                <div class="result-card">
                    <h3>Student: ${data.student_name}</h3>
                    <p><strong>Predicted Final Score:</strong> ${data.predicted_score}%</p>
                    <p><strong>Risk Classification:</strong> ${data.risk_level}</p>
                    <p><strong>Support Required:</strong> ${data.need_support ? 'Yes' : 'No'}</p>
                    <p><strong>Academic Action:</strong> ${data.recommendation}</p>
                </div>
            `;
        } else {
            resultDisplay.innerHTML = `<p style="color:red;">Error: ${result.error}</p>`;
        }
    } catch (err) {
        resultDisplay.innerHTML = `<p style="color:red;">Failed to connect to backend server.</p>`;
    }
});