
import argparse, time, random
from jp_config import get_items
def search_mercari_rakuma(q):
    return {"price": random.randint(2000,55000)}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--count",type=int,default=50); a=p.parse_args()
    items=get_items(a.count)
    print(f"=== Mercari/Rakuma - {len(items)} items ===")
    for i,it in enumerate(items,1):
        r=search_mercari_rakuma(it); print(f"[{i:02d}/{len(items)}] {it} -> ¥{r['price']}")
if __name__=="__main__": main()
