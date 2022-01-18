// Get the modal
const modal_add_club = document.getElementById("modal_add_club");

// Get the button that opens the modal
const addBtn = document.getElementById("addBtn");

// Get the <span> element that closes the modal
const closeAdd = document.getElementById("closeAdd");

// When the user clicks the button, open the modal
if (addBtn) {
    addBtn.onclick = function() {
        modal_add_club.style.display = "block";
    }
}

closeAdd.onclick = function() {
    modal_add_club.style.display = "none";
}
