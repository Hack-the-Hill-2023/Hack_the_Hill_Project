let start = document.getElementsByClassName('richtext')[0];
let div = document.createElement("div"); 
div.classList.add("aem-GridColumn--default--12")
div.classList.add("aem-GridColumn")

start.parentNode.insertBefore(div, start.nextSibling);

let iframe = document.createElement("iframe")

iframe.style.border = "none"
iframe.style.width = "100%"

iframe.setAttribute("src", "http://127.0.0.1:5000/ext");

div.appendChild(iframe)

// fetch("http://127.0.0.1:5000/ext", {
//     method: "GET",
// })
// .then((res) => {
//     if (res.ok) { // ok if status is 2xx
//         console.log(res.status);
//     } else {
//         console.log('Request failed.  Returned status of ' + res.status);
//     }

//     return res.blob()
// })
// .then((blob) => {
//     blob.text()
//     .then((data) => JSON.parse(data))
//     .then((text) => {

//         div.innerHTML=text.data
//     })
// })