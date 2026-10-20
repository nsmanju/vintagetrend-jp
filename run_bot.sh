#!/bin/bash
COUNT=${1:-50}
echo "=== Vintage Japan Trends - $COUNT items REAL PRICES (5 sites) ==="
echo "Morning search: $(date)"
echo "Sites: Yahoo JP | Mercari/Rakuma | Suruga-ya (games/figures/hobby) | Mandarake (anime/collectibles)"
echo "For Suruga-ya LIVE prices: export JP_PROXY=http://user:pass@jp-proxy:port  (needs JP IP per docs)"
python3 -c "import flask" 2>/dev/null || pip3 install flask --break-system-packages
python3 -c "import bs4" 2>/dev/null || pip3 install beautifulsoup4 lxml requests --break-system-packages

python3 scrapers/jp_config.py --count $COUNT
python3 scrapers/yahoo_jp.py --count $COUNT
python3 scrapers/mercari_rakuma.py --count $COUNT
python3 scrapers/surugaya.py --count $COUNT
python3 scrapers/mandarake.py --count $COUNT

# Build combined DB for dashboard
python3 << PY
import json, os, sqlite3, datetime, sys
sys.path.append('scrapers')
from jp_config import get_items
from surugaya import search_surugaya
from mandarake import search_mandarake
from yahoo_jp import search_yahoo_jp
items=get_items($COUNT)
os.makedirs('data', exist_ok=True)
os.makedirs('dashboard/data', exist_ok=True)
conn=sqlite3.connect('data/trends.db')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS trends')
cur.execute('CREATE TABLE trends (id INTEGER PRIMARY KEY, item TEXT, price_jpy INTEGER, source TEXT, date TEXT, detail TEXT)')
for name in items:
    y=search_yahoo_jp(name)
    s=search_surugaya(name)
    m=search_mandarake(name)
    # pick best price (lowest) for dashboard
    prices=[(y['price'],'Yahoo JP'), (s['price'],'Suruga-ya'), (m['price'],'Mandarake')]
    best=min(prices, key=lambda x: x[0])
    cur.execute('INSERT INTO trends (item, price_jpy, source, date, detail) VALUES (?,?,?,?,?)',
                (name, best[0], f"{best[1]} (Best of 3)", datetime.date.today().isoformat(), str(prices)))
conn.commit(); conn.close()
print(f"Seeded {len(items)} real prices -> data/trends.db")
PY

python3 dashboard/app.py --count $COUNT &
echo "Dashboard: http://localhost:5000 - $COUNT REAL prices"
