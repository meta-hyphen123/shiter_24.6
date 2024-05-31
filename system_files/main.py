import os
import time
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path, 'system_files')
import subprocess
import fade
import random
import glob
current_working_directory = os.getcwd()
def change_directory(target_name):
    global current_working_directory
    # 构建完整的路径模式
    pattern = os.path.join(current_working_directory, target_name + '*')
    # 使用 glob 来查找匹配的目录，限制为最多一个结果
    matches = glob.glob(pattern)
    if matches:
        # 如果找到匹配的项，选择第一个匹配的目录
        new_dir = matches[0]
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            current_working_directory = os.getcwd()
        else:
            print(f"Error: {new_dir} is not a directory")
    else:
        print(f"No matching directory for: {target_name}")
os.system("cls")
def run_python_script(script_name):
    script_path = os.path.join(tools_folder, script_name)
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def logo():
    text = """

                   ▄████████
                  ███    ███
                  ███    █▀
                  ███
                ▀███████████
                         ███
                   ▄█    ███
                 ▄████████▀    ver: 1.1  24Jun"""
    
    options = [fade.brazil(text), fade.purpleblue(text), fade.pinkred(text), fade.fire(text), fade.water(text), fade.greenblue(text), fade.purplepink(text), fade.blackwhite(text)]
    faded_text = random.choice(options)

    # Fading a ascii art text (green-blue)
    print(faded_text)



