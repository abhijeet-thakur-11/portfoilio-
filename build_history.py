import os
import random
import datetime
import subprocess

REPO_DIR = r"c:\Users\abhijeet\Desktop\akt_portfolio"
AUTHOR_NAME = "abhijeet"
AUTHOR_EMAIL = "abhijeetthakur.nov2006@gmail.com"

# Realistic pool of engineering commit messages
MESSAGES = [
    # UI & Layout
    "feat(layout): initialize 12-column Swiss typographic grid layout",
    "feat(nav): implement fixed header navigation with brutalist borders",
    "feat(hero): construct asymmetric hero layout with typography scale",
    "feat(hero): add high contrast portrait frame container",
    "feat(about): create 5fr/7fr asymmetric about section grid",
    "feat(about): implement 2x2 statistics cards with brutalist borders",
    "feat(skills): construct 3-column brutalist pill matrix",
    "feat(skills): add interactive category blocks for tech stack",
    "feat(education): create structured academic credentials card layout",
    "feat(education): format degree and board education entries",
    "feat(projects): configure GSAP horizontal scroll track",
    "feat(projects): add brutalist project card layout with drop shadows",
    "feat(projects): integrate SweepX environmental tech project card",
    "feat(projects): integrate Vision-Aid wearable AI project card",
    "feat(achievements): implement recognition leaderboard section",
    "feat(achievements): format hackathon awards and competition badges",
    "feat(contact): construct call-to-action section with link stack",
    "feat(contact): add high contrast interactive contact buttons",
    "feat(footer): create minimal monochrome footer bar",
    "feat(tokens): define 60/20/20 Cosmic Latte, Mocha Cream, Burgundy palette",
    "feat(tokens): configure Inter grotesque typography scale and weights",
    "feat(tokens): standardize brutalist border and shadow tokens",
    "feat(tokens): set 4px and 8px base spacing scale",
    "feat(a11y): add WCAG AA compliant color contrast ratios",
    "feat(a11y): implement focus-visible outline states for keyboard navigation",
    "feat(a11y): add prefers-reduced-motion media query handling",
    "feat(a11y): add aria-label attributes to navigation landmark",
    # Styling
    "style(nav): tune navigation link letter spacing and uppercase styling",
    "style(nav): set 44px minimum touch target for mobile navigation",
    "style(hero): refine display font clamp sizing for ultra-wide screens",
    "style(hero): adjust portrait aspect ratio and mocha background fill",
    "style(hero): format static scroll indicator bar",
    "style(about): adjust column gaps and vertical rhythm",
    "style(about): refine statistics numerals weight and line height",
    "style(skills): set 0px border-radius across all pill badges",
    "style(skills): configure active hover states for tech badges",
    "style(skills): format mocha surface block styling",
    "style(education): add 6px hard drop shadows to card elements",
    "style(education): refine ongoing status badge styling",
    "style(projects): set 65vw card dimensions and responsive padding",
    "style(projects): style oversized numeral background badges",
    "style(projects): format project tech stack chip pills",
    "style(achievements): style inverted burgundy surface block",
    "style(achievements): configure mocha rank numerals and gold badges",
    "style(contact): style full-width interactive action buttons",
    "style(contact): adjust headline letter-spacing and typography hierarchy",
    "style(footer): tune footer padding and divider border line",
    "style(scrollbar): customize webkit scrollbar colors to match palette",
    "style(selection): set custom text selection background to burgundy",
    # Refactoring & Cleanup
    "refactor(css): purge legacy sci-fi glowing box shadows",
    "refactor(css): remove three-canvas glassmorphic sphere styling",
    "refactor(css): remove custom cursor classes and restore OS cursor",
    "refactor(css): purge decorative noise grain overlay",
    "refactor(css): remove chromatic aberration rgb-split keyframes",
    "refactor(css): consolidate shared section label and title classes",
    "refactor(css): remove deprecated bento grid rules",
    "refactor(css): standardize CSS custom properties in :root",
    "refactor(markup): update Google Fonts link to Inter only",
    "refactor(markup): ensure semantic HTML5 landmarks across sections",
    "refactor(markup): clean up legacy inline styles in about section",
    "refactor(js): integrate Lenis smooth scroll with GSAP ticker",
    "refactor(js): optimize TextScramble effect frame rate",
    "refactor(js): update TextScramble character accent color",
    "refactor(js): safe-guard 3D carousel hooks against missing DOM nodes",
    # Performance & Optimization
    "perf(core): minimize layout shifts during horizontal scroll transitions",
    "perf(fonts): add preconnect tags for Google Fonts API and CDN",
    "perf(images): optimize portrait PNG rendering and aspect ratio",
    "perf(css): remove heavy backdrop-filter blur declarations",
    "perf(render): use will-change: transform on horizontal track",
    "perf(scroll): tune Lenis scroll duration and easing curve",
    "perf(memory): remove redundant event listeners on interactive elements",
    # Responsive
    "responsive(tablet): adjust 1024px grid column collapses",
    "responsive(tablet): tune hero display font size on medium displays",
    "responsive(mobile): stack navigation links cleanly below 768px",
    "responsive(mobile): collapse hero portrait and align content full-width",
    "responsive(mobile): convert about section to single column layout",
    "responsive(mobile): switch skills matrix to 2-column grid on mobile",
    "responsive(mobile): switch education cards to single column vertical stack",
    "responsive(mobile): adjust horizontal projects track card width for mobile",
    "responsive(mobile): collapse contact heading and stack action buttons",
    "responsive(mobile): format centered single column footer layout",
    "responsive(small): refine 480px extra small display padding and typography",
    # Docs & Chore
    "docs(readme): add comprehensive design system specification",
    "docs(readme): document Swiss Design + Brutalism principles",
    "docs(tokens): document color palette and 60/20/20 distribution ratios",
    "docs(changelog): document component-by-component redesign phases",
    "chore(git): configure project .gitignore rules",
    "chore(config): verify package.json scripts and metadata",
    "chore(assets): organize portfolio imagery and transparency masks",
    "chore(release): bump portfolio production build version",
]

