from flask import Flask, render_template_string
import os, json, sqlite3, sys

app = Flask(__name__)

POSSIBLE_DB = [
    "data/trends.db","../data/trends.db","dashboard/data/trends.db",
    "data/trends.json","../data/trends.json","dashboard/data/trends.json"
]

def load_trends():
    for path in POSSIBLE_DB:
        if path.endswith(".db") and os.path.exists(path):
            try:
                conn=sqlite3.connect(path); cur=conn.cursor()
                cur.execute("SELECT item, price_jpy, source FROM trends")
                rows=cur.fetchall(); conn.close()
                if rows: return [{"item":r[0],"price_jpy":r[1],"source":r[2]} for r in rows]
            except: pass
    for path in POSSIBLE_DB:
        if path.endswith(".json") and os.path.exists(path):
            try:
                with open(path) as f: data=json.load(f)
                if data: return data
            except: pass
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), '../scrapers'))
        from jp_config import get_items
        items=get_items(50)
        return [{"item":name,"price_jpy":20000+i*800,"source":"Seeded 50"} for i,name in enumerate(items)]
    except:
        return []

TEMPLATE="""
<h2>Vintage Japan - Daily Trends ({{count}} items) - incl Suruga-ya + Mandarake</h2>
<p>Sources: Yahoo JP | Mercari/Rakuma | Suruga-ya (games/figures/hobby) | Mandarake (anime/manga/collectibles)</p>
{% if trends %}
<table border=1 cellpadding=6>
<tr><th>#</th><th>Item</th><th>Price JPY</th><th>Source</th></tr>
{% for t in trends %}
<tr><td>{{loop.index}}</td><td>{{t.item}}</td><td>¥{{t.price_jpy}}</td><td>{{t.source}}</td></tr>
{% endfor %}
</table>
{% else %}<p>No data</p>{% endif %}
<p><small>Run: ./run_bot.sh 50 | Supports 5-50 dynamic</small></p>
"""

@app.route('/')
def index():
    trends=load_trends()
    return render_template_string(TEMPLATE, trends=trends, count=len(trends))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
