# Vintage Japan Trend Bot - 10 Items

Private Japan-only vintage tracker.

Sources: Yahoo Auctions / 【entity-Mercari¦canonical_name=Mercari】 / Rakuma via Buyee
Currency: JPY
Items: 10 vintage pieces (501s, Trucker Jackets, Walkmans)

## Run (Ubuntu)
./run_bot.sh
python dashboard/app.py
Open http://localhost:5000

## Run (Windows)
run_bot.bat
python dashboard/app.py

## Architecture
scrapers/ -> data/vintage.db -> engine/trend_engine (C++ sqlite) -> dashboard/trends.json -> Flask
Engine logs off, dashboard persists.

## Privacy
Private repo - Japan data only
