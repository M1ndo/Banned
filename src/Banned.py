#!/usr/bin/python3 
# Created By Ybenel
# Updated In 2020/04/14
try:
    import pyfiglet,os,sys,optparse
    from colors import get_colors
    from banner import banner,banner2
except ImportError:
    print("[!] Missing Dependecies \n[!] Install Using [pip3 install pyfiglet]")

class banners():
    # def banner():
    #     print(get_colors.white()+get_colors.randomize()+"""
    #          /\_/\
    #     /\  / o o \
    #    //\\ \~(*)~/
    #     `  \/   ^ /
    #     | \|| ||  Lara
    #     \ '|| ||  Allen
    #         \)()-())
    #     """)
    def optparser():
        parser = optparse.OptionParser()
        parser.add_option('-t','--text', dest="text", type="string",help="Your Text That U Wanna Font")
        parser.add_option('-f','--font', dest="font", type="string",help="Your Prefered Font")
        parser.add_option('-s','--show', dest='show',action="store_true",default=False,help="Show All Fonts Available")
        parser.add_option('-a','--all',dest='all', action="store_true", default=False,help="Test All Fonts With Your Text")
        parser.add_option('-v','--version',action="store_true",default=False, dest='version',help="Show Version")
        (options,args) = parser.parse_args()
        return options,parser
    def version():
        version = '2.0'
        print(version)
    def show():
        text = "Sample"
        fonts = pyfiglet.FigletFont.getFonts()
        times = 1
        for i in fonts:
            print(get_colors.white() + f"[{times}] "+get_colors.randomize1()+"Font Name: "+get_colors.randomize2()+f"{i}")
            times += 1 
            print(get_colors.cyan()+"["+get_colors.green()+"+"+get_colors.cyan()+"]"+get_colors.pink()+" Example: \n"+get_colors.randomize3())
            pyfiglet.print_figlet(text, i)
            print(get_colors.magento()+"#"*70 + get_colors.white())   
    def all():
        options, parser = banners.optparser()
        text = options.text
        if text == None:
            banners.case3()
        fonts = pyfiglet.FigletFont.getFonts()
        times = 1
        for i in fonts:
            print(get_colors.white() + f"[{times}] "+get_colors.randomize1()+" Font Name: "+get_colors.randomize2()+f"{i}")
            times += 1
            print(get_colors.white()+"["+get_colors.yellow()+"T"+get_colors.white()+"]"+get_colors.randomize()+" Your Text: "+get_colors.randomize1()+f"{text}\n"+get_colors.pink()+"["+get_colors.sharp_megento()+"+"+get_colors.pink()+"]"+get_colors.randomize2()+" Output: \n"+get_colors.randomize3())
            pyfiglet.print_figlet(text, i)
            print(get_colors.randomize()+"#"*70 + get_colors.white())
    def case1():
        options, parser = banners.optparser()
        text = options.text
        font = options.font
        fonts = pyfiglet.FigletFont.getFonts()
        if font in fonts:
            print(get_colors.white()+"["+get_colors.yellow()+"+"+get_colors.white()+"]"+get_colors.randomize1()+" Font Name: "+get_colors.randomize2()+f"{font}")
            print(get_colors.white()+"["+get_colors.yellow()+"T"+get_colors.white()+"]"+get_colors.randomize()+" Your Text: "+get_colors.randomize1()+f"{text}\n"+get_colors.pink()+"["+get_colors.sharp_megento()+"+"+get_colors.pink()+"]"+get_colors.randomize2()+" Output: \n"+get_colors.randomize3())
            pyfiglet.print_figlet(text,font)
        else:
            print(get_colors.red()+"["+get_colors.magento()+"!"+get_colors.red()+"]"+get_colors.randomize()+" Error: Unknown "+get_colors.randomize1()+f"[{font}]"+get_colors.randomize()+" Font Name" + get_colors.white())
            exit(1)            
    def case2():
        print(get_colors.randomize()+"["+get_colors.red()+"!"+get_colors.randomize()+"]"+get_colors.randomize1()+" Error: Missing Font Name" + get_colors.white())
        exit(1)
    def case3():
        print(get_colors.randomize()+"["+get_colors.red()+"!"+get_colors.randomize()+"]"+get_colors.randomize1()+" Error: Missing Text"+get_colors.white())
        exit(1)
    def clear():
        return os.system('clear')
    def main():
        options, parser = banners.optparser()
        if options.show:
            banners.clear()
            banner2()
            banners.show()
        elif options.all:
            banners.clear()
            banner2()
            banners.all()
        elif options.text and options.font != None:
            banners.clear()
            banner2()
            banners.case1()    
        elif options.text != None and options.font == None:
            banners.clear()
            banner2()
            banners.case2()
        elif options.text == None and options.font != None:
            banners.clear()
            banner2()
            banners.case3()
        elif options.version:
            banners.clear()
            banner2()
            banners.version() 
