#!/usr/bin/env python3
"""Legacy wrapper — prefer: python memory_cli.py search --query ..."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from memory_lib import search_episodes


def main() -> int:
    p = argparse.ArgumentParser(description="Search companion-memory episodes")
    p.add_argument("--root", default="memory", type=Path)
    p.add_argument("--query", required=True)
    p.add_argument("--wing", default=None)
    p.add_argument("--limit", type=int, default=8)
    args = p.parse_args()
    for h in search_episodes(args.root, args.query, wing=args.wing, limit=args.limit):
        print(f"{h.get('score', 0):.2f}\t{h.get('id')}\t{str(h.get('content', ''))[:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
