const form = document.getElementById('prediction-form');
const predictionText = document.getElementById('prediction');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Simulate sending data to a server-side script (replace with actual logic)
  const data = {
    gender: document.getElementById('gender').value,
    age: parseFloat(document.getElementById('age').value),
    salary: parseFloat(document.getElementById('salary').value),
    price: parseFloat(document.getElementById('price').value),
  };

  // Replace with actual prediction logic using your trained model (loaded from server)
  const prediction = Math.random() > 0.5 ? "Likely to Purchase" : "Not Likely to Purchase";

  predictionText.textContent = `Prediction: ${prediction}`;
});
