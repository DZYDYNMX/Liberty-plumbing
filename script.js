document.addEventListener('DOMContentLoaded', () => {
    // ── Video Autoplay Kickstarter ─────────────────────────────
    const bgVideos = document.querySelectorAll('video');
    bgVideos.forEach(video => {
        video.muted = true;
        const playPromise = video.play();
        if (playPromise !== undefined) {
            playPromise.catch(() => {
                document.body.addEventListener('touchstart', () => { video.play(); }, { once: true });
                document.body.addEventListener('click', () => { video.play(); }, { once: true });
            });
        }
    });

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

    // ── SPA Navigation Intercept ───────────────────────────────
    document.body.addEventListener('click', async e => {
        const link = e.target.closest('a');
        if (!link || link.target === '_blank' || link.hasAttribute('download')) return;
        
        const url = new URL(link.href, window.location.href);
        if (url.origin !== window.location.origin) return;
        if (url.pathname === window.location.pathname && url.hash) return;
        if (url.pathname.endsWith('.pdf') || url.pathname.endsWith('.mp4')) return;
        
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

            // Swap background video if it has changed
            const newVideoSrc = doc.querySelector('#bg-video source')?.getAttribute('src');
            const currentVideo = document.getElementById('bg-video');
            if (newVideoSrc && currentVideo) {
                const currentSource = currentVideo.querySelector('source');
                if (currentSource && currentSource.getAttribute('src') !== newVideoSrc) {
                    currentSource.setAttribute('src', newVideoSrc);
                    currentVideo.load();
                    const playPromise = currentVideo.play();
                    if (playPromise !== undefined) {
                        playPromise.catch(e => console.log('Video autoplay interrupted:', e));
                    }
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
