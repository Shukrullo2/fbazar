const translations = {
  en: {
    searchTitle: "Search Tasks",
    searchLabel: "Search by project",
    searchButton: "Search",
    by: "By",
    clicks: (clicks) =>
      clicks === 1 ? "1 Click" : `${item.click_total} Clicks`,
    formInput: "Search",
  },
  ru: {
    searchTitle: "Поиск задач",
    searchLabel: "Поиск по проекту",
    searchButton: "Поиск",
    by: "От",
    clicks: (clicks) =>
      clicks === 1 ? "1 клик" : `${item.click_total} кликов`,
    formInput: "Поиск",
  },
  uz: {
    searchTitle: "Vazifalarni qidirish",
    searchLabel: "Loyihaga ko'ra qidirish",
    searchButton: "Qidirish",
    by: "Tomonidan",
    clicks: (clicks) =>
      clicks === 1 ? "1 ta klik" : `${item.click_total} ta klik`,
    formInput: "Qidirish",
  },
};

function changeLanguage() {
  const selectedLanguage = document.getElementById("language").value;
  localStorage.setItem("selectedLanguage", selectedLanguage);
  translatePage(selectedLanguage);
}

function translatePage(language) {
  const elementsToTranslate = document.querySelectorAll("[data-translate]");

  elementsToTranslate.forEach((element) => {
    const key = element.getAttribute("data-translate");

    // Handle dynamic content like clicks count
    elementsToTranslate.forEach((element) => {
      const key = element.getAttribute("data-translate");

      // Handle dynamic content like clicks count
      if (key === "clicks") {
        const clicks = parseInt(element.getAttribute("data-clicks"), 10);
        element.innerText = translations[language][key](clicks);
      } else if (element.tagName.toLowerCase() === "input") {
        // For input elements, update the value attribute
        element.value = translations[language][key];
        element.placeholder = translations[language][key];
      } else {
        element.innerText = translations[language][key];
      }
    });
  });

  // Adjust text direction if needed (LTR for these languages)
  document.body.style.direction = "ltr";
}

// Load stored language on page load
window.onload = () => {
  const storedLanguage = localStorage.getItem("selectedLanguage") || "en";
  document.getElementById("language").value = storedLanguage;
  translatePage(storedLanguage);
};
