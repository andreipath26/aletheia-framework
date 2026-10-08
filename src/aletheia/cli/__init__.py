"""Command-line entry point for Aletheia Framework.

The CLI is a stub in the skeleton phase. Implementation lands in Milestone 1
alongside the IPP SDK and the local core.
"""

import sys

USAGE = """\
aletheia — the advisor framework

Usage:
    aletheia --version    print the version and exit
    aletheia --help       print this message and exit

The CLI is a stub in the skeleton phase. Implementation lands in Milestone 1.
"""


def main(argv: list[str] | None = None) -> int:
    """Entry point referenced by pyproject.toml [project.scripts]."""
    args = sys.argv[1:] if argv is None else argv

    if not args or args[0] in ("--help", "-h"):
        print(USAGE, end="")
        return 0

    if args[0] in ("--version", "-V"):
        from aletheia import __version__

        print(f"aletheia {__version__}")
        return 0

    print(f"unknown argument: {args[0]}", file=sys.stderr)
    print(USAGE, end="", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
