
import argparse
JP_50_ITEMS = ['Levis 501 502 Vintage', 'Levis LVC 501', 'Levis 501 Big E', 'Levis Type I Jacket', 'Levis Type II Jacket', 'Levis Type III Trucker', 'Levis 501 66 Model', 'Levis 505 60s Selvedge', 'Lee 101Z Rider Jacket', 'Lee 101B Sanforized', 'Porter Yoshida Tanker Bag', 'Porter Yoshida Boston Bag', 'Red Wing 875 Boot', 'Red Wing 8875 Irish Setter', 'Champion Reverse Weave 90s', 'Champion Reverse Weave Eyelet', 'Carhartt Detroit Jacket Japan', 'Carhartt Double Knee Pants', 'Dickies 874 Vintage', 'Alpha Industries MA-1 Flight Jacket', 'Sony TPS-L2 Walkman', 'Sony WM-D6C Walkman', 'Sony WM-2 Walkman', 'Sony WM-DD9 Discman', 'Sony MDR-7506 Vintage', 'Panasonic RX-5050 Boombox', 'National Panasonic RF-877 Radio', 'Technics SL-1200 MK2 Turntable', 'Victor JVC RC-M90 Boombox', 'Sony WM-FM30 Walkman', 'Vintage Band Tee 80s', 'Metallica Vintage Tee 90s', 'Nirvana Vintage Tee 1993', 'Akira Manga Tee Vintage', 'Ghost in Shell Tee 90s', 'Dragon Ball Z Vintage Tee', 'Studio Ghibli Totoro Tee', 'Harley Davidson 3D Emblem Tee', 'Bape Shark Hoodie Early', 'Human Made Heart Tee', 'Nintendo Famicom Console Boxed', 'Super Nintendo SFC Boxed', 'PlayStation 1 SCPH-1000 Boxed', 'Sega Mega Drive Boxed', 'Tamagotchi Original 1996', 'Gundam RX-78 Model Kit 80s', 'One Piece Luffy Figure Banpresto', 'Pokemon Card Charizard Base Set', 'Final Fantasy VII PS1 Black Label', 'Macross VF-1 Valkyrie Vintage Toy']
def get_items(count: int = 50):
    count = max(5, min(count, 50))
    return JP_50_ITEMS[:count]
def parse_args():
    p = argparse.ArgumentParser(description="Vintage Japan - 50 items incl Suruga-ya Mandarake Real Prices")
    p.add_argument("--count", type=int, default=50)
    return p.parse_args()
if __name__ == "__main__":
    args = parse_args()
    items = get_items(args.count)
    print(f"[JP_CONFIG] {len(items)} items selected:")
    for i, it in enumerate(items,1):
        print(f"{i:02d}. {it}")
