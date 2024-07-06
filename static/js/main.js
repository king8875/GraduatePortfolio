document.addEventListener('DOMContentLoaded', function() {
    const slideContainer = document.querySelector('.slide-container');
    const slide = document.querySelector('.slide');
    const slideItems = document.querySelectorAll('.slide li');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    let currentIndex = 0;
    const totalSlides = slideItems.length;

    function updateSlidePosition() {
        const newTransform = -currentIndex * 100;
        slide.style.transform = `translateX(${newTransform}%)`;
    }

    function showNextSlide() {
        if (currentIndex < totalSlides - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateSlidePosition();
    }

    function showPrevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = totalSlides - 1;
        }
        updateSlidePosition();
    }

    nextButton.addEventListener('click', showNextSlide);
    prevButton.addEventListener('click', showPrevSlide);

});






const BoxContent = document.querySelectorAll(".box_content");

    BoxContent.forEach((div) => {
      const authorNameDiv = div.querySelector(".author_name_con");
      console.log("fogew");
  
      div.addEventListener("mouseover", () => {
        authorNameDiv.style.visibility = "visible";
      });
  
      div.addEventListener("mouseleave", () => {
        authorNameDiv.style.visibility = "hidden";
      });
    });
