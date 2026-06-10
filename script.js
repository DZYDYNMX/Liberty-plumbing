document.addEventListener('DOMContentLoaded', () => {
    // ── Hamburger & Mobile Dropdowns ───────────────────────────
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

        // Lightbox Intercept
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            const lightbox = document.getElementById('lightbox-modal');
            if (lightbox) {
                const galleryItems = Array.from(document.querySelectorAll('.gallery-item'));
                const index = galleryItems.indexOf(galleryItem);
                const img = galleryItem.querySelector('img');
                if (img) {
                    const lightboxImg = lightbox.querySelector('.lightbox-img');
                    lightboxImg.src = img.src;
                    lightbox.dataset.currentIndex = index;
                    lightbox.classList.add('active');
                    document.body.classList.add('no-scroll');
                }
            }
            return;
        }
        
        const lightbox = document.getElementById('lightbox-modal');
        if (lightbox && lightbox.classList.contains('active')) {
            if (e.target.closest('.lightbox-close') || e.target === lightbox) {
                lightbox.classList.remove('active');
                document.body.classList.remove('no-scroll');
                return;
            }
            
            const galleryItems = Array.from(document.querySelectorAll('.gallery-item img'));
            if (galleryItems.length > 0) {
                let currentIndex = parseInt(lightbox.dataset.currentIndex) || 0;
                let changed = false;
                
                if (e.target.closest('.lightbox-prev')) {
                    currentIndex--;
                    changed = true;
                } else if (e.target.closest('.lightbox-next')) {
                    currentIndex++;
                    changed = true;
                }
                
                if (changed) {
                    if (currentIndex < 0) currentIndex = galleryItems.length - 1;
                    if (currentIndex >= galleryItems.length) currentIndex = 0;
                    lightbox.dataset.currentIndex = currentIndex;
                    const lightboxImg = lightbox.querySelector('.lightbox-img');
                    lightboxImg.src = galleryItems[currentIndex].src;
                    return;
                }
            }
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
            document.querySelectorAll('.modal-overlay, .lightbox-overlay').forEach(m => m.remove());
            doc.querySelectorAll('.modal-overlay, .lightbox-overlay').forEach(m => document.body.appendChild(m));

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
            
            // Re-initialize dynamic components
            initMobileCollapse();
            initReadMoreText();
            initMarquees();
        } catch (error) {
            console.error('SPA Navigation failed:', error);
            window.location.href = url; // Hard fallback
        }
    }

    // ── Accordion Logic ────────────────────────────────────────
    document.body.addEventListener('click', e => {
        const header = e.target.closest('.accordion-header');
        if (!header) return;
        
        const item = header.closest('.accordion-item');
        const isFAQ = item.closest('#faq'); // if it is FAQ, maybe close others? We'll just toggle for now.
        
        // If we want only one open at a time in the same container:
        const container = item.parentElement;
        const currentActive = container.querySelector('.accordion-item.active');
        
        if (currentActive && currentActive !== item) {
            currentActive.classList.remove('active');
        }
        
        item.classList.toggle('active');
    });

    // ── Progressive Disclosure Logic ────────────────────────────
    function initMobileCollapse() {
        if (window.innerWidth > 768) return;
        document.querySelectorAll('.mobile-collapse').forEach(container => {
            if (container.dataset.initialized) return;
            container.dataset.initialized = 'true';
            
            const limit = parseInt(container.getAttribute('data-collapse-limit')) || 4;
            const children = Array.from(container.children).filter(c => !c.classList.contains('show-more-btn'));
            
            if (children.length > limit) {
                children.forEach((child, index) => {
                    if (index >= limit) {
                        child.classList.add('mobile-hidden');
                    }
                });
                
                const btn = document.createElement('button');
                btn.className = 'show-more-btn';
                btn.textContent = 'Show More ▾';
                btn.onclick = () => {
                    const isHidden = children[limit].classList.contains('mobile-hidden');
                    children.forEach((child, index) => {
                        if (index >= limit) {
                            child.classList.toggle('mobile-hidden', !isHidden);
                        }
                    });
                    btn.textContent = isHidden ? 'Show Less ▴' : 'Show More ▾';
                    if (!isHidden) {
                        setTimeout(() => {
                            const offset = container.getBoundingClientRect().top + window.scrollY - 80; // 80px for navbar offset
                            window.scrollTo({ top: offset, behavior: 'smooth' });
                        }, 50);
                    }
                };
                container.parentNode.insertBefore(btn, container.nextSibling);
            }
        });
    }

    function initReadMoreText() {
        if (window.innerWidth > 768) return;
        document.querySelectorAll('.read-more-text').forEach(container => {
            if (container.dataset.initialized) return;
            container.dataset.initialized = 'true';
            
            const btn = document.createElement('button');
            btn.className = 'read-more-btn';
            btn.textContent = 'Read More';
            btn.onclick = () => {
                const isExpanded = container.classList.contains('expanded');
                container.classList.toggle('expanded');
                btn.textContent = isExpanded ? 'Read More' : 'Read Less';
                if (isExpanded) {
                    setTimeout(() => {
                        const offset = container.getBoundingClientRect().top + window.scrollY - 100; // offset
                        window.scrollTo({ top: offset, behavior: 'smooth' });
                    }, 50);
                }
            };
            container.appendChild(btn);
            
            // Only show button if text actually overflows
            const textContent = container.querySelector('.text-content');
            if (textContent && textContent.scrollHeight > textContent.clientHeight) {
                btn.style.display = 'inline-block';
            }
        });
    }

    function initMarquees() {
        document.querySelectorAll('.marquee-container').forEach(container => {
            if (container.dataset.marqueeInitialized) return;
            container.dataset.marqueeInitialized = 'true';

            const track = container.querySelector('.marquee-track');
            if (!track) return;

            // Clone items to create seamless loop
            const items = Array.from(track.children);
            items.forEach(item => {
                const clone = item.cloneNode(true);
                track.appendChild(clone);
            });
            items.forEach(item => {
                const clone = item.cloneNode(true);
                track.appendChild(clone);
            });

            let currentX = 0;
            let targetSpeed = -1; // default scroll speed
            let currentSpeed = targetSpeed;
            let isHovering = false;
            let isDragging = false;
            let startX = 0;
            let dragLastX = 0;

            function getOriginalWidth() {
                let w = 0;
                items.forEach(i => w += i.offsetWidth + parseFloat(window.getComputedStyle(track).gap || 0));
                return w;
            }

            function loop() {
                if (!isDragging) {
                    currentSpeed += (targetSpeed - currentSpeed) * 0.1;
                    currentX += currentSpeed;
                }

                const origWidth = getOriginalWidth();
                if (origWidth > 0) {
                    if (currentX <= -origWidth) {
                        currentX += origWidth;
                    }
                    if (currentX >= 0) {
                        currentX -= origWidth;
                    }
                }

                track.style.transform = `translateX(${currentX}px)`;
                requestAnimationFrame(loop);
            }

            requestAnimationFrame(loop);

            // Mouse tracking
            container.addEventListener('mouseenter', () => isHovering = true);
            container.addEventListener('mouseleave', () => {
                isHovering = false;
                if (!isDragging) targetSpeed = -1;
            });
            container.addEventListener('mousemove', (e) => {
                if (isHovering && !isDragging) {
                    const rect = container.getBoundingClientRect();
                    const xRatio = (e.clientX - rect.left) / rect.width;
                    targetSpeed = (0.5 - xRatio) * 5; // scales from -2.5 to 2.5
                }
            });

            // Touch dragging
            container.addEventListener('touchstart', (e) => {
                isDragging = true;
                container.classList.add('is-dragging');
                dragLastX = e.touches[0].clientX;
            }, {passive: true});

            container.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                const currentTouchX = e.touches[0].clientX;
                currentX += (currentTouchX - dragLastX);
                dragLastX = currentTouchX;
            }, {passive: true});

            const endDrag = () => {
                if (!isDragging) return;
                isDragging = false;
                container.classList.remove('is-dragging');
                targetSpeed = -1;
            };

            container.addEventListener('touchend', endDrag);
            container.addEventListener('touchcancel', endDrag);

            // Desktop dragging fallback
            container.addEventListener('mousedown', (e) => {
                isDragging = true;
                container.classList.add('is-dragging');
                dragLastX = e.clientX;
            });
            window.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                const currentMouseX = e.clientX;
                currentX += (currentMouseX - dragLastX);
                dragLastX = currentMouseX;
            });
            window.addEventListener('mouseup', endDrag);
        });
    }

    initMobileCollapse();
    initReadMoreText();
    initMarquees();
    // Handle window resize cleanly without losing state (optional, basic re-init)
    window.addEventListener('resize', () => {
        if (window.innerWidth <= 768) {
            initMobileCollapse();
            initReadMoreText();
        }
    });

});
