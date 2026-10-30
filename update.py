import re

# 1. READ INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Task 1: Move canvas
html = re.sub(r'\s*<canvas id="hero-canvas"></canvas>\n', '\n', html)
canvas_insert = '    <canvas id="three-canvas"></canvas>\n    <!-- Custom Cursor -->'
html = html.replace('<!-- Custom Cursor -->', canvas_insert)

# JS update
html = html.replace("document.getElementById('hero-canvas')", "document.getElementById('three-canvas')")

# Task 2: Insert Education before #projects
education_html = """
    <!-- ============ EDUCATION ============ -->
    <section id="education">
      <div class="work-header">
        <div>
          <div class="section-label reveal">Academic Background</div>
          <h2 class="section-title reveal scramble-target">EDUCATION</h2>
        </div>
      </div>
      <div class="edu-grid">

        <div class="edu-item reveal-scale reveal">
          <div class="edu-num">02</div>
          <div class="edu-icon">🎓</div>
          <div class="edu-tag">2024 – Present · New Delhi</div>
          <h3 class="edu-title">B.Tech CSE – Data Science</h3>
          <p class="edu-institution">Guru Gobind Singh Indraprastha University (GGSIPU)</p>
          <p class="edu-desc">Currently in First Year, specialising in Data Science and pursuing core Computer Science fundamentals alongside modern DS/AI coursework.</p>
          <div class="edu-badge">First Year · Ongoing</div>
        </div>

        <div class="edu-item reveal-scale reveal">
          <div class="edu-num">01</div>
          <div class="edu-icon">📚</div>
          <div class="edu-tag">Completed · New Delhi</div>
          <h3 class="edu-title">Class XII — CBSE Board</h3>
          <p class="edu-institution">Delhi, India</p>
          <p class="edu-desc">Completed Senior Secondary education under the Central Board of Secondary Education (CBSE), Delhi region.</p>
          <div class="edu-badge">CBSE · Completed</div>
        </div>

      </div>
    </section>

"""

html = html.replace('    <!-- ============ PROJECTS', education_html + '    <!-- ============ PROJECTS')

# Task 3: Replace Tech Stack
skills = [
("C", "Systems Programming"), ("C++", "Systems Programming"), ("CSS3", "Frontend"), ("HTML5", "Frontend"),
("Java", "Language"), ("JavaScript", "Language"), ("TypeScript", "Language"), ("Python", "Language"),
("Netlify", "Deployment"), ("Vercel", "Deployment"), ("Render", "Deployment"), ("Firebase", "Backend / BaaS"),
("FastAPI", "Backend"), ("Express.js", "Backend"), ("Flutter", "Mobile"), ("NPM", "Tooling"),
("Next.js", "Frontend"), ("Node.js", "Backend"), ("Socket.IO", "Realtime"), ("Svelte", "Frontend"),
("SvelteKit", "Frontend"), ("Three.js", "3D / Graphics"), ("TailwindCSS", "Styling"), ("OpenCV", "Computer Vision"),
("React Router", "Frontend"), ("MySQL", "Database"), ("MongoDB", "Database"), ("PostgreSQL", "Database"),
("Prisma", "ORM"), ("Supabase", "Database / BaaS"), ("Figma", "Design"), ("NumPy", "Data Science"),
("Pandas", "Data Science"), ("PyTorch", "ML / AI"), ("TensorFlow", "ML / AI"), ("Git", "Version Control"),
("GitHub", "Version Control"), ("GitHub Actions", "DevOps / CI-CD"), ("Arduino", "Hardware"),
("Home Assistant", "IoT"), ("Meta", "Platform / APIs"), ("Raspberry Pi", "Hardware"), ("React", "Frontend")
]

import random
random.seed(42)

skills_html = '<div class="skills-container">\n'
for name, cat in skills:
    pct = random.randint(70, 95)
    skills_html += f'''            <div class="skill-row reveal" data-skill="{pct}">
                <div class="skill-header">
                    <span class="skill-name">{name}</span>
                    <span class="skill-category">{cat}</span>
                </div>
                <div class="skill-bar-wrap">
                    <div class="skill-bar"></div>
                </div>
            </div>\n'''
