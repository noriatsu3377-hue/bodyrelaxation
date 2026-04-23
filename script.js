document.addEventListener('DOMContentLoaded', () => {

    /* ==============================================
       Opening Animation
       ============================================== */
    const opening = document.getElementById('opening');
    if (opening) {
        // Hide the opening screen after 2.5 seconds
        setTimeout(() => {
            opening.style.opacity = '0';
            opening.style.visibility = 'hidden';
        }, 2500);
    }

    /* ==============================================
       Scroll Animation (Fade Up)
       ============================================== */
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px', // Trigger slightly before it comes into view
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Optional: stop observing once visible
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-up');
    fadeElements.forEach(el => {
        observer.observe(el);
    });

    /* ==============================================
       FAQ Accordion
       ============================================== */
    const accordions = document.querySelectorAll('.accordion-header');
    
    accordions.forEach(acc => {
        acc.addEventListener('click', function() {
            this.classList.toggle('active');
            
            const panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    });

});
