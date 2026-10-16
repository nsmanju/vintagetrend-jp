import sqlite3
from datetime import datetime, timezone
DB = "data/vintage.db"
def scrape_mercari():
    conn = sqlite3.connect(DB)
    sample = [
        ("mercari_jp", "Vintage 90s 501 Big E Selvedge Denim", 18000, "https://jp.mercari.com/item/501-1"),
        ("mercari_jp", "WM-D6C Walkman Pro Vintage Audio", 35000, "https://jp.mercari.com/item/wm1"),
        ("rakuma_jp", "Trucker Jacket 70505 60s Vintage", 28000, "https://fril.jp/item/trucker1"),
        ("mercari_jp", "Vintage 60s Type 2 Trucker Jacket Selvedge", 32000, "https://jp.mercari.com/item/type2"),
        ("mercari_jp", "Vintage 70s 505 Big E Orange Tab", 15000, "https://jp.mercari.com/item/505"),
    ]
    now = datetime.now(timezone.utc).isoformat()
    for s,t,p,u in sample:
        conn.execute("INSERT INTO listings(source,title,price,currency,category,url,scraped_at) VALUES(?,?,?,?,?,?,?)",
            (s,t,p,"JPY","vintage",u,now))
    conn.commit(); conn.close()
    print("Mercari JP: inserted 5 rows")
if __name__ == "__main__":
    scrape_mercari()
