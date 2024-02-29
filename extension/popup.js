console.log("in popup");
document.addEventListener('DOMContentLoaded', function() {
    var sendUrlButton = document.getElementById('sendUrlButton');
    var resultDisplay = document.getElementById('resultDisplay');
    var imageDisplay = document.getElementById('imageDisplay');

    sendUrlButton.addEventListener('click', function() {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var currentUrl = tabs[0].url;

            chrome.runtime.sendMessage({ action: "sendUrl", url: currentUrl }, function(response) {
                console.log('Server response:', response.result);
            });
        });
    });


    chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
        if (request.action === "updatePopup") {
            resultDisplay.textContent = "Result: " + request.result;

            // Update image based on the result
            if (request.result === 'phishing') {
                imageDisplay.src = chrome.runtime.getURL('error.png');
                // Replace with your warning image URL
            } else {
                imageDisplay.src = chrome.runtime.getURL('check.png');
                // Replace with your tick mark image URL
            }
        }
    });
});




// full working code
// console.log("in popup");
// document.addEventListener('DOMContentLoaded', function() {
//     var sendUrlButton = document.getElementById('sendUrlButton');

//     sendUrlButton.addEventListener('click', function() {
//         chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//             var currentUrl = tabs[0].url;

//             chrome.runtime.sendMessage({ action: "sendUrl", url: currentUrl }, function(response) {
//                 console.log('Server response:', response.result);
//             });
//         });
//     });
// });

// document.addEventListener('DOMContentLoaded', function() {
//     var sendUrlButton = document.getElementById('sendUrlButton');

//     sendUrlButton.addEventListener('click', function() {
//         chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//             var currentUrl = tabs[0].url;
//             console.log(currentUrl);
//             fetch('http://localhost:5000/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'text/plain',
//                 },
//                 body: currentUrl,
//             })
//             // .then(response => response.text())
//             // .then(data => {
//             //     console.log('Server response:', data);
//             // })
//             // .catch(error => {
//             //     console.error('Error:', error);
//             // });
//         });
//     });
// });
