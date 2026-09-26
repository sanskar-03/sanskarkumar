(() => {
    const root = document.documentElement;
    const getStoredTheme = () => {
        try { return localStorage.getItem("portfolio-theme"); } catch (_) { return null; }
    };
    const setStoredTheme = (theme) => {
        try { localStorage.setItem("portfolio-theme", theme); } catch (_) {}
    };

    const applyTheme = (theme) => {
        root.dataset.theme = theme;
        document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
            const isDark = theme === "dark";
            button.setAttribute("aria-pressed", String(isDark));
            button.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
            const icon = button.querySelector(".theme-icon");
            if (icon) icon.textContent = isDark ? "☼" : "◐";
            const label = button.querySelector(".theme-label");
            if (label) label.textContent = isDark ? "Light" : "Dark";
        });
    };

    const stored = getStoredTheme();
    const initialTheme = stored || (window.matchMedia?.("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    root.dataset.theme = initialTheme;

    document.addEventListener("DOMContentLoaded", () => {
        const toggle = document.querySelector(".menu-toggle");
        const nav = document.querySelector(".site-nav");

        if (toggle && nav) {
            toggle.addEventListener("click", () => {
                const open = nav.classList.toggle("is-open");
                toggle.setAttribute("aria-expanded", String(open));
                toggle.textContent = open ? "Close" : "Menu";
            });
            nav.querySelectorAll("a").forEach((link) => {
                link.addEventListener("click", () => {
                    nav.classList.remove("is-open");
                    toggle.setAttribute("aria-expanded", "false");
                    toggle.textContent = "Menu";
                });
            });
        }

        document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
            button.addEventListener("click", () => {
                const next = root.dataset.theme === "dark" ? "light" : "dark";
                setStoredTheme(next);
                applyTheme(next);
            });
        });
        applyTheme(root.dataset.theme || "light");

        document.querySelectorAll("[data-current-year]").forEach((node) => {
            node.textContent = new Date().getFullYear();
        });

        const progress = document.querySelector(".scroll-progress");
        const updateProgress = () => {
            if (!progress) return;
            const scrollable = document.documentElement.scrollHeight - window.innerHeight;
            const ratio = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
            progress.style.transform = `scaleX(${ratio})`;
        };
        updateProgress();
        window.addEventListener("scroll", updateProgress, { passive: true });

        const revealNodes = document.querySelectorAll(".reveal");
        if ("IntersectionObserver" in window) {
            const observer = new IntersectionObserver((entries, obs) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        obs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
            revealNodes.forEach((node) => observer.observe(node));
        } else {
            revealNodes.forEach((node) => node.classList.add("is-visible"));
        }

        document.querySelectorAll("[data-spotlight]").forEach((node) => {
            node.addEventListener("pointermove", (event) => {
                const rect = node.getBoundingClientRect();
                node.style.setProperty("--mx", `${((event.clientX - rect.left) / rect.width) * 100}%`);
                node.style.setProperty("--my", `${((event.clientY - rect.top) / rect.height) * 100}%`);
            });
        });

        window.setTimeout(() => {
            document.querySelectorAll(".toast").forEach((toast) => {
                toast.style.opacity = "0";
                toast.style.transform = "translateY(-8px)";
                toast.style.transition = "opacity 220ms ease, transform 220ms ease";
                window.setTimeout(() => toast.remove(), 240);
            });
        }, 3800);
    });
})();
