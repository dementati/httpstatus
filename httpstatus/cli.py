"""Command-line interface for printing HTTP status name and description."""

from __future__ import annotations

import argparse
import sys
from http import HTTPStatus

import llm_cli


def main(argv: list[str] | None = None) -> None:
    """Entry point for the CLI.

    Usage:
      httpstatus 200
      python -m httpstatus 404
    """
    parser = argparse.ArgumentParser(
        prog="httpstatus",
        description="Print the name and description for an HTTP status code.",
    )
    parser.add_argument("code", type=int, help="HTTP status code (e.g. 200, 404)")
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Print only the phrase"
    )
    args = parser.parse_args(argv)

    try:
        status = HTTPStatus(args.code)
    except ValueError:
        print(f"Unknown HTTP status code: {args.code}", file=sys.stderr)
        sys.exit(2)

    if args.quiet:
        print(status.phrase)
        return

    # Newer Python versions expose a longer `.description`; fall back to phrase.
    description = getattr(status, "description", "") or status.phrase

    details = llm_cli.query_llm(
        "You are a helpful assistant.",
        f"Provide a brief description for HTTP status code {status.value} - {status.phrase}.",
    )

    print(f"{status.value} {status.phrase}")
    if description:
        print()
        print(description)
        print()
        print(details)


if __name__ == "__main__":
    main()
