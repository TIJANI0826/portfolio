// =============================================
// IBRAHIM TIJANI PORTFOLIO — Main JavaScript
// =============================================

document.addEventListener('DOMContentLoaded', () => {

    // === NAV SCROLL ===
    const navbar = document.getElementById('navbar');
    const handleNavScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', handleNavScroll, { passive: true });

    // === HAMBURGER MENU ===
    const menuBtn = document.getElementById('menuBtn');
    const navLinks = document.querySelector('.nav-links');
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            menuBtn.classList.toggle('active');
        });
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => {
                navLinks.classList.remove('open');
                menuBtn.classList.remove('active');
            });
        });
    }

    // === COUNTER ANIMATION ===
    const counters = document.querySelectorAll('.stat-num[data-target]');
    const runCounter = (el) => {
        const target = parseInt(el.dataset.target);
        const duration = 1500;
        const step = target / (duration / 16);
        let current = 0;
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                el.textContent = target;
                clearInterval(timer);
            } else {
                el.textContent = Math.floor(current);
            }
        }, 16);
    };

    // Run counters when hero is visible
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                counters.forEach(counter => runCounter(counter));
                heroObserver.disconnect();
            }
        });
    }, { threshold: 0.3 });
    const heroSection = document.getElementById('hero');
    if (heroSection) heroObserver.observe(heroSection);

    // === SKILL BAR ANIMATION ===
    const skillFills = document.querySelectorAll('.skill-fill');
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fills = entry.target.querySelectorAll('.skill-fill');
                fills.forEach((fill, i) => {
                    setTimeout(() => {
                        fill.style.width = fill.dataset.width + '%';
                    }, i * 60);
                });
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.skill-category-card').forEach(card => {
        skillObserver.observe(card);
    });

    // === FADE-IN ANIMATIONS ===
    const fadeEls = document.querySelectorAll(
        '.timeline-card, .skill-category-card, .project-card, .project-card-small, .cert-card, .achievement-card, .info-card'
    );
    fadeEls.forEach(el => el.classList.add('fade-in'));

    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    fadeEls.forEach(el => fadeObserver.observe(el));

    // === ACTIVE NAV LINK ===
    const sections = document.querySelectorAll('section[id]');
    const navLinksAll = document.querySelectorAll('.nav-links a');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinksAll.forEach(a => {
                    a.style.color = a.getAttribute('href') === `#${id}` ? 'var(--accent)' : '';
                });
            }
        });
    }, { threshold: 0.4 });

    sections.forEach(section => sectionObserver.observe(section));

    // === SMOOTH PARALLAX ON ORBS ===
    const orbs = document.querySelectorAll('.orb');
    if (orbs.length && window.innerWidth > 768) {
        window.addEventListener('mousemove', (e) => {
            const x = (e.clientX / window.innerWidth - 0.5) * 20;
            const y = (e.clientY / window.innerHeight - 0.5) * 20;
            orbs.forEach((orb, i) => {
                const factor = (i + 1) * 0.5;
                orb.style.transform = `translate(${x * factor}px, ${y * factor}px)`;
            });
        }, { passive: true });
    }

    // === TYPING CURSOR ON HERO TITLE ===
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        heroTitle.style.borderRight = '2px solid var(--accent)';
        let i = 0;
        const typeInterval = setInterval(() => {
            heroTitle.textContent += text[i];
            i++;
            if (i >= text.length) {
                clearInterval(typeInterval);
                setTimeout(() => { heroTitle.style.borderRight = 'none'; }, 800);
            }
        }, 40);
    }

});
