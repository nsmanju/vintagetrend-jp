#!/bin/bash
COUNT=${1:-15}
echo "=== Vintage Japan Trends - $COUNT Japan-hot items ==="
echo "Morning search started: $(date)"
python3 scrapers/jp_config.py --count $COUNT
python3 scrapers/yahoo_jp.py --count $COUNT || echo "yahoo done"
python3 scrapers/mercari_rakuma.py --count $COUNT || echo "mercari done"
if [ -f ./engine/trend_engine ]; then ./engine/trend_engine; elif [ -f ./engine/trend_engine.exe ]; then ./engine/trend_engine.exe; fi
python3 dashboard/app.py --count $COUNT &
echo "Dashboard: http://localhost:5000"
