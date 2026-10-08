"""Command line entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import catalog
from .planner import build_plan, render_markdown, to_csv


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cert-path",
                                 description="Standards map, test sequence and timeline for a hardware product")
    ap.add_argument("product", nargs="?", choices=sorted(catalog.PRODUCTS))
    ap.add_argument("--markets", default="us", help="comma list: us,eu (default us)")
    ap.add_argument("--option", action="append", default=[], choices=catalog.OPTION_FLAGS,
                    help="add optional scope; repeat for several")
    ap.add_argument("-o", "--out", type=Path, help="write markdown report")
    ap.add_argument("--csv", type=Path, help="write the plan as CSV (for a project tool)")
    ap.add_argument("--list", action="store_true", help="list product types and exit")
    args = ap.parse_args(argv)

    if args.list or not args.product:
        for k, v in catalog.PRODUCTS.items():
            print(f"{k:22} {v['label']}")
        return 0
    try:
        plan = build_plan(args.product, args.markets.split(","), args.option)
    except (KeyError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    report = render_markdown(plan)
    if args.out:
        args.out.write_text(report)
    if args.csv:
        args.csv.write_text(to_csv(plan))
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
