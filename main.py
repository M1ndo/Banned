#!/usr/bin/python3 
# Created By Ybenel
# Updated In 2020/04/14
import sys
sys.path.insert(1, 'src')
from src.Banned import banners
from src.banner import banner
from src.colors import get_colors
def main():
    try:
        banners.main()
    except KeyboardInterrupt as ky:
        print(get_colors.yellow()+get_colors.red() + "\n[!] CTRL+C Detected \n"+get_colors.cyan()+"Thanks For Usage :)")
if __name__ == "__main__":
    banner()
    main()
