// Declare switchElement in a broader scope
var switchElement;

switchElement = document.getElementById("switchRoundedDefault_wildflowers");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_grasses");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_aquaticplants");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_vines");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_herbs");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_poisonousplants");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_invasiveplants");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_cacti");
switchElement.checked = false;

// Declare plant_names and image_urls in a broader scope
var plant_names;
var plant_image_url;

// Fetch plant names and update buttons and image on page load
// fetchPlantNameList();

// Function to fetch plant names and update buttons and image
function fetchPlantNameList() {
  fetch('/get_plant_name_list')
    .then(response => response.json())
    .then(data => {
      plant_names = data.plant_names;
      plant_image_urls = data.plant_image_url;

      // Shuffle the plant names and get the first 4
      var random_plant_names = plant_names.sort(() => Math.random() - 0.5).slice(0, 4);

      // Randomly select one plant name from the four
      var selectedPlantName = random_plant_names[Math.floor(Math.random() * 4)];

      // Find the index of the selected plant name
      var index = plant_names.indexOf(selectedPlantName);
      console.log("index pn:", index);

      // Update the buttons with new plant names
      for (var i = 0; i < 4; i++) {
        var myButton = document.querySelector(".button-stack button:nth-child(" + (i + 1) + ")");
        myButton.innerHTML = random_plant_names[i];
      }

      // Update the image with the corresponding URL
      var imageElement = document.getElementById("selectedPlantImage");
      imageElement.src = plant_image_urls[index];
      
    });
}

// Add event listeners to the buttons
for (var i = 0; i < 4; i++) {
  var myButton = document.querySelector(".button-stack button:nth-child(" + (i + 1) + ")");
  
  if (myButton) {
    myButton.addEventListener("click", function() {
      // Get the clicked button value (plant name)
      var allButtons = document.querySelectorAll(".button-stack button");
      allButtons.forEach(button => {
        button.classList.remove("is-focused");
      });
      // var buttonValue = this.innerHTML;

      // // Log the buttonValue to the console
      // console.log("Button Value:", buttonValue);

      // // Find the corresponding URL based on the clicked button's index
      // var index = plant_names.indexOf(buttonValue);
      // var imageUrl = plant_image_url[index];

      // console.log("index", index);
      // console.log("imageUrl", imageUrl);

      // // Update the image with the new URL
      // var imageElement = document.getElementById("selectedPlantImage");
      // console.log("imageElement", imageElement);
      // imageElement.src = plant_image_url; //

      // Fetch new plant names and update buttons for the next round
      fetchPlantNameList();
    });
  }
  
}

