// ==========================================
// CONFIGURATION & TOGGLES
// ==========================================
const ENABLE_MAP = false; // Set to true to enable the Leaflet map, false to turn it off completely

// ==========================================
// STATE MANAGEMENT
// ==========================================
const quizState = {
    plantNames: [],
    plantImageUrls: [],
    selectedIndex: null,
    correctPlantName: "",
    correctPlantIndex: 0,
    correctCount: 0,
    totalCount: 0,
    correctCheck: true,
    previousPlantName: "", 
    isAnsweringAllowed: true
};

// Map state variables
let map;
let countyLayers = [];
let selectedOption = null;

// ==========================================
// GLOBAL EVENT HANDLERS & HELPERS
// ==========================================

// Centralized switch state reader
function getCurrentSwitches() {
    const getCheck = (id) => document.getElementById(id)?.checked || false;
    return {
        trees: getCheck("switchRoundedDefault_trees"),
        leaves: getCheck("switchRoundedDefault_leaves"),
        barks: getCheck("switchRoundedDefault_barks"),
        wildflowers: getCheck("switchState_wildflowers"),
        grasses: getCheck("switchRoundedDefault_grasses"),
        aquaticplants: getCheck("switchRoundedDefault_aquaticplants"),
        vines: getCheck("switchRoundedDefault_vines"),
        cacti: getCheck("switchRoundedDefault_cacti")
    };
}

function handleOptionClick(index) {
    if (!quizState.isAnsweringAllowed) return;
    quizState.isAnsweringAllowed = false;

    if (document.activeElement) {
        document.activeElement.blur();
    }

    quizState.selectedIndex = index;
    checkSelectedAnswer(quizState.selectedIndex, quizState.correctPlantIndex);

    // Call for the next round after letting them see if they got it right
    setTimeout(() => {
        fetchPlantNameList(getCurrentSwitches());
    }, 400);
}

