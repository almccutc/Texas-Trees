// Declare switchElement in a broader scope
var switchElement;

switchElement = document.getElementById("switchRoundedDefault_trees");
switchElement.checked = true;

switchElement = document.getElementById("switchRoundedDefault_leaves");
switchElement.checked = true;

switchElement = document.getElementById("switchRoundedDefault_barks");
switchElement.checked = false;

switchElement = document.getElementById("switchState_wildflowers");
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
var map;
var countyLayers = [];
var selectedOption = null;

document.addEventListener("DOMContentLoaded", function() {
  map = L.map('map').setView([31.0000, -100.0000], 5.5);


  var texasBounds = L.latLngBounds(
      L.latLng(25.8371, -106.6466),
      L.latLng(36.5007, -93.5083)
  );

  map.setMaxBounds(texasBounds);
  map.on('drag', function() {
      map.panInsideBounds(texasBounds, { animate: false });
  });
  map.on('dragend', function() {
      if (!texasBounds.contains(map.getCenter())) {
          map.panInsideBounds(texasBounds);
      }
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Add the outline of Texas to the map using ArcGIS REST Services
  var texasOutlineLayer = L.esri.featureLayer({
      url: 'https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer/0',
      where: "STATE_NAME = 'Texas'",
      style: function () {
        return {
          color: '#006400', // Outline color
          weight: 2,        // Outline weight
          fillOpacity: 0    // Set fillOpacity to 0 to prevent filling the state
      };
      }
  }).addTo(map);

  // Add a reset button to reset the map to its initial view
  document.getElementById("resetButton").addEventListener("click", function() {
    map.setView([31.0000, -100.0000], 5.5);
});

  // Add error handling
  texasOutlineLayer.on('error', function(error) {
      console.error('Error loading Texas outline layer:', error);
  });
});


document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-input');
  const dropdownMenu = document.getElementById('dropdown-menu');
  const selectedOptionsContainer = document.getElementById('selected-options-container');

  // Function to toggle dropdown menu visibility
  function toggleDropdown() {
      dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
  }

  // Add event listener to input box to toggle dropdown menu
  searchInput.addEventListener('click', function () {
      toggleDropdown();
  });

  // Add event listener to input box to focus and show dropdown menu
  searchInput.addEventListener('focus', function () {
      toggleDropdown();
  });

  // Add event listener to input box for dynamic filtering
  searchInput.addEventListener('input', function () {
      const inputValue = searchInput.value.toLowerCase();
      const dropdownItems = dropdownMenu.querySelectorAll('.dropdown-item');

      dropdownItems.forEach(item => {
          const itemText = item.textContent.toLowerCase();
          if (itemText.includes(inputValue)) {
              item.style.display = 'block';
          } else {
              item.style.display = 'none';
          }
      });

      // Toggle dropdown menu visibility
      const hasVisibleItems = [...dropdownItems].some(item => item.style.display !== 'none');
      dropdownMenu.style.display = hasVisibleItems ? 'block' : 'none';
  });

  // Add event listener to close dropdown when item is clicked
dropdownMenu.addEventListener('click', function (event) {
  if (event.target.classList.contains('dropdown-item')) {
    if (selectedOption) {
      selectedOption.remove();
  }
      countyLayers.forEach(function (countyLayer) {
        map.removeLayer(countyLayer);
    });
      selectedOption = document.createElement('button');
      selectedOption.classList.add('button', 'is-success', 'is-light', 'selected-option');
      selectedOption.style.marginLeft = '5px';
      selectedOption.textContent = event.target.textContent;
      var selected_plant = event.target.textContent;

      fetch(`/get_county_names?selected_plant=${selected_plant}`)
      .then(response => response.json())
      .then(data => {
        countyNames = data.countyNames;

          // Create a where clause to select only the counties in the countyNames array
          var whereClause = "STATE_NAME = 'Texas' AND (";
          countyNames.forEach(function (countyName, index) {
              whereClause += "NAME = '" + countyName + " County'";
              if (index !== countyNames.length - 1) {
                  whereClause += " OR ";
              }
          });
          whereClause += ")";

          // Create the feature layer with the where clause
          var countyLayer = L.esri.featureLayer({
              url: 'https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Counties/FeatureServer/0',
              where: whereClause,
              style: function () {
                  return {
                      color: '#006400',
                      weight: 1,
                      // fillOpacity: 0.1
                  };
              }
          });

          countyLayers.push(countyLayer);

          // Check if map is a valid Leaflet map object
          if (typeof map !== 'undefined') {
              countyLayer.addTo(map); // Add the layer to the map
          } else {
              console.error('Leaflet map object is not defined.');
          }

      });

      // map.addLayers(countyLayers);
      


      // Create delete button and remove the selected option/county layers
      const deleteButton = document.createElement('button');
      deleteButton.classList.add('delete', 'is-small');
      deleteButton.addEventListener('click', function () {
          selectedOption.remove(); 
          countyLayers.forEach(function (countyLayer) {
            map.removeLayer(countyLayer);
        });
      });

      // Append non-breaking space between text and delete symbol
      selectedOption.appendChild(document.createTextNode('\u00A0')); // Unicode for non-breaking space
      
      // Append delete button to selected option
      selectedOption.appendChild(deleteButton);

      // Append selected option to container
      selectedOptionsContainer.appendChild(selectedOption);

      dropdownMenu.style.display = 'none';
      event.preventDefault();
      event.stopPropagation();
  }
});


  // Add event listener to close dropdown when clicking outside of it
  document.body.addEventListener('click', function (event) {
      if (!dropdownMenu.contains(event.target) && event.target !== searchInput) {
          dropdownMenu.style.display = 'none';
      }
  });
});


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
        switchState_wildflowers = document.getElementById("switchState_wildflowers").checked;
        switchState_grasses = document.getElementById("switchRoundedDefault_grasses").checked;
        switchState_aquaticplants = document.getElementById("switchRoundedDefault_aquaticplants").checked;
        switchState_vines = document.getElementById("switchRoundedDefault_vines").checked;
        // switchState_herbs = document.getElementById("switchRoundedDefault_herbs").checked;
        switchState_cacti = document.getElementById("switchRoundedDefault_cacti").checked;
        
        if (correctCheck == "true") {
          // Fetch new plant names and update buttons for the next round
        fetchPlantNameList(selectedIndex, switchState_trees, switchState_leaves, switchState_barks, switchState_wildflowers, switchState_grasses, switchState_aquaticplants, switchState_vines, switchState_cacti, previousPlantName);
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
function fetchPlantNameList(selectedIndex, switchState_trees, switchState_leaves, switchState_barks, switchState_wildflowers, switchState_grasses, switchState_aquaticplants, switchState_vines, switchState_cacti) {
  // Randomly select one index from the four
  randomIndex = Math.floor(Math.random() * 4);
  fetch(`/get_plant_name_list?switchState_trees=${switchState_trees}&switchState_leaves=${switchState_leaves}&switchState_barks=${switchState_barks}&switchState_wildflowers=${switchState_wildflowers}&switchState_grasses=${switchState_grasses}&switchState_aquaticplants=${switchState_aquaticplants}&switchState_vines=${switchState_vines}&switchState_cacti=${switchState_cacti}&previousPlantName=${previousPlantName}`)
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
    if(event.key === "Escape") {
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




