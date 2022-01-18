// Get the modal
const modalAddDesc = document.getElementById("modal_addDesc");

// Get the button that opens the modal
const addDescBtn = document.getElementById("addDescBtn");

// Get the <span> element that closes the modal
const closeAdd = document.getElementById("closeAdd");

// When the user clicks the button, open the modal
if (addDescBtn) {
    addDescBtn.onclick = function() {
        modalAddDesc.style.display = "block";
    }
}

closeAdd.onclick = function() {
    modalAddDesc.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalAddDesc) {
        modalAddDesc.style.display = "none";
    } 
};