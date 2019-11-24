#!/usr/bin/python
# Made By ybenel
# Twitter : @_ybenel
try:

 import pyfiglet,optparse

except:

  print("[!] Error: Please Install PyFiglet Library Use Command:> \033[1;32mpip install pyfiglet")
  exit(1)

##########################################
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
cyan="\033[96m"
stong="\033[41m"
##########################################


print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+Blue+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+Blue+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+Blue+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+Blue+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+Blue+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+Blue+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+Blue+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+Blue+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+Blue+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+Blue+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+Blue+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+Blue+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+Blue+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+Blue+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+Blue+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+Blue+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+cyan+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"              "+Green+"["+Reset+"Banned"+Reset+"]"+Blue+"         ")
print("     "+Red+"         "+Red+"["+Red+"    Made By ybenel"+Grey+"]"+Blue+"    "+Reset+"\n")

parse = optparse.OptionParser("""
  Usage: python banned.py [OPTION..]
  OPTIONS:
  -t --text    >> Your Name Or Nickname Or Any Text
  -s --show    >> SHOW All Fonts You Can Use With Example
  -f --font    >> Set Font Name You Want
  -a --all     >> Use all Fonts With Your Text
  Examples:
  python banned.py --show
  python banned.py -t Python -f speed
  python banned.py -t ybenel --all
""",version='1.0')  
def Main():
  parse.add_option("-t",'-T','--text','--TEXT',dest="tex",type="string")
  parse.add_option('-f','-F','--font','--FONT',dest='font',type="string")
  parse.add_option('-s','-S','--show','--SHOW',action='store_true',dest='show',default=False)
  parse.add_option('-a','-A','--all','--ALL',action='store_true',dest='all',default=False)
  (options, args) = parse.parse_args()
  if options.show:
	text = "Your Text"
	fonts = pyfiglet.FigletFont.getFonts()
	loop = 1
	try:
	 for f in fonts:
	    print("\033[1;32m[\033[1;37m{}\033[1;32m] Font Name: \033[1;33m{}".format(loop,f))
	    loop +=1
	    print("\033[1;32m[#] Example:\n\033[1;36m")
	    pyfiglet.print_figlet(text,f)
	    print("\033[1;35m")
	    print("="*60)
	except KeyboardInterrupt:
		print("\n\033[1;31m[Ctrl+c]\033[1;33m Exit!")
		exit(1)

  elif options.tex !=None and options.font !=None:
	text = options.tex
	font = options.font
	fonts = pyfiglet.FigletFont.getFonts()
	if font in fonts:
            print("\033[1;32m[\033[1;37m~\033[1;32m] Font Name: \033[1;33m{}".format(font))
            print("\033[1;32m[T]\033[1;37m Your Text:\033[1;33m {}\n\033[1;37m\nOutput:\n".format(text))
            pyfiglet.print_figlet(text,font)
	else:
	   print("\n\033[1;31m[!]\033[1;33m Error:\033[1;37m Unknown \033[1;33m[{}]\033[1;37m Font Name\n\033[1;32m[*]\033[1;37m Please Try Use:\033[1;32m --show >\033[1;37m For Show All Fonts Names You Can Set With Examples".format(font))
	   exit(1)
  elif options.tex !=None and options.all:
        text = options.tex
        fonts = pyfiglet.FigletFont.getFonts()
        loop = 1
        try:
         for f in fonts:
            print("\033[1;32m[\033[1;37m{}\033[1;32m] Font Name: \033[1;33m{}".format(loop,f))
            loop +=1
            print("\033[1;32m[T]\033[1;37m Your Text:\033[1;33m {}\n\033[1;37m\nOutput:\n".format(text))
            pyfiglet.print_figlet(text,f)
            print("\033[1;35m")
            print("="*60)
        except KeyboardInterrupt:
                print("\n\033[1;31m[Ctrl+c]\033[1;33m Exit!")
                exit(1)
  else:
	print(parse.usage)
	exit(1)


if __name__=="__main__":
	Main()
#'='!!