skills_html += '        </div>'

# replace Bento Grid
html = re.sub(r'<div class="bento-grid">.*?</section>', skills_html + '\n    </section>', html, flags=re.DOTALL)

js_inject = """
        // Skill bar reveal
        gsap.utils.toArray('.skill-row').forEach(row => {
            const bar = row.querySelector('.skill-bar');
            let skillVal = row.getAttribute('data-skill');
            ScrollTrigger.create({
                trigger: row,
                start: 'top 85%',
                onEnter: () => { bar.style.width = skillVal + '%'; }
            });
        });

        // Add reveal-scale behavior just in case
        gsap.utils.toArray('.reveal-scale').forEach(el => {
            gsap.fromTo(el, 
                { opacity: 0, scale: 0.9, y: 30 },
                { opacity: 1, scale: 1, y: 0, duration: 1.2, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 85%' } }
            );
        });
"""

html = html.replace('    })();\n    </script>', js_inject + '\n    })();\n    </script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. READ STYLE.CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove #hero-canvas
css = re.sub(r'#hero-canvas\s*\{[^}]*\}', '', css)

# Append new styles
new_css = """

#three-canvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  width: 100vw;
  height: 100vh;
}
section, nav, footer {
    position: relative;
    z-index: 1;
}

#education {
  padding: 8rem 3rem;
  border-top: 1px solid rgba(240,235,225,.08);
  position: relative;
  z-index: 1;
}
.edu-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px;
  margin-top: 0;
}
.edu-item {
  position: relative;
  overflow: hidden;
  background: #111;
  padding: 3.5rem 3rem;
  border: 1px solid rgba(240,235,225,.06);
  transition: background .4s;
  cursor: default;
}
.edu-item:hover {
  background: rgba(201,74,43,.05);
}
.edu-item::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 2px;
  background: var(--rust);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .5s cubic-bezier(.16,1,.3,1);
}
.edu-item:hover::before {
  transform: scaleX(1);
}
.edu-num {
  font-family: var(--font-display);
  font-size: 5rem;
  color: rgba(240,235,225,.04);
  position: absolute;
  top: 1rem; right: 1.5rem;
  line-height: 1;
  pointer-events: none;
}
.edu-icon {
  font-size: 2rem;
  margin-bottom: 1.5rem;
}
.edu-tag {
  font-size: .65rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--rust);
  margin-bottom: .75rem;
}
.edu-title {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 2.5vw, 2.2rem);
  color: var(--cream);
  line-height: 1;
  margin-bottom: .75rem;
  letter-spacing: .02em;
}
.edu-institution {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 1rem;
  color: var(--gold, #FFD700);
  margin-bottom: 1.25rem;
}
.edu-desc {
  font-size: .82rem;
  line-height: 1.7;
  color: var(--muted, rgba(240,235,225,0.5));
  margin-bottom: 2rem;
}
.edu-badge {
  display: inline-block;
  padding: .4rem 1rem;
  border: 1px solid rgba(201,74,43,.4);
  font-size: .65rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--rust);
  font-family: var(--font-mono);
}
@media (max-width: 768px) {
  .edu-grid { grid-template-columns: 1fr; }
  #education { padding: 5rem 1.5rem; }
}

/* Custom Skills Styles */
.skills-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 4rem;
    row-gap: 2.5rem;
    padding-top: 3rem;
}
.skill-row {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}
.skill-name {
    font-family: var(--font-display);
    font-size: 1.5rem;
    color: var(--cream);
    letter-spacing: 1px;
}
.skill-category {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: rgba(240, 235, 225, 0.4);
    letter-spacing: 2px;
    text-transform: uppercase;
    float: right;
    margin-top: 0.5rem;
}
.skill-bar-wrap {
    width: 100%;
    height: 3px;
    background: rgba(240, 235, 225, 0.1);
    position: relative;
    border-radius: 2px;
    overflow: hidden;
}
.skill-bar {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: var(--rust);
    width: 0; /* Animated */
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}
@media (max-width: 768px) {
    .skills-container { grid-template-columns: 1fr; }
}
"""

css = css + new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Files updated successfully.")
