// Select the first element with the class 'richtext'
let start = document.getElementsByClassName('richtext')[0];

// Create a new div element
let div = document.createElement("div"); 

// Add two classes to the new div element
div.classList.add("aem-GridColumn--default--12")
div.classList.add("aem-GridColumn")

// Insert the new div element before the element selected in the first step
start.parentNode.insertBefore(div, start.nextSibling);

// Create a new iframe element
let iframe = document.createElement("iframe")

// Set the CSS styles for the iframe element
iframe.style.border = "none"
iframe.style.width = "100%"
iframe.style.minHeight = "300px"

// Set the source attribute of the iframe element
iframe.setAttribute("src", "http://127.0.0.1:5000/ext");

// Append the iframe element to the newly created div element
div.appendChild(iframe)
