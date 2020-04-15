# Created By Ybenel
from colors import get_colors
from random import shuffle
def banner():
    print(get_colors.white()+get_colors.randomize()+"""    
      /\_/\ \

 /\  / o o \ \
            
//\\\ \~(*)~/
`  \/   ^ /
   | \|| ||  Welcome To Banned!
   \ '|| ||  
    \)()-())
""" + get_colors.white())
list_choice = ['Nice Choice',"Wow You're Perfect","Cool Choice","You're Talented", "Ooh I See", "Perfect", "Truly Amazing"]
shuffle(list_choice)
for i in list_choice:
    sentence = i
def banner2():
    print(get_colors.white()+get_colors.randomize()+f"""    
      /\_/\ \

 /\  / o o \ \
            
//\\\ \~(*)~/
`  \/   ^ /
   | \|| ||  {sentence}!
   \ '|| ||  
    \)()-())
""" + get_colors.white())