document.addEventListener("DOMContentLoaded", () => {
    // ---------------------------------------------------------
    // 1. INITIALIZE SWITCHES
    // ---------------------------------------------------------
    const switchDefaults = [
        { id: "switchRoundedDefault_trees", checked: true },
        { id: "switchRoundedDefault_leaves", checked: true },
        { id: "switchRoundedDefault_barks", checked: false },
        { id: "switchState_wildflowers", checked: false },
        { id: "switchRoundedDefault_grasses", checked: false },
        { id: "switchRoundedDefault_aquaticplants", checked: false },
        { id: "switchRoundedDefault_vines", checked: false },
        { id: "switchRoundedDefault_cacti", checked: false }
    ];

    switchDefaults.forEach(sw => {
        const el = document.getElementById(sw.id);
        if (el) el.checked = sw.checked;
    });

    // ---------------------------------------------------------
    // 2. INITIALIZE MAP (IF ENABLED)
    // ---------------------------------------------------------
    const mapContainer = document.getElementById('map');
    const resetButton = document.getElementById("resetButton");

    if (ENABLE_MAP) {
        if (mapContainer) mapContainer.style.display = 'block';
        if (resetButton) resetButton.style.display = 'inline-block';

        map = L.map('map').setView([31.0000, -100.0000], 5.5);

        const texasBounds = L.latLngBounds(
            L.latLng(25.8371, -106.6466),
            L.latLng(36.5007, -93.5083)
        );

        map.setMaxBounds(texasBounds);
        map.on('drag', () => {
            map.panInsideBounds(texasBounds, { animate: false });
        });
        map.on('dragend', () => {
            if (!texasBounds.contains(map.getCenter())) {
                map.panInsideBounds(texasBounds);
            }
        });

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        const texasOutlineLayer = L.esri.featureLayer({
            url: 'https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer/0',
            where: "STATE_NAME = 'Texas'",
            style: () => ({
                color: '#006400',
                weight: 2,
                fillOpacity: 0
            })
        }).addTo(map);

        texasOutlineLayer.on('error', (error) => {
            console.error('Error loading Texas outline layer:', error);
        });

        resetButton.addEventListener("click", () => {
            map.setView([31.0000, -100.0000], 5.5);
        });
    } else {
        if (mapContainer) mapContainer.style.display = 'none';
        if (resetButton) resetButton.style.display = 'none';
    }

    // ---------------------------------------------------------
    // 3. SEARCH & DROPDOWN LOGIC
    // ---------------------------------------------------------
    const searchInput = document.getElementById('search-input');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const selectedOptionsContainer = document.getElementById('selected-options-container');

    if (searchInput && dropdownMenu) {
        const toggleDropdown = () => {
            dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
        };

        searchInput.addEventListener('click', toggleDropdown);
        searchInput.addEventListener('focus', toggleDropdown);

        searchInput.addEventListener('input', () => {
            const inputValue = searchInput.value.toLowerCase();
            const dropdownItems = dropdownMenu.querySelectorAll('.dropdown-item');

            dropdownItems.forEach(item => {
                const itemText = item.textContent.toLowerCase();
                item.style.display = itemText.includes(inputValue) ? 'block' : 'none';
            });

            const hasVisibleItems = [...dropdownItems].some(item => item.style.display !== 'none');
            dropdownMenu.style.display = hasVisibleItems ? 'block' : 'none';
        });

        dropdownMenu.addEventListener('click', async (event) => {
            if (event.target.classList.contains('dropdown-item')) {
                event.preventDefault();
                event.stopPropagation();

                if (selectedOption) selectedOption.remove();
                
                if (ENABLE_MAP && map) {
                    countyLayers.forEach(layer => map.removeLayer(layer));
                    countyLayers = [];
                }

                const selectedPlant = event.target.textContent;

                selectedOption = document.createElement('button');
                selectedOption.classList.add('button', 'is-success', 'is-light', 'selected-option');
                selectedOption.style.marginLeft = '5px';
                selectedOption.textContent = selectedPlant;

                try {
                    const response = await fetch(`/get_county_names?selected_plant=${encodeURIComponent(selectedPlant)}`);
                    const data = await response.json();
                    const countyNames = data.countyNames;

                    if (ENABLE_MAP && map && countyNames.length > 0) {
                        const whereClause = `STATE_NAME = 'Texas' AND NAME IN (${countyNames.map(c => `'${c} County'`).join(',')})`;
                        
                        const countyLayer = L.esri.featureLayer({
                            url: 'https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Counties/FeatureServer/0',
                            where: whereClause,
                            style: () => ({
                                color: '#006400',
                                weight: 1
                            })
                        });

                        countyLayers.push(countyLayer);
                        countyLayer.addTo(map);
                    }
                } catch (error) {
                    console.error('Error fetching county names:', error);
                }

                const deleteButton = document.createElement('button');
                deleteButton.classList.add('delete', 'is-small');
                deleteButton.addEventListener('click', () => {
                    selectedOption.remove();
                    if (ENABLE_MAP && map) {
                        countyLayers.forEach(layer => map.removeLayer(layer));
                        countyLayers = [];
                    }
                });

                selectedOption.appendChild(document.createTextNode('\u00A0'));
                selectedOption.appendChild(deleteButton);
                selectedOptionsContainer.appendChild(selectedOption);

                dropdownMenu.style.display = 'none';
            }
        });

        document.body.addEventListener('click', (event) => {
            if (!dropdownMenu.contains(event.target) && event.target !== searchInput) {
                dropdownMenu.style.display = 'none';
            }
        });
    }

    // ---------------------------------------------------------
    // 4. QUIZ LOGIC & BUTTONS
    // ---------------------------------------------------------
    const optionButtons = document.querySelectorAll(".button-stack button");
    
    optionButtons.forEach((button, index) => {
        button.addEventListener("click", () => handleOptionClick(index));
    });

    const quizNextBtn = document.getElementById("quizNextButton");
    if (quizNextBtn) {
        const handleNextClick = () => {
            if (document.activeElement) document.activeElement.blur();
            
            fetchPlantNameList(getCurrentSwitches());

            setTimeout(() => {
                quizNextBtn.style.display = 'none';
                quizState.totalCount++;
                updateResultBox();
            }, 2000); 
        };

        quizNextBtn.addEventListener('click', handleNextClick);
    }

    // ---------------------------------------------------------
    // 5. MODAL LOGIC
    // ---------------------------------------------------------
    const openModal = ($el) => $el.classList.add('is-active');
    const closeModal = ($el) => $el.classList.remove('is-active');
    const closeAllModals = () => {
        document.querySelectorAll('.modal').forEach(closeModal);
    };

    document.querySelectorAll('.js-modal-trigger').forEach(($trigger) => {
        const modalId = $trigger.dataset.target;
        const $target = document.getElementById(modalId);
        if ($target) {
            $trigger.addEventListener('click', () => openModal($target));
        }
    });

    document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button').forEach(($close) => {
        const $target = $close.closest('.modal');
        $close.addEventListener('click', () => closeModal($target));
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === "Escape") closeAllModals();
    });

    // ---------------------------------------------------------
    // 6. INSTRUCTIONS EXPAND/COLLAPSE LOGIC
    // ---------------------------------------------------------
    const expandableContainer = document.getElementById('expandable-container');
    if (expandableContainer) {
        expandableContainer.addEventListener('click', (event) => {
            if (event.target.matches('#expand-button')) {
                expandableContainer.innerHTML = `
                  <div class="box">
                    <p style="margin-bottom: 10px;">Test your knowledge of plants by identifying them based on images. You'll see a plant image and four options; choose the correct species. Toggle switches to include specific plant categories like tree leaves or wildflowers. Click the image for photo credits. &nbsp; &nbsp;</p>
                    <button id="collapse-button" class="button is-light">Close</button>
                  </div>
                `;
            } else if (event.target.matches('#collapse-button')) {
                collapseBox();
            }
        });
    }

    // KICK OFF INITIAL PREFETCH SO ROUND 2 IS READY BEFORE THEY EVEN PLAY ROUND 1
    prefetchNextRound(getCurrentSwitches());
});


