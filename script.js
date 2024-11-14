// Fetch crop prices from the Flask API and display them
function fetchCropPrices() {
    const cropName = document.getElementById("cropSearch").value;
    const pricesTable = document.getElementById("pricesTable");
  
    fetch('http://127.0.0.1:5000/api/prices')
      .then(response => response.json())
      .then(data => {
        // Filter data based on search input
        const filteredData = data.filter(item => item.crop.toLowerCase().includes(cropName.toLowerCase()));
  
        // Populate table
        pricesTable.innerHTML = `
          <table>
            <tr><th>Crop</th><th>Price</th><th>Location</th></tr>
            ${filteredData.map(item => `
              <tr><td>${item.crop}</td><td>${item.price}</td><td>${item.location}</td></tr>
            `).join('')}
          </table>
        `;
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        pricesTable.innerHTML = "<p>Unable to load crop prices.</p>";
      });
  }
  