import argparse, time, sys, os
sys.path.append(os.path.dirname(__file__))
try:
    from jp_config import get_items
except:
    def get_items(c=15): return ["test"]*c

def search_yahoo_jp(query):
    print(f"[Yahoo JP] Searching: {query}...")
    time.sleep(1.5)
    return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=15)
    args = parser.parse_args()
    items = get_items(args.count)
    print(f"=== Yahoo JP - Searching {len(items)} items ===")
    for idx, item in enumerate(items, 1):
        print(f"[{idx}/{len(items)}] {item}")
        search_yahoo_jp(item)
        time.sleep(1)

if __name__ == "__main__":
    main()