// ==========================================
// CORE FUNCTIONS & BACKGROUND PREFETCHING ENGINE
// ==========================================

let activePrefetchPromise = null;

// This function silently downloads the next round's data & image in the background
function prefetchNextRound(switches) {
    const switchesStr = JSON.stringify(switches);
    
    const queryParams = new URLSearchParams({
        switchState_trees: switches.trees,
        switchState_leaves: switches.leaves,
        switchState_barks: switches.barks,
        switchState_wildflowers: switches.wildflowers,
        switchState_grasses: switches.grasses,
        switchState_aquaticplants: switches.aquaticplants,
        switchState_vines: switches.vines,
        switchState_cacti: switches.cacti,
        previousPlantName: quizState.previousPlantName,
        _cb: new Date().getTime() 
    });

    activePrefetchPromise = new Promise(async (resolve, reject) => {
        try {
            const response = await fetch(`/get_plant_name_list?${queryParams.toString()}`, {
                method: 'GET',
                credentials: 'same-origin', 
                headers: {
                    'Cache-Control': 'no-cache, no-store, must-revalidate',
                    'Pragma': 'no-cache',
                    'Expires': '0'
                }
            });
            
            if (!response.ok) throw new Error("Network issue");
            const data = await response.json();
            
            // Instantly trigger the browser to download the S3 image into cache
            const nextImage = new Image();
            nextImage.src = data.plant_image_url[data.randomIndex];
            
            // Only resolve as "ready" once the S3 download finishes
            nextImage.onload = () => {
                resolve({ data: data, imageSrc: nextImage.src, switchesStr: switchesStr });
            };
            nextImage.onerror = () => {
                reject(new Error("Image failed to preload"));
            };
        } catch (error) {
            reject(error);
        }
    });
}

// Triggers when the user actually wants to go to the next round
async function fetchPlantNameList(switches) {
    const switchesStr = JSON.stringify(switches);
    
    // Provide visual feedback if they click fast and their internet is still loading the background prefetch
    const imageElement = document.getElementById("selectedPlantImage");
    if (imageElement) imageElement.style.opacity = '0.5';

    try {
        // FAST PATH: Wait for the background prefetch to finish!
        if (activePrefetchPromise) {
            try {
                const prefetched = await activePrefetchPromise;
                // Double check they didn't change the checkboxes while we were prefetching
                if (prefetched && prefetched.switchesStr === switchesStr) {
                    renderRound(prefetched.data, prefetched.imageSrc);
                    return; // Mission accomplished, instantly loaded!
                }
            } catch (err) {
                console.log("Background prefetch wasn't ready, falling back to manual fetch.");
            }
        }

        // SLOW PATH: Backup plan if the prefetch failed or they changed checkboxes right before clicking
        const queryParams = new URLSearchParams({
            switchState_trees: switches.trees,
            switchState_leaves: switches.leaves,
            switchState_barks: switches.barks,
            switchState_wildflowers: switches.wildflowers,
            switchState_grasses: switches.grasses,
            switchState_aquaticplants: switches.aquaticplants,
            switchState_vines: switches.vines,
            switchState_cacti: switches.cacti,
            previousPlantName: quizState.previousPlantName,
            _cb: new Date().getTime()
        });

        const response = await fetch(`/get_plant_name_list?${queryParams.toString()}`, {
            method: 'GET',
            credentials: 'same-origin', 
            headers: { 'Cache-Control': 'no-cache, no-store, must-revalidate' }
        });
        const data = await response.json();
        
        const nextImage = new Image();
        nextImage.src = data.plant_image_url[data.randomIndex];
        
        nextImage.onload = () => renderRound(data, nextImage.src);
        nextImage.onerror = () => {
            console.error("Failed to preload S3 image on fallback.");
            renderRound(data, nextImage.src); // Try to render anyway so we don't freeze the game
        };

    } catch (error) {
        console.error("Error fetching plant list:", error);
        quizState.isAnsweringAllowed = true;
        if (imageElement) imageElement.style.opacity = '1'; // Reset opacity if crashed
    }
}

