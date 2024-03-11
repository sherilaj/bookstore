function enlargeImage() {
    var image = document.getElementById('bookImage');
    image.style.transform = 'scale(1.1)'; // Increase size by 10%
    // Optionally, you can set a transition for a smoother effect
    image.style.transition = 'transform 0.2s ease';
    
    // Reset the size after a short delay (e.g., 500 milliseconds)
    setTimeout(function() {
        image.style.transform = 'scale(1)';
    }, 500);
}
