// Get the element you want to scroll horizontally
const container = document.getElementsByClassName("item");

// Define the amount to scroll each time
const scrollAmount = 10; // Adjust this value as needed

// Function to scroll left
function scrollLeft() {
  container.scrollLeft -= scrollAmount;
}

// Function to scroll right
function scrollRight() {
  container.scrollLeft += scrollAmount;
}
function openPythonEditor() {
  window.location.href = "/python";
}

function openJavaEditor() {
  window.location.href = "/java";
}
function openCEditor() {
  window.location.href = "/c";
}
function openhtmlcssEditor() {
  window.location.href = "/htmlcss";
}
function openjavascriptEditor() {
  window.location.href = "/javascript";
}
function openphpEditor() {
  window.location.href = "/php";
}
function opencppEditor() {
  window.location.href = "/cpp";
}
function openrubyEditor() {
  window.location.href = "/ruby";
}
function openrEditor() {
  window.location.href = "/r";
}
document.getElementById("searchLink").addEventListener("click", function(event) {
  event.preventDefault(); // Prevent the link from navigating
  searchLanguages(); // Call the search function
});
