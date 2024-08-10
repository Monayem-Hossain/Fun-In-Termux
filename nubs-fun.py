import subprocess, time

def cmd(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error : {e}")

def sl():
    cmd("sl")
def cacafire():
    cmd("cacafire")
def cmatrix():
    cmd("cmatrix")
def fortune():
    cmd("fortune")
def cowsay():
    txt = input("Enter Your Name : ")
    cmd(f"cowsay {txt}")
def toilet():
    txt = input("Enter Your Name : ")
    cmd(f'toilet -f mono12 -F gay "{txt}"')
def web():
    txt = input("Enter Web-link : ")
    cmd(f"w3m {txt}")
def map():
    cmd("telnet mapscii.me")
def pak():
    cmd("pkg install sl")
    cmd("pkg install libcaca")
    cmd("pkg install toilet")
    cmd("pkg install cmatrix")
    cmd("pkg install cowsay")
    cmd("pkg install w3m")
    cmd("pkg install fortune")

def curl():
    txt = input("Enter City Name : ")
    cmd(f"curl wttr.in/{txt}")
def main(): 
    while True:
        cmd("clear")
        print("""Make a Choice:
              1. Train in Termux
              2. Put Termux in Fire
              3. Matrix Cemulation
              4. Know Your Fortune
              5. Cow Say
              6. Banner in Your Name
              7. Use Web in Termux
              8. World Map
              9. Weather Information
              0. Install Required Package
              q. Exit
        """)
        x=input("==> ")
        if x=="1":
            sl()
        elif x=="2":
            cacafire()
        elif x=="3":
            cmatrix()
        elif x=="4":
            fortune()
        elif x=="5":
            cowsay()
        elif x=="6":
            toilet()
        elif x=="7":
            web()
        elif x=="8":
            map()
        elif x=="9":
            curl()
        elif x=="0":
            pak()
        elif x=="q":
            exit()
        else:
            print("Make a Right Choice.....")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit...")