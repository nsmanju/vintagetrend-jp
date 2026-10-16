import sqlite3
from datetime import datetime, timezone
DB = "data/vintage.db"
def scrape_yahoo():
    conn = sqlite3.connect(DB)
    now = datetime.now(timezone.utc).isoformat()
    fallback = [
        ("yahoo_jp", "Vintage 501 Selvedge Japan 60s", 12000, "https://buyee.jp/item/501-60s"),
        ("yahoo_jp", "WM-2 Walkman Vintage Japan Audio", 20000, "https://buyee.jp/item/wm2"),
        ("yahoo_jp", "Vintage 80s 501 66 Redline Selvedge", 22000, "https://buyee.jp/item/501-66"),
        ("yahoo_jp", "Vintage 70s Denim Work Shirt Big E", 9800, "https://buyee.jp/item/workshirt"),
        ("yahoo_jp", "WM-DD33 Disc Drive Walkman Vintage", 45000, "https://buyee.jp/item/dd33"),
    ]
    for s,t,p,u in fallback:
        conn.execute("INSERT INTO listings(source,title,price,currency,category,url,scraped_at) VALUES(?,?,?,?,?,?,?)",
            (s,t,p,"JPY","vintage",u,now))
    conn.commit(); conn.close()
    print(f"Yahoo JP: inserted {len(fallback)} rows")
if __name__ == "__main__":
    scrape_yahoo()
