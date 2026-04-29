#!/usr/bin/env python3
"""
Build agent index from local clone of agency-agents repo.
Usage: python3 build-index.py [/path/to/local/clone]
"""

import json
import os
import re
import sys

CACHE_DIR = os.path.expanduser("~/.omc/agency-cache")
INDEX_FILE = os.path.join(CACHE_DIR, "agent-index.json")

AGENT_DIRS = [
    "academic", "design", "engineering", "finance",
    "game-development", "marketing", "paid-media", "product",
    "project-management", "sales", "spatial-computing", "specialized",
    "strategy/coordination", "support", "testing",
]


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a .md file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end < 0:
        return None
    fm = content[3:end].strip()
    result = {}
    for line in fm.split("\n"):
        m = re.match(r"^(\w[\w-]*):\s*(.+)$", line.strip())
        if m:
            result[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return result if result else None


def build_index(repo_root):
    repo_root = os.path.abspath(repo_root)
    if not os.path.isdir(repo_root):
        print(f"Error: {repo_root} is not a directory")
        sys.exit(1)

    index = []
    for cat in AGENT_DIRS:
        cat_dir = os.path.join(repo_root, cat)
        if not os.path.isdir(cat_dir):
            continue
        cat_name = cat.split("/")[0]
        for root, dirs, files in os.walk(cat_dir):
            for fname in sorted(files):
                if not fname.endswith(".md"):
                    continue
                if fname.startswith("README") or fname.startswith("EXECUTIVE") or fname.startswith("QUICKSTART"):
                    continue
                fpath = os.path.join(root, fname)
                rel_path = os.path.relpath(fpath, repo_root)
                fm = parse_frontmatter(fpath)
                if not fm:
                    continue
                entry = {
                    "name": fm.get("name", os.path.splitext(fname)[0]),
                    "description": fm.get("description", ""),
                    "category": cat_name,
                    "vibe": fm.get("vibe", ""),
                    "emoji": fm.get("emoji", ""),
                    "file_path": rel_path,
                }
                index.append(entry)

    index.sort(key=lambda x: x["name"].lower())

    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"Indexed {len(index)} agents -> {INDEX_FILE}")
    # Print summary by category
    cats = {}
    for e in index:
        cats.setdefault(e["category"], []).append(e)
    for c in sorted(cats):
        print(f"  {c}: {len(cats[c])} agents")

    return index


if __name__ == "__main__":
    repo_root = sys.argv[1] if len(sys.argv) > 1 else "/tmp/agency-agents"
    build_index(repo_root)
