document.addEventListener("DOMContentLoaded", () => {
    window.setTimeout(() => {
        document.querySelectorAll(".dashboard-toast").forEach((toast) => {
            toast.style.opacity = "0";
            toast.style.transform = "translateY(-5px)";
            toast.style.transition = "opacity 180ms ease, transform 180ms ease";
            window.setTimeout(() => toast.remove(), 200);
        });
    }, 3200);
});