// Separated the rendering logic to make the flow cleaner
function renderRound(data, imageSrc) {
    quizState.plantNames = data.plant_names;
    quizState.plantImageUrls = data.plant_image_url;
    
    const randomIndex = data.randomIndex; 
    const scientificNames = data.scientific_names;
    const plantTypes = data.plant_types;
    const source = data.source;
    const indices = Array.from({ length: quizState.plantNames.length }, (_, index) => index);

    // Wipe old classes and update buttons
    for (let i = 0; i < 4; i++) {
        let btn = document.querySelector(`.button-stack button:nth-child(${i + 1})`);
        if (btn) {
            // THE NUCLEAR OPTION FOR STICKY HOVER: 
            // Destroy the old button entirely and replace it with a perfect clone.
            // A brand new DOM element physically cannot retain the mobile hover state!
            let freshBtn = btn.cloneNode(true);
            btn.parentNode.replaceChild(freshBtn, btn);
            btn = freshBtn; // Switch our reference to the new clean button
            
            // Re-attach the click listener since cloning strips JavaScript events
            btn.addEventListener("click", () => handleOptionClick(i));

            btn.classList.remove('true', 'false', 'is-focused', 'is-hovered', 'is-active');
            btn.setAttribute("data-is-correct", "no-answer");

            const commonEl = btn.querySelector('.common-name');
            const scientificEl = btn.querySelector('.scientific-name');
            const typeEl = btn.querySelector('.tree-type');

            if (commonEl) commonEl.innerHTML = quizState.plantNames[indices[i]];
            if (scientificEl) scientificEl.innerHTML = scientificNames[indices[i]];
            if (typeEl) typeEl.innerHTML = plantTypes[indices[i]];
        }
    }

    // Update Image & Text seamlessly
    const imageElement = document.getElementById("selectedPlantImage");
    if (imageElement) {
        imageElement.src = imageSrc; 
        imageElement.style.opacity = '1'; // Ensure opacity is reset from loading state
    }

    const textElement = document.getElementById("modal-text");
    if (textElement) textElement.textContent = source[randomIndex];

    // Update State variables
    quizState.correctPlantIndex = randomIndex; 
    quizState.previousPlantName = quizState.plantNames[randomIndex]; 

    collapseBox();
    quizState.isAnsweringAllowed = true;

    // THE MOST IMPORTANT STEP: Instantly trigger the next prefetch so the next round is ready!
    prefetchNextRound(getCurrentSwitches());
}

function checkSelectedAnswer(selectedIndex, correctPlantIndex) {
    const selectedButton = document.querySelector(`.button-stack button:nth-child(${selectedIndex + 1})`);
    
    quizState.totalCount++;

    if (selectedButton) {
        const isCorrect = selectedIndex === correctPlantIndex;

        selectedButton.setAttribute("data-is-correct", isCorrect ? "true" : "false");

        if (isCorrect) {
            selectedButton.classList.add("true");
            quizState.correctCount++;
            quizState.correctCheck = true;
        } else {
            selectedButton.classList.add("false");
            quizState.correctCheck = false;

            // Highlight the correct answer to show them what it was!
            const correctButton = document.querySelector(`.button-stack button:nth-child(${correctPlantIndex + 1})`);
            if (correctButton) {
                correctButton.classList.add("true");
                setTimeout(() => correctButton.classList.remove("true"), 700); 
            }
        }
    }

    updateResultBox();
}

function updateResultBox() {
    const resultTextSpan = document.getElementById("resultText");
    if (resultTextSpan) {
        resultTextSpan.textContent = `Correct: ${quizState.correctCount}/${quizState.totalCount}`;
    }
}

function collapseBox() {
    const expandableContainer = document.getElementById('expandable-container');
    if (expandableContainer) {
        expandableContainer.innerHTML = ''; 
        const expandButton = document.createElement('button');
        expandButton.id = 'expand-button';
        expandButton.classList.add('button', 'is-light');
        expandButton.textContent = 'Instructions & Info';
        expandableContainer.appendChild(expandButton);
    }
}