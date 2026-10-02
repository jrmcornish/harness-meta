#!/usr/bin/env python3
"""Print what Rob typed in Claude Code sessions, oldest first.

Usage: user_messages.py [--since YYYY-MM-DD] [--max-chars N] PATH...

PATH is a transcript (.jsonl) or a folder of them, such as one project's
folder under ~/.claude/projects/. Transcripts are large and mostly tool
output; this prints only the user's own messages, each with its time and
session, so a session's worth of work can be read in a few pages.
"""
import argparse
import json
import pathlib

# Text that arrives in a "user" turn but was not typed by the user.
NOT_TYPED = (
    "<system-reminder",
    "<task-notification",
    "<local-command",
    "<command-name>",
    "Caveat:",
    "This session is being continued",
    "[Request interrupted",
    "Another Claude session sent a message",
    "[SYSTEM NOTIFICATION",
)


def texts(record):
    content = record.get("message", {}).get("content")
    if isinstance(content, str):
        yield content
    elif isinstance(content, list):
        for part in content:
            if isinstance(part, dict) and part.get("type") == "text":
                yield part.get("text", "")


def user_messages(path, since):
    with open(path, errors="replace") as f:
        for line in f:
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if record.get("type") != "user" or record.get("isSidechain") or record.get("isMeta"):
                continue
            stamp = record.get("timestamp", "")
            if since and stamp[:10] < since:
                continue
            for text in texts(record):
                text = text.strip()
                if text and not text.startswith(NOT_TYPED):
                    yield stamp, text


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", type=pathlib.Path, metavar="PATH")
    parser.add_argument("--since", help="only messages on or after this date")
    parser.add_argument("--max-chars", type=int, default=1500, help="cut each message to this length")
    args = parser.parse_args()

    files = []
    for path in args.paths:
        files += sorted(path.glob("*.jsonl")) if path.is_dir() else [path]

    found = []
    for file in files:
        for stamp, text in user_messages(file, args.since):
            found.append((stamp, file.stem[:8], text))

    for stamp, session, text in sorted(found):
        print(f"\n### {stamp[:16]} [{session}]\n{text[:args.max_chars]}")
    print(f"\n{len(found)} messages from {len(files)} transcripts")


if __name__ == "__main__":
    main()
