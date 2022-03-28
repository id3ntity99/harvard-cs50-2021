const backgroundTxt = document.querySelector(".background-text h1");

window.addEventListener("scroll", () => {
  if (window.scrollY >= 700) {
    backgroundTxt.classList.add("gradient");
  }
});
