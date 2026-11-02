"""Keep maintenance release drafts separate by app and locale within a project."""

import argparse
import json
import sqlite3
import unicodedata
from pathlib import Path


def wording_key(text):
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return "".join(char for char in normalized if char.isalnum())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("recent", "remember"))
    parser.add_argument("--db", type=Path, default=Path(".whats-new/history.sqlite3"))
    parser.add_argument("--app", default="default")
    parser.add_argument("--locale", default="en")
    parser.add_argument("--text", help="One full draft to remember")
    args = parser.parse_args()
    scope = (args.app.strip().casefold(), args.locale.strip().replace("_", "-").lower())

    if args.action == "recent" and not args.db.exists():
        print("[]")
        return 0
    if args.action == "remember":
        if not args.text or not wording_key(args.text):
            parser.error("remember requires a nonempty draft with words")
        args.db.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(args.db) as db:
        if args.action == "recent":
            rows = db.execute(
                "SELECT draft FROM drafts WHERE app = ? AND locale = ? "
                "ORDER BY rowid DESC LIMIT 8", scope
            )
            print(json.dumps([row[0] for row in rows], ensure_ascii=False))
            return 0
        db.execute(
            "CREATE TABLE IF NOT EXISTS drafts (app TEXT, locale TEXT, "
            "wording TEXT, draft TEXT, UNIQUE(app, locale, wording))"
        )
        inserted = db.execute(
            "INSERT INTO drafts VALUES (?, ?, ?, ?) ON CONFLICT DO NOTHING",
            (*scope, wording_key(args.text), args.text.strip()),
        )
        if not inserted.rowcount:
            print("duplicate")
            return 1
    print("saved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
