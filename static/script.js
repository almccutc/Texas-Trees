// Declare switchElement in a broader scope
var switchElement;

switchElement = document.getElementById("switch_wildflowers");
switchElement.checked = true;

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

// Declare plant_names, plant_image_urls, selectedIndex, and correctPlantIndex 
var plant_names;
var plant_image_urls;
var selectedIndex;
var correctPlantName;
var correctPlantIndex = 0; // Initialize correctPlantIndex with 0
var correctCount = 0; 
var totalCount = 0;
var switchState

// // Add an event listener to the checkbox
// switch_wildflowers.addEventListener("change", function() {
//   if (!this.checked) {
//       // The checkbox is now unchecked (false)
//       // Add your logic here
//       // console.log("Checkbox is unchecked");
//   }
// });

// Event listeners for the 4 buttons
for (let i = 0; i < 4; i++) {
  var myButton = document.querySelector(".button-stack button:nth-child(" + (i + 1) + ")");
  
  if (myButton) {
    myButton.addEventListener("click", function(index) {
      return function() {

        // Determine the index of the selected button
        var selectedIndex = index;

        // Call the checkSelectedAnswer function with the selected index and correct index
        checkSelectedAnswer(selectedIndex, correctPlantIndex);

        switchState = document.getElementById("switch_wildflowers").checked;
        
        // Fetch new plant names and update buttons for the next round
        fetchPlantNameList(selectedIndex, switchState);

        actionPerformed = true;
      };
    }(i));
  }
}

// Function to fetch plant names and update buttons and image
function fetchPlantNameList(selectedIndex, switchState) {
  console.log(switchState);
  fetch(`/get_plant_name_list?switchState=${switchState}`) 
    .then(response => response.json())
    .then(data => {
      plant_names = data.plant_names;
      plant_image_urls = data.plant_image_url;
      scientific_names = data.scientific_names;
      plant_types = data.plant_types;

      // Create an array of indices
      var indices = Array.from({ length: plant_names.length }, (_, index) => index);

      // Randomly select one index from the four
      var randomIndex = indices[Math.floor(Math.random() * 4)];

      // Update the buttons with new plant names
      for (var i = 0; i < 4; i++) {
        var myButton = document.querySelector(".button-stack button:nth-child(" + (i + 1) + ")");
        myButton.querySelector('.common-name').innerHTML = plant_names[indices[i]];
        myButton.querySelector('.scientific-name').innerHTML = scientific_names[indices[i]];
        myButton.querySelector('.tree-type').innerHTML = plant_types[indices[i]];

        // Unfocus the button
        setTimeout(function () {
          myButton.classList.remove('is-focused');
        }, 1000);
        
      }

      // Update the image with the corresponding URL
      var imageElement = document.getElementById("selectedPlantImage");
      imageElement.src = plant_image_urls[randomIndex];

      correctPlantIndex = indices.indexOf(randomIndex);
    });
}

// Function to determine if the selected answer was correct
function checkSelectedAnswer(selectedIndex, correctPlantIndex) {
  var selectedButton = document.querySelector(".button-stack button:nth-child(" + (selectedIndex + 1) + ")");
  totalCount = totalCount + 1; 
  
  if (selectedButton) {
    var isCorrect = selectedIndex === correctPlantIndex;

    // Set data-is-correct attribute based on correctness
    selectedButton.setAttribute("data-is-correct", isCorrect ? "true" : "false");

    // Add a class based on the data-is-correct attribute
    if (isCorrect) {
      selectedButton.classList.add("true");
      correctCount = correctCount + 1;
    } else {
      selectedButton.classList.add("false");
    }

    // Remove the class and set data-is-correct to "no-answer" after a 1-second timeout
    setTimeout(function () {
      selectedButton.classList.remove("true", "false");
      selectedButton.setAttribute("data-is-correct", "no-answer");
    }, 1000);
  }

  // Update the content of the result box
  updateResultBox();
}

function updateResultBox() {
  var resultBox = document.getElementById("counterBox");
  var resultTextSpan = document.getElementById("resultText");

  // Update the content of the result box
  resultTextSpan.textContent = "Correct: " + correctCount + "/" + totalCount;
}
