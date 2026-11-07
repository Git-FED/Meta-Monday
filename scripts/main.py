"""CLI entry point for planning-only Black Friday/Cyber Monday research."""

import argparse
import json
from pathlib import Path

from cyber_monday_check import compare_prices
from verify_deal import verify_deal
from worker_split import plan_as_dicts


def main() -> int:
    parser = argparse.ArgumentParser(description="Muse AI Black Monday planning toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="create assignments; never dispatches workers")
    plan.add_argument("--mode", choices=["broad", "item"], required=True)
    plan.add_argument("--category", required=True)
    plan.add_argument("--workers", type=int, default=50)
    plan.add_argument("--item")

    verify = sub.add_parser("verify", help="verify a JSON deal record")
    verify.add_argument("--deal-json", type=Path, required=True)

    compare = sub.add_parser("compare", help="compare baseline and Cyber Monday JSON records")
    compare.add_argument("--baseline", type=Path, required=True)
    compare.add_argument("--cyber", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "plan":
        print(json.dumps({"dispatch": False, "assignments": plan_as_dicts(args.mode, args.category, args.workers, args.item)}, indent=2))
    elif args.command == "verify":
        print(json.dumps(verify_deal(json.loads(args.deal_json.read_text())), indent=2))
    elif args.command == "compare":
        print(json.dumps(compare_prices(json.loads(args.baseline.read_text()), json.loads(args.cyber.read_text())), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
