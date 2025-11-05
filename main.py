"""Backward-compatible script entry point.

This module delegates to the `httpstatus` package so running
`python main.py 200` will work during development.
"""

from __future__ import annotations

import sys
from httpstatus.cli import main


if __name__ == "__main__":
    # pass command-line args (skip script name)
    main(sys.argv[1:])
