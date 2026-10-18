import argparse

DEFAULT_JP_ITEMS = [
    "Levis 501 502 Vintage",
    "Levis LVC 501",
    "Levis 501 Big E",
    "Levis Type I Jacket",
    "Levis Type II Jacket",
    "Levis Type III Trucker",
    "Sony TPS-L2 Walkman",
    "Sony WM-D6C Walkman",
    "Vintage Band Tee 80s",
    "Red Wing 875 Boot"
]

EXTRA_POOL = [
    "Levis 501 66 Model",
    "Lee 101Z Rider Jacket",
    "Porter Yoshida Tanker Bag",
    "Sony WM-2 Walkman",
    "Champion Reverse Weave 90s"
]

def get_items(count: int = 15):
    count = max(5, min(count, 30))
    if count <= 10:
        return DEFAULT_JP_ITEMS[:count]
    return DEFAULT_JP_ITEMS + EXTRA_POOL[:count-10]

def parse_args():
    parser = argparse.ArgumentParser(description="Vintage Japan Trends - Japan-hot items")
    parser.add_argument("--count", type=int, default=15, help="Number of items to search (5-30)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    items = get_items(args.count)
    print(f"[JP_CONFIG] {len(items)} items selected:")
    for i, it in enumerate(items, 1):
        print(f"{i}. {it}")
