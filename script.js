document.addEventListener('DOMContentLoaded', () => {
    // ── Hamburger ──────────────────────────────────────────────
    const hamburger = document.querySelector('.hamburger');
    const navLinks  = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            const expanded = hamburger.getAttribute('aria-expanded') === 'true';
            hamburger.setAttribute('aria-expanded', String(!expanded));
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // ── Review Carousel Logic ──────────────────────────────────
    function initCarousel() {
        const track = document.getElementById('review-track');
        if (!track) return;
        const slides = Array.from(track.children);
        if (slides.length === 0) return;
        
        const nextBtn = document.getElementById('next-btn');
        const prevBtn = document.getElementById('prev-btn');
        
        let currentIndex = 0;
        let isDragging = false;
        let startPos = 0;
        let currentTranslate = 0;
        let prevTranslate = 0;
        let animationID;

        function updateCarousel() {
            const slideWidth = slides[0].getBoundingClientRect().width;
            const gap = 32; // 2rem gap
            currentTranslate = currentIndex * -(slideWidth + gap);
            prevTranslate = currentTranslate;
            track.style.transform = `translateX(${currentTranslate}px)`;
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < slides.length - 1) currentIndex++;
                updateCarousel();
            });
        }
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) currentIndex--;
                updateCarousel();
            });
        }

        // Drag handlers
        track.addEventListener('mousedown', dragStart);
        track.addEventListener('touchstart', dragStart, {passive: true});
        track.addEventListener('mouseup', dragEnd);
        track.addEventListener('mouseleave', dragEnd);
        track.addEventListener('touchend', dragEnd);
        track.addEventListener('mousemove', dragAction);
        track.addEventListener('touchmove', dragAction, {passive: true});

        function dragStart(e) {
            isDragging = true;
            startPos = getPositionX(e);
            animationID = requestAnimationFrame(animationLoop);
            track.style.transition = 'none';
        }

        function dragAction(e) {
            if (!isDragging) return;
            const currentPosition = getPositionX(e);
            currentTranslate = prevTranslate + currentPosition - startPos;
        }

        function dragEnd() {
            isDragging = false;
            cancelAnimationFrame(animationID);
            const movedBy = currentTranslate - prevTranslate;
            
            // Snap threshold
            if (movedBy < -100 && currentIndex < slides.length - 1) currentIndex += 1;
            if (movedBy > 100 && currentIndex > 0) currentIndex -= 1;
            
            track.style.transition = 'transform 0.5s ease-out';
            updateCarousel();
        }

        function getPositionX(event) {
            return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
        }

        function animationLoop() {
            track.style.transform = `translateX(${currentTranslate}px)`;
            if (isDragging) requestAnimationFrame(animationLoop);
        }
        
        // Auto-play (optional)
        // setInterval(() => {
        //     if (!isDragging && currentIndex < slides.length - 1) { currentIndex++; updateCarousel(); }
        //     else if (!isDragging && currentIndex === slides.length - 1) { currentIndex = 0; updateCarousel(); }
        // }, 5000);

        window.addEventListener('resize', updateCarousel);
    }
    initCarousel();

    // ── Global Click Event Delegation (SPA & Modals) ───────────
    document.body.addEventListener('click', async e => {
        // Modals
        const contactModal = document.getElementById('contact-modal');
        
        if (e.target.classList.contains('modal-overlay')) {
            e.target.classList.remove('active');
            document.body.classList.remove('no-scroll');
        }
        const closeBtn = e.target.closest('.modal-close');
        if (closeBtn) {
            const modal = closeBtn.closest('.modal-overlay');
            if (modal) {
                modal.classList.remove('active');
                document.body.classList.remove('no-scroll');
            }
        }

        // Contact Button Intercept
        const contactBtn = e.target.closest('.contact-btn');
        if (contactBtn && contactModal) {
            e.preventDefault();
            contactModal.classList.add('active');
            document.body.classList.add('no-scroll');
            
            const svc = contactBtn.getAttribute('data-service');
            if (svc) {
                const sel = document.getElementById('modal-service');
                if (sel) sel.value = svc;
            }
            return;
        }

        // SPA Navigation Intercept
        const link = e.target.closest('a');
        if (!link || link.target === '_blank' || link.hasAttribute('download')) return;
        
        const url = new URL(link.href, window.location.href);
        if (url.origin !== window.location.origin) return;
        if (url.pathname === window.location.pathname && url.hash) return;
        if (url.pathname.endsWith('.pdf') || url.pathname.endsWith('.mp4') || url.pathname.endsWith('.png')) return;
        
        // Don't intercept tel: links
        if (url.protocol === 'tel:') return;

        e.preventDefault();

        // Close mobile nav if open
        if (hamburger && navLinks) {
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
            navLinks.classList.remove('active');
        }

        await navigateTo(url.href);
    });

    // ── SPA Routing Logic ──────────────────────────────────────
    window.addEventListener('popstate', () => {
        navigateTo(window.location.href, false);
    });

    async function navigateTo(url, push = true) {
        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error('Network error');
            const html = await response.text();
            
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            
            // Swap main content securely
            const newMain = doc.querySelector('main.main-content');
            const currentMain = document.querySelector('main.main-content');
            if (newMain && currentMain) {
                currentMain.innerHTML = newMain.innerHTML;
                currentMain.className = newMain.className;
            }

            // Re-init carousel if present
            initCarousel();

            // Swap modals dynamically
            document.querySelectorAll('.modal-overlay').forEach(m => m.remove());
            doc.querySelectorAll('.modal-overlay').forEach(m => document.body.appendChild(m));

            // Swap background image if it has changed
            const newImgSrc = doc.querySelector('#bg-image')?.getAttribute('src');
            const currentImg = document.getElementById('bg-image');
            if (newImgSrc && currentImg) {
                if (currentImg.getAttribute('src') !== newImgSrc) {
                    currentImg.setAttribute('src', newImgSrc);
                }
            }

            // Update title
            document.title = doc.title;

            // Update active nav link
            const pathname = new URL(url).pathname;
            document.querySelectorAll('.nav-links a').forEach(a => {
                a.classList.remove('active');
                const href = a.getAttribute('href');
                if (pathname.endsWith(href) || (pathname.endsWith('/') && href === 'index.html')) {
                    a.classList.add('active');
                }
            });

            if (push) {
                window.history.pushState({}, '', url);
            }

            window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch (error) {
            console.error('SPA Navigation failed:', error);
            window.location.href = url; // Hard fallback
        }
    }
});
