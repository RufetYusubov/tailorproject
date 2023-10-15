const sliderItems = document.querySelectorAll('.slider-item');
const prevSlideBtn = document.querySelector('.prev-slide');
const nextSlideBtn = document.querySelector('.next-slide');

let currentIndex = 0;

function showSlide(index) {
    sliderItems.forEach((item, i) => {
        if (i === index) {
            item.style.opacity = 1;
        } else {
            item.style.opacity = 0;
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % sliderItems.length;
    showSlide(currentIndex);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + 2) % sliderItems.length; 
  showSlide(currentIndex);
}
nextSlideBtn.addEventListener('click', nextSlide);
prevSlideBtn.addEventListener('click', prevSlide);
// Otomatik geçiş süresi (milisaniye cinsinden) - 3000 ms (3 saniye) olarak ayarladık.
setInterval(nextSlide, 3000);


// Sayfa yüklendiğinde ilk slaydı göster
showSlide(currentIndex);
