@echo off
set COUNT=%1
if "%COUNT%"=="" set COUNT=15
echo Vintage Japan Trends - %COUNT% items - Morning Search
python scrapers/jp_config.py --count %COUNT%
python scrapers/yahoo_jp.py --count %COUNT%
if exist engine\trend_engine.exe engine\trend_engine.exe
python dashboard/app.py --count %COUNT%
pause
