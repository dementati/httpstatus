"""Make the package runnable with `python -m httpstatus`."""

from __future__ import annotations

from .cli import main
import sys


if __name__ == "__main__":
    main(sys.argv[1:])
