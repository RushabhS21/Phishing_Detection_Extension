chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.action === "sendUrl") {
            // Handle the URL and send it to the server
            var currentUrl = request.url;
            // console.log(currentUrl);
            fetch('http://localhost:5000/main', {
                method: 'POST',
                headers: {
                    'Content-Type': 'text/plain',
                },
                body: currentUrl,
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                chrome.runtime.sendMessage({ action: "updatePopup", result: data.result });
            })
            // .catch(error => {
            //     console.error('Error:', error);
            // });
            sendResponse({ result: "success" });

            fetch('http://localhost:5000/info', {
                method: 'POST',
                headers: {
                    'Content-Type': 'text/plain',
                },
                body: currentUrl,
            })
            .then(response => response.text())
            .then(data => {
                console.log('Server response for analysis:', data);
                // Handle the response for analysis as needed
            })
            // .then(response => response.json())
            // .then(data => {
            //     console.log(data);
            //     chrome.runtime.sendMessage({ action: "updatePopup", result: data.result });
            // })

            // Send a response if needed
            sendResponse({ result: "success" });



        }
    }
);


// full working code below
// chrome.runtime.onMessage.addListener(
//     function(request, sender, sendResponse) {
//         if (request.action === "sendUrl") {
//             // Handle the URL and send it to the server
//             var currentUrl = request.url;
//             // console.log(currentUrl);
//             fetch('http://localhost:5000/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'text/plain',
//                 },
//                 body: currentUrl,
//             })
//             .then(response => response.text())
//             .then(data => {
//                 console.log(data);
//                 chrome.runtime.sendMessage({ action: "updatePopup", result: data });
//             })
//             // .catch(error => {
//             //     console.error('Error:', error);
//             // });

//             // Send a response if needed
//             sendResponse({ result: "success" });
//         }
//     }
// );
