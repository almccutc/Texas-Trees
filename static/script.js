// Declare switchElement in a broader scope
var switchElement;

switchElement = document.getElementById("switchRoundedDefault_trees");
switchElement.checked = true;

switchElement = document.getElementById("switchRoundedDefault_leaves");
switchElement.checked = true;

switchElement = document.getElementById("switchRoundedDefault_barks");
switchElement.checked = false;

switchElement = document.getElementById("switch_wildflowers");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_grasses");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_aquaticplants");
switchElement.checked = false;

switchElement = document.getElementById("switchRoundedDefault_vines");
switchElement.checked = false;

// switchElement = document.getElementById("switchRoundedDefault_herbs");
// switchElement.checked = false;

// switchElement = document.getElementById("switchRoundedDefault_poisonousplants");
// switchElement.checked = false;

// switchElement = document.getElementById("switchRoundedDefault_invasiveplants");
// switchElement.checked = false;

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
var switchState_trees
var switchState_leaves
var switchState_barks
var switchState_wildflowers
var switchState_grasses
var switchState_aquaticplants
var switchState_vines
// var switchState_herbs
var switchState_cacti
var correctCheck = "true";
var previousPlantName = "plant";

// Add event listener to the tree switch
document.getElementById("switchRoundedDefault_trees").addEventListener('change', function() {
  // If the tree switch is unchecked, uncheck the bark and leaf switches
  if (!this.checked) {
      document.getElementById("switchRoundedDefault_leaves").checked = false;
      // document.getElementById("switchRoundedDefault_barks").checked = false;
  } else {
      // If the tree switch is checked again, check the bark and leaf switches
      document.getElementById("switchRoundedDefault_leaves").checked = true;
      // document.getElementById("switchRoundedDefault_barks").checked = true;
  }
});

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

        switchState_trees = document.getElementById("switchRoundedDefault_trees").checked;
        switchState_leaves = document.getElementById("switchRoundedDefault_leaves").checked;
        switchState_barks = document.getElementById("switchRoundedDefault_barks").checked;
        switchState_wildflowers = document.getElementById("switch_wildflowers").checked;
        switchState_grasses = document.getElementById("switchRoundedDefault_grasses").checked;
        switchState_aquaticplants = document.getElementById("switchRoundedDefault_aquaticplants").checked;
        switchState_vines = document.getElementById("switchRoundedDefault_vines").checked;
        // switchState_herbs = document.getElementById("switchRoundedDefault_herbs").checked;
        switchState_cacti = document.getElementById("switchRoundedDefault_cacti").checked;
        
        if (correctCheck == "true") {
          // Fetch new plant names and update buttons for the next round
        fetchPlantNameList(selectedIndex, switchState_trees, switchState_wildflowers, switchState_grasses, switchState_aquaticplants, switchState_vines, switchState_cacti, previousPlantName);
        } else {
          // Show the Next Button again 
          document.getElementById("quizNextButton").style.display = 'block';
        }
      };
    }(i));
  }
}

// Adds an event listener for the Next Image button
document.getElementById("quizNextButton").addEventListener('click', function() {
    // Fetch new plant names and update buttons for the next round
  fetchPlantNameList(selectedIndex, switchState_trees, switchState_leaves, switchState_barks, switchState_wildflowers, switchState_grasses, switchState_aquaticplants, switchState_vines, switchState_cacti, previousPlantName);

  // Hide the Next Button
  setTimeout(function() {
    document.getElementById("quizNextButton").style.display = 'none';
    totalCount = totalCount + 1;
    }, 2000);
});
  

// Function to fetch plant names and update buttons and image
function fetchPlantNameList(selectedIndex, switchState_trees, switchState_wildflowers, switchState_grasses, switchState_aquaticplants, switchState_vines, switchState_cacti) {
  // Randomly select one index from the four
  randomIndex = Math.floor(Math.random() * 4);
  fetch(`/get_plant_name_list?switchState_trees=${switchState_trees}&switchState_wildflowers=${switchState_wildflowers}&switchState_grasses=${switchState_grasses}&switchState_aquaticplants=${switchState_aquaticplants}&switchState_vines=${switchState_vines}&switchState_cacti=${switchState_cacti}&previousPlantName=${previousPlantName}`)
    .then(response => response.json())
    .then(data => {
      plant_names = data.plant_names;
      plant_image_urls = data.plant_image_url;
      scientific_names = data.scientific_names;
      plant_types = data.plant_types;
      source = data.source;

      // Create an array of indices
      var indices = Array.from({ length: plant_names.length }, (_, index) => index);

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

      var textElement = document.getElementById("modal-text");
      textElement.textContent = source[randomIndex];

      correctPlantIndex = indices.indexOf(randomIndex);

      previousPlantName = plant_names[randomIndex];

      collapseBox();
      
    });
}

// Function to determine if the selected answer was correct
function checkSelectedAnswer(selectedIndex, correctPlantIndex) {
  var selectedButton = document.querySelector(".button-stack button:nth-child(" + (selectedIndex + 1) + ")");
  if (correctCheck == "true") {
    totalCount = totalCount + 1;
  } else {
    }
   
  if (selectedButton) {
    var isCorrect = selectedIndex === correctPlantIndex;

    // Set data-is-correct attribute based on correctness
    selectedButton.setAttribute("data-is-correct", isCorrect ? "true" : "false");

    // Add a class based on the data-is-correct attribute
    if (isCorrect) {
      selectedButton.classList.add("true");
      correctCount = correctCount + 1;
      correctCheck = "true"
    } else {
      selectedButton.classList.add("false");
      correctCheck = "false"
    }

    // Remove the class and set data-is-correct to "no-answer" after a 1-second timeout
    setTimeout(function () {
      selectedButton.classList.remove("true", "false");
      selectedButton.setAttribute("data-is-correct", "no-answer");
    }, 1500);
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

document.addEventListener('DOMContentLoaded', () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal - using Bulma 
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if(e.key === "Escape") {
      closeAllModals();
    }
  });
});

function collapseBox() {
  const expandableContainer = document.getElementById('expandable-container');
  expandableContainer.innerHTML = ''; // Clear container
  const expandButton = document.createElement('button');
  expandButton.id = 'expand-button';
  expandButton.classList.add('button', 'is-light');
  expandButton.textContent = 'Instructions & Info';
  expandableContainer.appendChild(expandButton);
}


  document.addEventListener('DOMContentLoaded', function() {
    const expandableContainer = document.getElementById('expandable-container');

    expandableContainer.addEventListener('click', function(event) {
      const target = event.target;

      if (target.matches('#expand-button')) {
        // Replace button with a box containing the expanded text
        const expandedContent = document.createElement('div');
        expandedContent.classList.add('box');
        expandedContent.innerHTML = `
          <p style="margin-bottom: 10px;" >Test your knowledge of plants by identifying them based on images. You'll see a plant image and four options; choose the correct species. Toggle switches to include specific plant categories like flowers or herbs. Click the image for photo credits. Hints coming soon. &nbsp; &nbsp;</p>
          <button id="collapse-button" class="button is-light">Close</button>
        `;
        expandableContainer.innerHTML = ''; // Clear container
        expandableContainer.appendChild(expandedContent);
      } else if (target.matches('#collapse-button')) {
        // Revert to the original button
        const expandButton = document.createElement('button');
        expandButton.id = 'expand-button';
        expandButton.classList.add('button', 'is-light');
        expandButton.textContent = 'Instructions & Info';
        expandableContainer.innerHTML = ''; // Clear container
        expandableContainer.appendChild(expandButton);
      }
    });
  });




