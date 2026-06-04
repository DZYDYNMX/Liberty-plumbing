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
