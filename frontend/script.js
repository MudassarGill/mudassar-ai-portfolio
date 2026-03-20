const titles = ["AI/ML Engineer", "Deep Learning", "Data Science", "Generative AI", "MLOps", "LLMs & RAG Systems", "AI Agents"];
const typeTextSpan = document.querySelector(".type-text");
let textIdx = 0;
let charIdx = 0;
let isDeleting = false;

function type() {
    const currentTitle = titles[textIdx];
    if (isDeleting) {
        typeTextSpan.textContent = currentTitle.substring(0, charIdx - 1);
        charIdx--;
    } else {
        typeTextSpan.textContent = currentTitle.substring(0, charIdx + 1);
        charIdx++;
    }

    let typeSpeed = isDeleting ? 50 : 100;

    if (!isDeleting && charIdx === currentTitle.length) {
        typeSpeed = 2000; // Pause at end
        isDeleting = true;
    } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        textIdx = (textIdx + 1) % titles.length;
        typeSpeed = 500; // Pause before new word
    }
    setTimeout(type, typeSpeed);
}

document.addEventListener("DOMContentLoaded", () => {
    // Start typing effect
    if(typeTextSpan) type();
    
    // Fetch Projects
    fetchProjects();

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if(menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
             navLinks.classList.remove('active');
        });
    });

    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            const statusDiv = document.getElementById('form-status');
            const submitBtn = contactForm.querySelector('.submit-btn');
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin"></i>';

            try {
                // Pointing to FastAPI local server endpoint
                const response = await fetch('http://127.0.0.1:8000/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, email, message })
                });

                if (response.ok) {
                    statusDiv.textContent = "Message sent successfully! I'll get back to you soon.";
                    statusDiv.className = "form-status status-success";
                    contactForm.reset();
                } else {
                    const data = await response.json();
                    statusDiv.textContent = data.detail || "Failed to send message. Please try again later.";
                    statusDiv.className = "form-status status-error";
                }
            } catch (error) {
                statusDiv.textContent = "Error connecting to server. Is the backend running on port 8000?";
                statusDiv.className = "form-status status-error";
                console.error('Error:', error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Send Message</span> <i class="fas fa-paper-plane"></i>';
            }
        });
    }
});

async function fetchProjects() {
    const container = document.getElementById('projects-container');
    try {
        const response = await fetch('http://127.0.0.1:8000/projects');
        if (!response.ok) throw new Error("Failed to fetch");
        
        const projects = await response.json();
        container.innerHTML = ''; // Clear loading
        
        projects.forEach(project => {
            const card = document.createElement('div');
            card.className = 'project-card glass-card';
            card.innerHTML = `
                <img src="${project.image_url || 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500&q=80'}" alt="${project.title}" class="project-img" loading="lazy">
                <div class="project-info">
                    <h3>${project.title}</h3>
                    <p>${project.description}</p>
                    <div class="project-tags">${project.tech_stack}</div>
                    <a href="${project.github_link}" class="btn secondary-btn" target="_blank" style="padding: 0.5rem 1rem; font-size: 0.9rem; text-align: center;">View Github</a>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (error) {
        console.error("Error fetching projects:", error);
        container.innerHTML = '<p style="color:red; text-align: center; width: 100%;">Error loading projects. Ensure the FastAPI backend is running.</p>';
    }
}
