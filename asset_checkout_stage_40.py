# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: AssetCheckout
def main():
    parser = argparse.ArgumentParser(description="AssetCheckout CLI")
    sub = parser.add_subparsers(dest="command")
    out = sub.add_parser("checkout", help="check out asset")
    out.add_argument("asset_id", help="ID of the asset")
    out.add_argument("--receiver", help="receiver name")
    out.add_argument("--deadline", help="return deadline")
    ret = sub.add_parser("return", help="return asset")
    ret.add_argument("asset_id", help="ID of the asset")
    sh = sub.add_parser("show", help="show records")
    sh.add_argument("--status", help="filter by status")
    args = parser.parse_args()
    if args.command == "checkout":
        checkout(args.asset_id, args.receiver, args.deadline)
    elif args.command == "return":
        return_asset(args.asset_id)
    elif args.command == "show":
        display(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
