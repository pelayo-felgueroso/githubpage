
from pathlib import Path
import shutil
import subprocess
import sys

# ==================================================
# CONFIGURATION
# ==================================================

VAULT = Path(r"C:\Users\pelaf\Documents\Obsidian-vault")
REPO = Path(__file__).resolve().parent
CONTENT = REPO / "content"

WELCOME_NOTE = "Hi, I'm Pelayo. Welcome to my notes!.md"
WELCOME_TITLE = "Hi, I'm Pelayo. Welcome to my notes!"

EXCLUDED_DIRS = {
    ".obsidian",
    ".trash",
    "templates",
    "private",
    ".git",
}

EXCLUDED_FILES = {
    ".DS_Store",
}

# ==================================================
# HELPERS
# ==================================================

def run(command, cwd=REPO):
    print(f"\n> {' '.join(map(str, command))}")

    subprocess.run(
        command,
        cwd=cwd,
        check=True,
        shell=False
    )


def pull_latest():
    print("\n[1/6] Synchronizing repository with GitHub...")

    run(["git", "pull", "--ff-only", "origin", "main"])


def copy_vault():
    print("\n[2/6] Synchronizing Obsidian notes...")

    CONTENT.mkdir(parents=True, exist_ok=True)

    # Remove destination files that no longer exist
    # in the source vault, without touching excluded folders.
    for path in sorted(CONTENT.rglob("*"), reverse=True):
        relative = path.relative_to(CONTENT)

        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue

        source = VAULT / relative

        if path.is_file() and not source.is_file():
            path.unlink()

        elif path.is_dir() and not source.is_dir():
            shutil.rmtree(path)

    # Copy all allowed files from the public vault.
    for source in VAULT.rglob("*"):
        relative = source.relative_to(VAULT)

        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue

        if source.is_file():
            if source.name in EXCLUDED_FILES:
                continue

            # Homepage is handled separately.
            if source.name == WELCOME_NOTE:
                continue

            destination = CONTENT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)

            if (
                not destination.exists()
                or source.stat().st_mtime_ns != destination.stat().st_mtime_ns
                or source.stat().st_size != destination.stat().st_size
            ):
                shutil.copy2(source, destination)
                print(f"  Updated: {relative}")


def generate_homepage():
    print("\n[3/6] Generating homepage...")

    source = VAULT / WELCOME_NOTE

    if not source.exists():
        raise FileNotFoundError(
            f"Homepage note not found: {source}"
        )

    body = source.read_text(encoding="utf-8-sig")

    # Remove old frontmatter, if present.
    if body.startswith("---"):
        parts = body.split("---", 2)

        if len(parts) == 3:
            body = parts[2].lstrip("\r\n")

    # Remove duplicate H1.
    lines = body.splitlines()

    if lines and lines[0].strip() == f"# {WELCOME_TITLE}":
        lines = lines[1:]

    body = "\n".join(lines).strip()

    homepage = (
        "---\n"
        f'title: "{WELCOME_TITLE}"\n'
        "---\n\n"
        f"{body}\n"
    )

    (CONTENT / "index.md").write_text(
        homepage,
        encoding="utf-8"
    )


def build_website():
    print("\n[4/6] Building Quartz...")

    run(["npx.cmd", "quartz", "build"])


def publish_git():
    print("\n[5/6] Publishing to GitHub...")

    run(["git", "add", "content"])

    # Only commit content changes.
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=REPO
    )

    if result.returncode == 0:
        print("No changes to publish.")
        return

    if result.returncode != 1:
        raise RuntimeError("Could not check Git changes.")

    run([
        "git",
        "commit",
        "-m",
        "Update Obsidian notes"
    ])

    run(["git", "push", "origin", "main"])


# ==================================================
# MAIN
# ==================================================

def main():
    print("\n===================================")
    print("       OBSIDIAN WEBSITE UPDATE")
    print("===================================")

    if not VAULT.is_dir():
        raise FileNotFoundError(f"Vault not found: {VAULT}")

    if not (REPO / ".git").is_dir():
        raise FileNotFoundError("Git repository not found.")

    if not (REPO / "package.json").is_file():
        raise FileNotFoundError("Quartz package.json not found.")

    if not (REPO / "node_modules").is_dir():
        raise FileNotFoundError(
            "node_modules not found. Run npm install first."
        )

    # Check that the repository is clean before pulling.
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True
    ).stdout.strip()

    if status:
        raise RuntimeError(
            "You have uncommitted changes in the repository. "
            "Commit or stash them before publishing."
        )

    # Make sure we are on main.
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True
    ).stdout.strip()

    if branch != "main":
        raise RuntimeError(
            f"You are on branch '{branch}', not 'main'. "
            "Switch to main before publishing."
        )

    pull_latest()

    copy_vault()
    generate_homepage()
    build_website()
    publish_git()

    print("\n[6/6] Done!")
    print("GitHub Pages deployment has been triggered.")
    print("https://pelayo-felgueroso.github.io/githubpage/")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"\nERROR: {error}")
        sys.exit(1)

