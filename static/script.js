// Declare plant_names in a broader scope
var plant_names;

var switchElement = document.getElementById("switchRoundedDefault_wildflowers");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_grasses");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_aquaticplants");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_vines");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_herbs");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_poisonousplants");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_invasiveplants");
switchElement.checked = false;
var switchElement = document.getElementById("switchRoundedDefault_cacti");
switchElement.checked = false;

fetchPlantNameList();

function fetchPlantNameList() {
  fetch('/get_plant_name_list')
    .then(response => response.json())
    .then(data => {
      plant_names = data.plant_names;

      var url = data.image_url[0];
      // Now you can use the variableValue in your JavaScript code
      // console.log(Button_1_Value);
      // console.log(url);

      plant_names.sort(() => Math.random() - 0.5);

      // Now you have a new variable 'random_plant_names' with the randomized order
      var random_plant_names = plant_names;

      for (var i = 1; i <= 4; i++) {
        var myButton = document.getElementById("Button_" + i);
        myButton.innerHTML = random_plant_names[i - 1];
      }

      var imageElement = document.getElementById("Plant_Image");
      imageElement.src = url; // Set the image URL
    });
}

// Add event listeners to the buttons
for (var i = 1; i <= 4; i++) {
  var myButton = document.getElementById("Button_" + i);
  myButton.addEventListener("click", function() {
    var buttonValue = this.innerHTML;

    

    // Compare the button value with the desired value
    if (buttonValue === plant_names[0]) {
      // Call the fetchPlantNameList function
      fetchPlantNameList();

      console.log("It worked");
    }
  })
}
