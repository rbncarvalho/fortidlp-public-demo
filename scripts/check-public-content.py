#!/usr/bin/env python3
"""Heuristic pre-publication scanner. This does not replace manual review."""
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent.parent
FILES = [p for p in BASE.rglob("*") if p.is_file() and ".git" not in p.parts]
PATTERNS = {
    "azure-subscription-guid": re.compile(r"\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b"),
    "tenant-domain": re.compile(r"\b[a-z0-9-]+(?:\.onmicrosoft\.com|\.sharepoint\.com)\b", re.I),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "public-ip": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "api-token": re.compile(r"(?:ghp_|github_pat_|eyJ[A-Za-z0-9_-]{20,})"),
    "auth-header": re.compile(r"Authorization\s*:\s*(?:Bearer|Basic)", re.I),
    "windows-user-path": re.compile(r"C:\\Users\\(?!<LAB_USER>|%USERNAME%)[^\\\s<>]+", re.I),
}
ALLOW_IPS = {"192.0.2.10", "192.0.2.0", "198.51.100.0", "203.0.113.0"}
ALLOW_EMAILS = {"user@example.invalid", "contact@example.invalid"}
errors = []
for p in FILES:
    if p.suffix.lower() not in {".md",".txt",".py",".ps1",".json",".yml",".yaml",".sh"}:
        continue
    s = p.read_text(encoding="utf-8", errors="replace")
    for key, regex in PATTERNS.items():
        for m in regex.finditer(s):
            token = m.group(0)
            if key == "public-ip" and token in ALLOW_IPS: continue
            if key == "email" and token.lower() in ALLOW_EMAILS: continue
            if p.name == "check-public-content.py": continue
            errors.append((str(p.relative_to(BASE)), key, token[:40]))
if errors:
    print("Review possible sensitive content:")
    for path,key,val in errors: print(f"  {path}: {key}: {val}")
    sys.exit(1)
print(f"OK: scanned {len(FILES)} files; no heuristic findings.")
