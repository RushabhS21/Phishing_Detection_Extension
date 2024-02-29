console.log("in background");
let lastTabUrl = "";
chrome.tabs.onActivated.addListener((activeInfo) => {
    chrome.tabs.get(activeInfo.tabId, (tab) => {
      const currentUrl = tab.url;
      console.log(currentUrl);
      if (currentUrl != lastTabUrl) {
        fetch(`http://localhost:5000/`, {
        method: "POST",
        headers: {
            "Content-Type": "text/plain",
        },
        body: currentUrl,
      });
    }
    });
});