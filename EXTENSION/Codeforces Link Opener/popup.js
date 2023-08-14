document.getElementById('openLinksButton').addEventListener('click', () => {
    chrome.scripting.executeScript({
      target: { tabId: chrome.tabs.getCurrent().id },
      function: openCodeforcesLinksInNewTabs
    });
  });
  
  function openCodeforcesLinksInNewTabs() {
    const links = document.querySelectorAll('a');
    links.forEach(link => {
      if (link.href.includes('codeforces.com')) {
        link.target = '_blank';
      }
    });
  }
  