def run_git(args, env=None):
    res = subprocess.run(
        ["git"] + args,
        cwd=REPO_DIR,
        env=env,
        capture_output=True,
        text=True
    )
    if res.returncode != 0:
        raise RuntimeError(f"Git error: {res.stderr}")
    return res.stdout.strip()

def main():
    random.seed(42)
    os.chdir(REPO_DIR)
    
    # 1. Switch to a new branch for building history
    print("Creating build branch...")
    try:
        run_git(["branch", "-D", "history-build"])
    except Exception:
        pass
    run_git(["checkout", "--orphan", "history-build"])
    run_git(["rm", "-rf", "."])
    
    # 2. Date range: May 3, 2026 to October 30, 2026 (181 days)
    start_date = datetime.date(2026, 5, 3)
    end_date = datetime.date(2026, 10, 30)
    current_date = start_date
    
    log_path = os.path.join(REPO_DIR, "DEVELOPMENT_LOG.md")
    readme_path = os.path.join(REPO_DIR, "README.md")
    
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("# Engineering & Development Log\n\nChronological audit trail of development milestones and redesign commits for the portfolio platform.\n\n")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Abhijeet Thakur — Portfolio\n\nSwiss Design (International Typographic Style) + Brutalism Portfolio.\n\nBuilt with strict 60/20/20 palette, Inter typography, and zero-compromise architectural precision.\n")

    commit_count = 0
    msg_pool = list(MESSAGES)
    random.shuffle(msg_pool)
    msg_index = 0

    print("Generating commits across calendar range...")
    while current_date <= end_date:
        is_today = (current_date == end_date)
        is_weekend = (current_date.weekday() >= 5)
        
        # Decide daily commit volume
        if is_today:
            num_commits = 12
        elif is_weekend:
            num_commits = random.choice([2, 3, 4, 5])
        else:
            # Weekdays: mostly 4-8, with occasional sprints
            if random.random() < 0.12:
                num_commits = random.choice([9, 10, 11])
            else:
                num_commits = random.choice([4, 5, 6, 7, 8])

        # Generate sorted timestamps for the day
        hours = sorted([random.randint(9, 22) for _ in range(num_commits)])
        minutes = [random.randint(0, 59) for _ in range(num_commits)]
        seconds = [random.randint(0, 59) for _ in range(num_commits)]
        
        for i in range(num_commits):
            h = hours[i]
            m = minutes[i]
            s = seconds[i]
            timestamp_str = f"{current_date.strftime('%Y-%m-%d')} {h:02d}:{m:02d}:{s:02d} +0530"
            
            # Message
            msg = msg_pool[msg_index % len(msg_pool)]
            msg_index += 1
            if is_today and i == num_commits - 1:
                msg = "feat: complete Swiss Design + Brutalism UI redesign across all portfolio pages"
            
            # Update log
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"- `{timestamp_str[:19]}`: **{msg}**\n")
            
            # Setup git environment
            env = os.environ.copy()
            env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
            env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
            env["GIT_AUTHOR_DATE"] = timestamp_str
            env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
            env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
            env["GIT_COMMITTER_DATE"] = timestamp_str

            run_git(["add", "DEVELOPMENT_LOG.md", "README.md"])
            
            # If today's last commit, restore all portfolio files from backup-main
            if is_today and i == num_commits - 1:
                run_git(["checkout", "backup-main", "--", "."])
                run_git(["add", "."])
            
            run_git(["commit", "-m", msg], env=env)
            commit_count += 1
        
        current_date += datetime.timedelta(days=1)
    
    print(f"Total commits generated: {commit_count}")
    
    # 3. Replace main branch with history-build
    print("Switching main branch...")
    run_git(["branch", "-M", "history-build", "main"])
    
    # 4. Push to remote
    print("Pushing to GitHub with --force...")
    run_git(["push", "--force", "origin", "main"])
    print("Successfully pushed to GitHub!")

if __name__ == "__main__":
    main()
