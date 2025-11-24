// script.js

document.addEventListener("DOMContentLoaded", () => {

    // ===== Animate elements on scroll =====
    const fadeElements = document.querySelectorAll(".info-box, h1, h2, .photo, table");

    const fadeInOnScroll = () => {
        const windowBottom = window.innerHeight + window.scrollY;
        fadeElements.forEach(el => {
            const elementTop = el.offsetTop + 50;
            if (windowBottom > elementTop) {
                el.style.opacity = 1;
                el.style.transform = "translateY(0)";
            }
        });
    };

    fadeElements.forEach(el => {
        el.style.opacity = 0;
        el.style.transform = "translateY(40px)";
        el.style.transition = "all 0.8s ease-out";
    });

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll();

    // ===== Dark/Light Mode Toggle =====
    const toggleBtn = document.createElement("button");
    toggleBtn.textContent = "🌙 Dark Mode";
    toggleBtn.style.position = "fixed";
    toggleBtn.style.top = "20px";
    toggleBtn.style.right = "20px";
    toggleBtn.style.padding = "10px 14px";
    toggleBtn.style.cursor = "pointer";
    toggleBtn.style.borderRadius = "6px";
    toggleBtn.style.border = "none";
    toggleBtn.style.backgroundColor = "navy";
    toggleBtn.style.color = "#fff";
    toggleBtn.style.zIndex = "1000";
    document.body.appendChild(toggleBtn);

    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        toggleBtn.textContent = document.body.classList.contains("dark-mode") ? "☀️ Light Mode" : "🌙 Dark Mode";
    });

    // ===== Typing Animation for About Me =====
    const aboutText = document.querySelector("#about p");
    const fullText = aboutText.textContent;
    aboutText.textContent = "";
    let i = 0;

    const typeWriter = () => {
        if (i < fullText.length) {
            aboutText.textContent += fullText[i];
            i++;
            setTimeout(typeWriter, 30);
        }
    };
    typeWriter();

    // ===== Smooth Section Navigation =====
    const nav = document.createElement("nav");
    nav.style.position = "fixed";
    nav.style.top = "0";
    nav.style.left = "0";
    nav.style.width = "100%";
    nav.style.backgroundColor = "rgba(255,255,255,0.95)";
    nav.style.display = "flex";
    nav.style.justifyContent = "center";
    nav.style.padding = "12px 0";
    nav.style.zIndex = "999";
    nav.style.boxShadow = "0 2px 8px rgba(0,0,0,0.1)";

    nav.innerHTML = `
        <a href="#about" style="margin:0 15px; color:navy; text-decoration:none;">About</a>
        <a href="#skills" style="margin:0 15px; color:navy; text-decoration:none;">Skills</a>
        <a href="#projects" style="margin:0 15px; color:navy; text-decoration:none;">Projects</a>
        <a href="#contact" style="margin:0 15px; color:navy; text-decoration:none;">Contact</a>
    `;
    document.body.prepend(nav);

    document.querySelectorAll("nav a").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute("href"));
            target.scrollIntoView({ behavior: "smooth" });
        });
    });

    // ===== Hover Effects =====
    // Info boxes
    const infoBoxes = document.querySelectorAll(".info-box");
    infoBoxes.forEach(box => {
        box.style.transition = "all 0.3s ease";
        box.addEventListener("mouseenter", () => {
            box.style.transform = "translateY(-5px)";
            box.style.boxShadow = "0 8px 20px rgba(0,0,0,0.15)";
        });
        box.addEventListener("mouseleave", () => {
            box.style.transform = "translateY(0)";
            box.style.boxShadow = "0 4px 10px rgba(0,0,0,0.1)";
        });
    });

    // Projects list items
    const projectList = document.querySelectorAll("#projects ul li");
    projectList.forEach(item => {
        item.style.transition = "all 0.3s ease";
        item.addEventListener("mouseenter", () => {
            item.style.color = "#3498db";
            item.style.fontWeight = "600";
        });
        item.addEventListener("mouseleave", () => {
            item.style.color = "";
            item.style.fontWeight = "normal";
        });
    });

    // Skills table cells
    const skillCells = document.querySelectorAll("#skills table td:nth-child(2)");
    skillCells.forEach(cell => {
        const skillLevel = cell.textContent.toLowerCase();
        let color = "lightgray";
        if (skillLevel === "beginner") color = "#f39c12";
        if (skillLevel === "learning") color = "#3498db";
        if (skillLevel === "good") color = "#2ecc71";

        cell.style.backgroundColor = color;
        cell.style.color = "#fff";
        cell.style.fontWeight = "600";
        cell.style.textAlign = "center";
        cell.style.transition = "all 0.3s ease";

        cell.addEventListener("mouseenter", () => {
            cell.style.transform = "scale(1.05)";
            cell.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";
        });
        cell.addEventListener("mouseleave", () => {
            cell.style.transform = "scale(1)";
            cell.style.boxShadow = "none";
        });
    });

    // ===== Contact Form Validation =====
    const form = document.querySelector("form");
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const name = form.querySelector('input[type="text"]').value.trim();
        const email = form.querySelector('input[type="email"]').value.trim();
        const message = form.querySelector('textarea').value.trim();

        if (!name || !email || !message) {
            alert("Please fill in all fields before sending your message!");
        } else {
            alert(`Thank you ${name}! Your message has been sent.`);
            form.reset();
        }
    });

    // ===== Back to Top Button =====
    const topBtn = document.createElement("button");
    topBtn.textContent = "↑ Top";
    topBtn.style.position = "fixed";
    topBtn.style.bottom = "30px";
    topBtn.style.right = "30px";
    topBtn.style.padding = "12px 18px";
    topBtn.style.fontSize = "16px";
    topBtn.style.borderRadius = "8px";
    topBtn.style.border = "none";
    topBtn.style.backgroundColor = "navy";
    topBtn.style.color = "#fff";
    topBtn.style.cursor = "pointer";
    topBtn.style.display = "none";
    topBtn.style.zIndex = "1000";
    document.body.appendChild(topBtn);

    topBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) topBtn.style.display = "block";
        else topBtn.style.display = "none";
    });

});