def run_python(script):
    script_path = os.path.join(tools_folder, script)
    try:
        subprocess.run([script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")
def o(content):
    if not os.path.exists(tools_folder):
        os.makedirs(tools_folder)

    install_txt_path = os.path.join(tools_folder, 'install.txt')

    with open(install_txt_path, 'a') as file:
        file.write('\n' + content)  



red = '\033[91m'  # Red color
yellow = '\033[93m'  # Yellow color
blue = '\033[94m'  # Blue color
green = '\033[92m'  # Green color
orange = '\033[33m'  # Orange color
purple = '\033[95m'  # Purple color
pink = '\033[95m' 
white = '\033[37m' # Pink color
def main():
    global current_working_directory
    user_dir = os.path.join(current_file_path, 'user')  # 用户目录的路径
    os.chdir(user_dir)  # 初始切换到用户目录
    current_working_directory = os.getcwd()  # 更新全局变量

    prom = f"{green}{namme}@{namme}{white}:\033[94m~user{white}$ "
    dos = "1"
    os.chdir(tools_folder)
    try:
        while True:
                user_input = input(prom).strip()

                if user_input == "dir":
                    # 列出当前目录下的文件和目录
                    for item in os.listdir(current_working_directory):
                        print(item)
                elif user_input.startswith("cd "):
                    # 提取 cd 命令的目标目录
                    target_dir = user_input[3:].strip()
                    change_directory(target_dir)  # 尝试切换目录
                    # 更新提示符
                    current_dir = os.path.basename(current_working_directory)
                    prom = f"{green}{namme}@{namme}{white}:\033[94m~user/{current_dir}{white}$ "
                elif user_input.lower() == "exit":
                    break
                if user_input.lower() == 'shiter attack':
                        os.chdir(current_file_path)
                        os.system("python3 attack.py")
                if user_input.lower() == 'logo':
                    logo()
                if user_input.lower() == 'auto attack':
                    os.system("python3 auto_attack.py")
                if 'color' in user_input.lower():
                    if 'red' in user_input.lower():
                        prom = red + prom 
                    if 'yellow' in user_input.lower():
                        prom = yellow+prom 
                    if 'blue' in user_input.lower():
                        prom = blue + prom
                    if 'green' in user_input.lower():
                        prom = green + prom 
                    if 'orange' in user_input.lower():
                        prom = orange + prom
                    if 'purple' in user_input.lower():
                        prom = purple + prom
                    if 'pink' in user_input.lower():
                        prom = pink + prom

                if 'run' in user_input.lower():
                    if 'web2attack' in user_input.lower():
                        os.system("cd web2attack && sudo python3 w2aconsole")
                    elif 'skipfish' in user_input.lower():
                        os.system("sudo skipfish -h")
                    elif 'subdomain finder' in user_input.lower():
                        os.system("cd Sublist3r && python3 sublist3r.py -h")
                    elif 'checkurl' in user_input.lower():
                        os.system("cd checkURL && python3 checkURL.py --help")
                    elif 'blazy' in user_input.lower():
                        os.system("cd Blazy && sudo python2.7 blazy.py")
                    elif 'wifi-pumpkin' in user_input.lower():
                        os.system("sudo wifipumpkin3")
                    elif 'pixiewps' in user_input.lower():
                        os.system(
                            'echo "'
                            '1.> Put your interface into monitor mode using '
                            '\'airmon-ng start {wireless interface}\n'
                            '2.> wash -i {monitor-interface like mon0}\'\n'
                            '3.> reaver -i {monitor interface} -b {BSSID of router} -c {router channel} -vvv -K 1 -f"'
                            '| boxes -d boy')
                        print("You Have To Run Manually By USing >>pixiewps -h ")
                    elif 'bluetooth honeypot gui framework' in user_input.lower():
                        os.system("cd bluepot && sudo java -jar bluepot.jar")
                    elif 'nosqlmap' in user_input.lower():
                        os.system("python NoSQLMap")
                    elif 'leviathan' in user_input.lower():
                        os.system("cd leviathan;python leviathan.py")

                    elif 'fluxion' in user_input.lower():
                        os.system("cd fluxion;sudo bash fluxion.sh -i")
                    elif 'wifiphisher' in user_input.lower():
                        os.system("cd wifiphisher;sudo wifiphisher")
                    elif 'wifite' in user_input.lower():
                        os.system("cd wifite2; sudo wifite")
                    elif 'evil twin' in user_input.lower():
                        os.system("cd fakeap && sudo bash fakeap.sh")
                    elif 'fastssh' in user_input.lower():
                        os.system("cd fastssh && sudo bash fastssh.sh --scan")
                    elif 'howmanypeople' in user_input.lower():
                        os.system("howmanypeoplearearound")
                    elif 'vegile' in user_input.lower():
                        os.system("cd Vegile && sudo bash Vegile")
                        os.system('echo "You can Use Command: \n'
                                  '[!] Vegile -i / --inject [backdoor/rootkit] \n'
                                  '[!] Vegile -u / --unlimited [backdoor/rootkit] \n'
                                  '[!] Vegile -h / --help"|boxes -d parchment')
                    elif 'chrome keylogger' in user_input.lower():
                        os.system("cd HeraKeylogger && sudo python3 hera.py")
                    elif 'autophisher' in user_input.lower():
                        os.system("cd autophisher;sudo bash autophisher.sh")
                    elif 'pyphisher' in user_input.lower():
                        os.system("cd PyPhisher;sudo python3 pyphisher.py")
                    elif 'advphishing' in user_input.lower():
                        os.system("cd AdvPhishing && sudo bash AdvPhishing.sh")
                    elif 'setoolkit' in user_input.lower():
                        os.system("sudo setoolkit")
                    elif 'socialfish' in user_input.lower():
                        os.system("cd SocialFish && sudo python3 SocialFish.py root pass")
                    elif 'hiddeneye' in user_input.lower():
                        os.system("cd HiddenEye;sudo python3 HiddenEye.py")
                    elif 'evilginx2' in user_input.lower():
                        os.system("sudo evilginx")
                    elif 'i-see_you' in user_input.lower():
                        os.system("cd I-See-You && sudo bash ISeeYou.sh")
                    elif 'saycheese' in user_input.lower():
                        os.system("cd saycheese && sudo bash saycheese.sh")
                    elif 'qr code jacking' in user_input.lower():
                        os.system("cd ohmyqr && sudo bash ohmyqr.sh")
                    elif 'wifiphisher' in user_input.lower():
                        os.system("cd wifiphisher;sudo python setup.py")
                    elif 'blackeye' in user_input.lower():
                        os.system("cd blackeye && sudo bash blackeye.sh")
                    elif 'shellphish' in user_input.lower():
                        os.system("cd shellphish;sudo bash shellphish.sh")
                    elif 'thanos' in user_input.lower():
                        os.system("cd Thanos;sudo bash Thanos.sh")
                    elif 'qrljacking' in user_input.lower():
                        os.system("cd QRLJacking/QRLJacker;python3 QrlJacker.py")
                    elif 'maskphish' in user_input.lower():
                        os.system("cd maskphish;sudo bash maskphish.sh")
                    elif 'blackphish' in user_input.lower():
                        os.system("cd BlackPhish;sudo python3 blackphish.py")
                    elif 'dnstwist' in user_input.lower():
                        os.system("cd dnstwist;sudo python3 dnstwist.py")
                    if 'the fatrat' in user_input.lower():
                        os.system("cd TheFatRat && sudo bash setup.sh")
                    elif 'brutal' in user_input.lower():
                        os.system("cd Brutal && sudo bash Brutal.sh")
                    elif 'stitch' in user_input.lower():
                        os.system("cd Stitch && sudo python main.py")
                    elif 'msfvenom' in user_input.lower():
                        os.system("cd msfpc;sudo bash msfpc.sh -h -v")
                    elif 'venom' in user_input.lower():
                        os.system("cd venom && sudo ./venom.sh")
                    elif 'spycam' in user_input.lower():
                        os.system("cd spycam && ./spycam")
                    elif 'mob-droid' in user_input.lower():
                        os.system("cd mob-droid;sudo python mob-droid.py")
                    elif 'enigma' in user_input.lower():
                        os.system("cd Enigma;sudo python enigma.py") 
                    else:
                        print("Shiter can't run tool:{user_input[:14]} ")





                    
                if 'shiter' in user_input.lower():
                    if 'list' in user_input.lower():
                        print(install_content)
                    if 'install' in user_input.lower():

                    
                        if 'slowloris' in user_input.lower():
                            os.system('pip3 install slowloris')
                            o("slowloris")

                        if 'slowloris' in user_input.lower():
                            os.system('pip3 install slowloris')
                        if 'nosqlmap' in user_input.lower():
                            os.system("git clone https://github.com/codingo/NoSQLMap.git")
                            os.system("sudo chmod -R 755 NoSQLMap")
                            os.system("cd NoSQLMap")
                            os.system("python setup.py install")
                            o("nosqlmap")
                        if 'leviathan' in user_input.lower():
                            os.system("git clone https://github.com/leviathan-framework/leviathan.git")
                            os.system("cd leviathan")
                            os.system("sudo pip3 install -r requirements.txt")
                            o("leviathan")

                        if 'web2attack' in user_input.lower():
                            os.system("sudo git clone https://github.com/santatic/web2attack.git")
                            o("web2attack")

                        elif 'skipfish' in user_input.lower():
                            os.system("sudo git clone https://gitlab.com/kalilinux/packages/skipfish.git")
                            os.system("cd skipfish; sudo make")
                            o("skipfish")

                        elif 'subdomain finder' in user_input.lower():
                            os.system("sudo pip3 install requests argparse dnspython")
                            os.system("sudo git clone https://github.com/aboul3la/Sublist3r.git")
                            os.system("cd Sublist3r && sudo pip3 install -r requirements.txt")
                            o("subdomain finder")

                        elif 'checkurl' in user_input.lower():
                            os.system("sudo git clone https://github.com/UndeadSec/checkURL.git")
                            o("checkurl")

                        elif 'blazy' in user_input.lower():
                            os.system("sudo git clone https://github.com/UltimateHackers/Blazy.git")
                            os.system("cd Blazy && sudo pip2.7 install -r requirements.txt")
                            o("blazy")

                        elif 'sub-domain takeover' in user_input.lower():
                            os.system("git clone https://github.com/m4ll0k/takeover.git")
                            os.system("cd takeover; sudo python3 setup.py install")
                            o("sub-domain takeover")

                        elif 'dirb' in user_input.lower():
                            os.system("sudo git clone https://gitlab.com/kalilinux/packages/dirb.git")
                            os.system("cd dirb; sudo bash configure; make")
                            o("dirb")

                        elif 'wifipumpkin' in user_input.lower():
                            os.system("sudo apt install libssl-dev libffi-dev build-essential")
                            os.system("sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git")
                            os.system("chmod -R 755 wifipumpkin3")
                            os.system("sudo apt install python3-pyqt5")
                            os.system("cd wifipumpkin3;sudo python3 setup.py install")
                            o("wifipumpkin")

                        elif 'pixiewps' in user_input.lower():
                            os.system("sudo git clone https://github.com/wiire/pixiewps.git && apt-get -y install build-essential")
                            os.system("cd pixiewps*/ && make")
                            os.system("cd pixiewps*/ && sudo make install && wget https://pastebin.com/y9Dk1Wjh")
                            o("pixiewps")

                        elif 'bluepot' in user_input.lower():
                            os.system("sudo wget https://raw.githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz")
                            os.system("sudo tar xfz bluepot-0.2.tar.gz;sudo rm bluepot-0.2.tar.gz")
                            o("bluepot")

                        elif 'fluxion' in user_input.lower():
                            os.system("git clone https://github.com/FluxionNetwork/fluxion.git")
                            os.system("cd fluxion && sudo chmod +x fluxion.sh")
                            o("fluxion")

                        elif 'wifiphisher' in user_input.lower():
                            os.system("git clone https://github.com/wifiphisher/wifiphisher.git")
                            os.system("cd wifiphisher;sudo python3 setup.py install")
                            ("wifiphisher")

                        elif 'wifite' in user_input.lower():
                            os.system("sudo git clone https://github.com/derv82/wifite2.git")
                            os.system("cd wifite2 && sudo python3 setup.py install")
                            o("wifite")

                        elif 'eviltwin' in user_input.lower():
                            os.system("sudo git clone https://github.com/Z4nzu/fakeap.git")
                            os.system("cd fakeap && sudo bash fakeap.sh")
                            o("eviltwin")

                        elif 'fastssh' in user_input.lower():
                            os.system("sudo git clone https://github.com/Z4nzu/fastssh.git && cd fastssh && sudo chmod +x fastssh.sh")
                            os.system("sudo apt-get install -y sshpass netcat")
                            o("fastssh")

                        elif 'howmanypeople' in user_input.lower():
                            os.system("sudo apt-get install tshark;sudo python3 -m pip install howmanypeoplearearound")
                            os.system("howmanypeoplearearound")
                            o("howmanypeople")
                            

                        if 'vegile' in user_input.lower():
                            os.system("sudo git clone https://github.com/Screetsec/Vegile.git")
                            os.system("cd Vegile && sudo chmod +x Vegile")
                            os.system("cd Vegile && sudo bash Vegile")
                            o("vegile")

                        elif 'chrome keylogger' in user_input.lower():
                            os.system("sudo git clone https://github.com/UndeadSec/HeraKeylogger.git")
                            os.system("cd HeraKeylogger && sudo apt-get install python3-pip -y && sudo pip3 install -r requirements.txt")
                            os.system("cd HeraKeylogger && sudo python3 hera.py")
                            o("chrome keylogger")
                        if 'autophisher' in user_input.lower():
                            os.system("sudo git clone https://github.com/CodingRanjith/autophisher.git")
                            os.system("cd autophisher")
                            os.system("cd autophisher;sudo bash autophisher.sh")
                            o("autophisher")

                        elif 'pyphisher' in user_input.lower():
                            os.system("sudo git clone https://github.com/KasRoudra/PyPhisher")
                            os.system("cd PyPhisher/files")
                            os.system("pip3 install -r requirements.txt")
                            os.system("cd PyPhisher;sudo python3 pyphisher.py")
                            o("pyphisher")

                        elif 'advphishing' in user_input.lower():
                            os.system("sudo git clone https://github.com/Ignitetch/AdvPhishing.git")
                            os.system("cd AdvPhishing;chmod 777 *;bash Linux-Setup.sh")
                            o("advphishing")

                        elif 'setoolkit' in user_input.lower():
                            os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/")
                            os.system("cd social-engineer-toolkit && sudo python3 setup.py")
                            os.system("sudo setoolkit")
                            o("setoolkit")

                        elif 'socialfish' in user_input.lower():
                            os.system("sudo git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y")
                            os.system("cd SocialFish && sudo python3 -m pip install -r requirements.txt")
                            os.system("cd SocialFish && sudo python3 SocialFish.py root pass")
                            o("socialfish")

                        elif 'hiddeneye' in user_input.lower():
                            os.system("sudo git clone https://github.com/Morsmalleo/HiddenEye.git ;sudo chmod 777 HiddenEye")
                            os.system("cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok")
                            os.system("cd HiddenEye;sudo python3 HiddenEye.py")
                            o("hiddeneye")

                        elif 'evilginx2' in user_input.lower():
                            os.system("sudo apt-get install git make;go get -u github.com/kgretzky/evilginx2")
                            os.system("cd $GOPATH/src/github.com/kgretzky/evilginx2;make")
                            os.system("sudo make install;sudo evilginx")
                            o("evilginx2")

                        elif 'i-seeyou' in user_input.lower():
                            os.system("sudo git clone https://github.com/Viralmaniar/I-See-You.git")
                            os.system("cd I-See-You && sudo chmod u+x ISeeYou.sh")
                            os.system("cd I-See-You && sudo bash ISeeYou.sh")
                            o("i-seeyou")

                        elif 'saycheese' in user_input.lower():
                            os.system("sudo git clone https://github.com/hangetzzu/saycheese")
                            os.system("cd saycheese && sudo bash saycheese.sh")
                            o("saycheese")

                        elif 'qrjacking' in user_input.lower():
                            os.system("sudo git clone https://github.com/cryptedwolf/ohmyqr.git && sudo apt -y install scrot")
                            os.system("cd ohmyqr && sudo bash ohmyqr.sh")
                            o("qrjacking")

                        elif 'wifiphisher' in user_input.lower():
                            os.system("sudo git clone https://github.com/wifiphisher/wifiphisher.git")
                            os.system("cd wifiphisher")
                            o("wifiphisher")

                        elif 'blackeye' in user_input.lower():
                            os.system("sudo git clone https://github.com/thelinuxchoice/blackeye")
                            os.system("cd blackeye ")
                            o("blackeye")

                        elif 'shellphish' in user_input.lower():
                            os.system("git clone https://github.com/An0nUD4Y/shellphish.git")
                            os.system("cd shellphish;sudo bash shellphish.sh")
                            o("shellphish")

                        elif 'thanos' in user_input.lower():
                            os.system("sudo git clone https://github.com/TridevReddy/Thanos.git")
                            os.system("cd Thanos && sudo chmod -R 777 Thanos.sh")
                            os.system("cd Thanos;sudo bash Thanos.sh")
                            o("thanos")

                        elif 'qrljacking' in user_input.lower():
                            os.system("git clone https://github.com/OWASP/QRLJacking.git")
                            os.system("cd QRLJacking")
                            os.system("git clone https://github.com/mozilla/geckodriver.git")
                            os.system("chmod +x geckodriver")
                            os.system("sudo mv -f geckodriver /usr/local/share/geckodriver")
                            os.system("sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver")
                            os.system("sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver")
                            os.system("cd QRLJacker;pip3 install -r requirements.txt")
                            os.system("cd QRLJacking/QRLJacker;python3 QrlJacker.py")
                            o("qrljacking")

                        elif 'maskphish' in user_input.lower():
                            os.system("sudo git clone https://github.com/jaykali/maskphish.git")
                            os.system("cd maskphish")
                            os.system("cd maskphish;sudo bash maskphish.sh")
                            o("maskphish")

                        elif 'blackphish' in user_input.lower():
                            os.system("sudo git clone https://github.com/iinc0gnit0/BlackPhish.git")
                            os.system("cd BlackPhish;sudo bash install.sh")
                            os.system("cd BlackPhish;sudo python3 blackphish.py")
                            o("blackphish")

                        elif 'dnstwist' in user_input.lower():
                            os.system("sudo git clone https://github.com/elceef/dnstwist.git")
                            os.system("cd dnstwist")
                            os.system("cd dnstwist;sudo python3 dnstwist.py")
                            o("dnstwist")
                        if 'TheFatRat' in user_input:
                            os.system("sudo git clone https://github.com/Screetsec/TheFatRat.git")
                            os.system("cd TheFatRat && sudo chmod +x setup.sh && sudo bash setup.sh")
                            o("TheFatRat")

                        elif 'Brutal' in user_input:
                            os.system("sudo git clone https://github.com/Screetsec/Brutal.git")
                            os.system("cd Brutal && sudo chmod +x Brutal.sh && sudo bash Brutal.sh")
                            o("Brutal")

                        elif 'Stitch' in user_input:
                            os.system("sudo git clone https://github.com/nathanlopez/Stitch.git")
                            os.system("cd Stitch && sudo pip install -r lnx_requirements.txt && sudo python main.py")
                            o("Stitch")

                        elif 'MSFvenom' in user_input:
                            os.system("sudo git clone https://github.com/g0tmi1k/msfpc.git")
                            os.system("cd msfpc;sudo chmod +x msfpc.sh && sudo bash msfpc.sh -h -v")
                            o("MSFvenom")

                        elif 'Venom' in user_input:
                            os.system("sudo git clone https://github.com/r00t-3xp10it/venom.git")
                            os.system("sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh && sudo ./venom.sh -u")
                            o("Venom")

                        elif 'Spycam' in user_input:
                            os.system("sudo git clone https://github.com/indexnotfound404/spycam.git")
                            os.system("cd spycam && bash install.sh && chmod +x spycam && ./spycam")
                            o("Spycam")

                        elif 'Mob-Droid' in user_input:
                            os.system("git clone https://github.com/kinghacker0/mob-droid.git")
                            os.system("cd mob-droid;sudo python mob-droid.py")
                            o("Mob-Droid")

                        elif 'Enigma' in user_input:
                            os.system("sudo git clone https://github.com/UndeadSec/Enigma.git")
                            os.system("cd Enigma;sudo python enigma.py")
                            o("Enigma")
                        elif '//' in user_input:
                            url = user_input[14:]
                            os.system("git clone"+url)
                        else:
                            print("Shiter can't run command:{user_input} ")
                    else:
                            os.chdir(current_file_path+"\\user")
                            if 'dir' in user_input.lower():
                                os.system("ls")
                                os.system("dir")
                            elif 'ls' in user_input.lower():
                                os.system("ls")
                                os.system("dir")
                            elif './' in user_input.lower():
                                os.system(user_input[8:])
                            elif 'python' in user_input.lower():
                                os.system(user_input[8:]) 
                            elif 'git clone' in user_input.lower():
                                os.system(user_input[8:])
                            elif 'md test' in user_input.lower():
                                pass
                            
                            elif 'shutdown' in user_input.lower():
                                if 's' in user_input.lower():
                                    os.system("shutdown /s")
                                if 'r' in user_input.lower():
                                    os.system("shutdown /r")
                                if 'l' in user_input.lower():
                                    os.system("shutdown /l")
                                if 'h' in user_input.lower():
                                    os.system("shutdown /h /f")
                                if 'a' in user_input.lower():
                                    os.system("shutdown /a")

                                if '/s /t' in user_input.lower():
                                    os.system(user_input[8:])
                                else:
                                    os.chdir(current_file_path+"user")
       
                        
                os.chdir(current_file_path+"\\user")
                if 'hack_' in user_input.lower():
                    if 'hack_scanqli' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_ddos' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmap' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmate' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_xsscon' in user_input.lower():
                        os.chdir(tools_folder+"\\xsscon")
                        os.system("python "+user_input)
                        os.chdir(tools_folder)
                        
                    if 'hack_xsstrike' in user_input.lower():
                        os.chdir(tools_folder+"\\xsstrike")
                        os.system("python "+user_input)
                        os.chdir(tools_folder)

                    if 'hack_cpscan' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python "+user_input)
                        os.chdir(tools_folder)


                    if 'hack_wifi' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python "+user_input)
                        os.chdir(tools_folder)
                    else:
                        pass
                if user_input.lower() == 'cl':
                    os.system("clear")
                    os.system("cls")                    
                
                if 'shiter_xss' in user_input.lower():
                    os.system("python "+user_input)
                    os.chdir(tools_folder)

                if user_input.lower() == 'dns-shell':
                    os.system("cls")
                    os.system("clear")
                    run_python_script("DNShell.py")
                    
                if user_input.lower() == 'ip':
                    os.system("ipconfig")
                    
                elif 'shiter_admin-finder' in user_input.lower():
                    os.system("python "+user_input)


                elif 'shiter_xctr' in user_input.lower():
                    os.system("python xctr.py")
                if user_input.lower() == 'python':
                    os.chdir(tools_folder)
                    os.system("python3 python.py")
                elif './' in user_input.lower():
                    os.system(user_input)
                elif user_input.lower() == 'python':
                    os.system("python")
                elif 'python' in user_input.lower():
                    os.system(user_input)
                elif 'git clone' in user_input.lower():
                    os.system(user_input)
                elif 'md test' in user_input.lower():
                    pass
                commands = ['ls', 'pwd', 'mkdir', 'rm', 'cp', 'mv',
                            'cat', 'less', 'head', 'tail', 'grep', 'find',
                            'chmod', 'chown', 'tar', 'wget', 'ssh', 'ps',
                            'kill', 'top', 'ifconfig', 'ping', 'netstat',
                            'df', 'du', 'scp', 'crontab', 'yum']

                if any(cmd in user_input for cmd in commands):
                    os.system(user_input)

                if user_input.lower() == 'show password':
                    print("password:" + namme)
                    pass
                elif 'shutdown' in user_input.lower():
                    if 's' in user_input.lower():
                        os.system("shutdown /s")
                    if 'r' in user_input.lower():
                        os.system("shutdown /r")
                    if 'l' in user_input.lower():
                        os.system("shutdown /l")
                    if 'h' in user_input.lower():
                        os.system("shutdown /h /f")
                    if 'a' in user_input.lower():
                        os.system("shutdown /a")

                    if '/s /t' in user_input.lower():
                        os.system(user_input)
                    
                    else:
                        pass
                if user_input.lower() == 'exit':
                    break
                        
                else:
                    pass

    except KeyboardInterrupt:
        print("^C")
        main()
