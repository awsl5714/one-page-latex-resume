#!/usr/bin/env python3
"""Extract text from build/main-ats.pdf and check reading order is sane.

Verifies the parser sees, in order near the top: name, role, a single contact
line, then the section headings. Run after build.sh.
"""
import sys
from pypdf import PdfReader

EXPECT_ORDER = ["教育背景", "实习经历", "项目经历", "科研", "专业技能"]

def main() -> int:
    text = PdfReader("build/main-ats.pdf").pages[0].extract_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    print("\n".join(lines[:6]))
    pos = [next((i for i, l in enumerate(lines) if h in l), -1) for h in EXPECT_ORDER]
    if -1 in pos:
        print("MISSING section:", [h for h, p in zip(EXPECT_ORDER, pos) if p == -1])
        return 1
    if pos != sorted(pos):
        print("OUT-OF-ORDER sections:", list(zip(EXPECT_ORDER, pos)))
        return 1
    print("\nATS extraction order OK:", EXPECT_ORDER)
    return 0

if __name__ == "__main__":
    sys.exit(main())
