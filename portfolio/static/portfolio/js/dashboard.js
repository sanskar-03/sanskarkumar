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

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector(".cms-form");

    if (!form) return;


    /* =====================================================
       DIRTY STATE
       ===================================================== */

    let dirty = false;

    const state = document.querySelector("#formState");

    form.querySelectorAll("input, textarea, select").forEach((field) => {

        field.addEventListener("input", () => {

            dirty = true;

            if (state) {
                state.textContent = "Unsaved";
            }
        });

    });


    form.addEventListener("submit", () => {

        dirty = false;

        if (state) {
            state.textContent = "Saving…";
        }

    });


    window.addEventListener("beforeunload", (event) => {

        if (!dirty) return;

        event.preventDefault();
        event.returnValue = "";

    });


    /* =====================================================
       PROJECT SLUG
       ===================================================== */

    const title = form.querySelector("#id_title");
    const slug = form.querySelector("#id_slug");

    if (title && slug) {

        let manuallyEdited = false;

        slug.addEventListener("input", () => {
            manuallyEdited = true;
        });

        title.addEventListener("input", () => {

            if (manuallyEdited) return;

            slug.value = title.value
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9]+/g, "-")
                .replace(/^-+|-+$/g, "");

        });

    }


    /* =====================================================
       TECH STACK TAG PREVIEW
       ===================================================== */

    const techInput = form.querySelector("#id_tech_stack");
    const techPreview = form.querySelector('[data-source="tech_stack"]');

    const renderTags = () => {

        if (!techInput || !techPreview) return;

        techPreview.innerHTML = "";

        const values = techInput.value
            .split(/[,\n]+/)
            .map(item => item.trim())
            .filter(Boolean);

        [...new Set(values)].forEach((value) => {

            const tag = document.createElement("span");

            tag.className = "tech-tag";

            tag.textContent = value;

            techPreview.appendChild(tag);

        });

    };

    if (techInput) {

        renderTags();

        techInput.addEventListener("input", renderTags);

    }


    /* =====================================================
       IMAGE PREVIEW
       ===================================================== */

    const imageInput =
        form.querySelector("#id_image_upload") ||
        form.querySelector("#id_profile_image_upload");

    if (imageInput) {

        imageInput.addEventListener("change", () => {

            const file = imageInput.files?.[0];

            if (!file) return;

            const allowed = [
                "image/jpeg",
                "image/png",
                "image/webp",
                "image/gif"
            ];

            if (!allowed.includes(file.type)) {

                alert("Please upload JPG, PNG, WEBP or GIF.");

                imageInput.value = "";

                return;

            }

            if (file.size > 5 * 1024 * 1024) {

                alert("Image must be smaller than 5 MB.");

                imageInput.value = "";

                return;

            }

            let preview = form.querySelector(".upload-live-preview");

            if (!preview) {

                preview = document.createElement("div");

                preview.className = "media-preview upload-live-preview";

                imageInput.closest(".upload-zone")?.after(preview);

            }

            const img = document.createElement("img");

            img.src = URL.createObjectURL(file);

            img.alt = "Selected image preview";

            preview.replaceChildren(img);

        });

    }


    /* =====================================================
       SKILL RANGE
       ===================================================== */

    const skillRange = form.querySelector("#id_level");

    const skillOutput =
        document.querySelector("#skillLevelValue");

    if (skillRange && skillOutput) {

        const syncRange = () => {

            skillOutput.value = `${skillRange.value}%`;

        };

        syncRange();

        skillRange.addEventListener("input", syncRange);

    }


    /* =====================================================
       URL VALIDATION
       ===================================================== */

    form.querySelectorAll('input[type="url"]').forEach((input) => {

        input.addEventListener("blur", () => {

            if (!input.value.trim()) return;

            try {

                new URL(input.value);

                input.removeAttribute("aria-invalid");

            } catch {

                input.setAttribute("aria-invalid", "true");

            }

        });

    });


    /* =====================================================
       TOASTS
       ===================================================== */

    window.setTimeout(() => {

        document
            .querySelectorAll(".dashboard-toast")
            .forEach((toast) => {

                toast.style.opacity = "0";
                toast.style.transform = "translateY(-5px)";
                toast.style.transition =
                    "opacity 180ms ease, transform 180ms ease";

                window.setTimeout(
                    () => toast.remove(),
                    200
                );

            });

    }, 3200);

});
