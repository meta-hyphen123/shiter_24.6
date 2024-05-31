import os
import time
import subprocess
import fade
import random
import glob
import getpass
import requests
import webbrowser
import sys
import json
import shutil
def print_working_directory():
    try:
        return os.getcwd()
    except Exception as e:
        return str(e)

def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        return 'Directory created'
    except Exception as e:
        return str(e)

def remove_file_or_directory(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        else:
            return 'Path does not exist'
        return 'File/Directory removed'
    except Exception as e:
        return str(e)

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        return f'Copied {src} to {dst}'
    except Exception as e:
        return str(e)

def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        return str(e)

def write_file(path, content):
    try:
        with open(path, 'w') as file:
            file.write(content)
        return f'Written to {path}'
    except Exception as e:
        return str(e)

def get_file_info(path):
    try:
        info = os.stat(path)
        return f'Size: {info.st_size} bytes\nPermissions: {stat.filemode(info.st_mode)}\nOwner: {info.st_uid}\nGroup: {info.st_gid}\nLast modified: {info.st_mtime}'
    except Exception as e:
        return str(e)

def change_file_permissions(path, mode):
    try:
        os.chmod(path, mode)
        return f'Changed permissions of {path} to {oct(mode)}'
    except Exception as e:
        return str(e)

def create_symbolic_link(src, dst):
    try:
        os.symlink(src, dst)
        return f'Created symbolic link from {src} to {dst}'
    except Exception as e:
        return str(e)
def format_size(size):
    # Format file size
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024

def get_last_write_time(path):
    # Get the last write time of a file/folder
    time_obj = time.gmtime(os.path.getmtime(path))
    return time.strftime('%m/%d/%Y %I:%M %p', time_obj)

def list_directory(path="."):
    # Get the directory contents
    try:
        entries = os.listdir(path)
    except PermissionError:
        print(f"{red}Error: You do not have the necessary permissions to access '{path}'.{white}")
        return

    # Print the header
    print(f"Directory: {path}")
    print("Mode                 LastWriteTime         Length Name")

    # Print the separator
    print("----                 -------------         ------ ----")

    # Iterate over the directory contents
    for entry in entries:
        full_path = os.path.join(path, entry)
        mode = ""
        if os.path.isdir(full_path):
            mode = "d----"
            color = yellow
        elif os.path.isfile(full_path):
            mode = "-a---"
            color = white
        if os.access(full_path, os.R_OK):
            mode = mode[:1] + "r" + mode[2:]
        if os.access(full_path, os.W_OK):
            mode = mode[:2] + "w" + mode[3:]
        if os.access(full_path, os.X_OK):
            mode = mode[:3] + "x" + mode[4:]

        last_write_time = get_last_write_time(full_path)
        size = format_size(os.path.getsize(full_path)) if os.path.isfile(full_path) else ""
        print(f"{color}{mode}  {last_write_time}  {size:>10}  {entry}{white}")
def install_git():
    try:
        # Check if Git is installed
        git_version = os.system("git --version")
        if git_version == 0:
            print("Git is already installed.")
        else:
            # Determine the package manager based on the OS
            system_os = platform.system()
            if system_os == "Windows":
                # Windows: Download and run the Git installer
                os.system("start https://github.com/git-for-windows/git/releases/download/v2.45.1.windows.1/Git-2.45.1-64-bit.exe")
            elif system_os == "Linux":
                # Linux (Debian/Ubuntu): Install Git using APT
                os.system("sudo apt install git -y")
            else:
                print("Unsupported operating system.")
                return

            print("Git has been installed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def is_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

    if is_git_installed():
        pass
    else:
        install_git()
        
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path, 'system_files')
git_folder = os.path.join(current_file_path, 'user')
def clear():
    import  platform
    if platform.system() == "Windows":
        os.system("cls")
    if  platform.system()  == "Linux":
        os.system("clear")
    else:
        pass
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"delete {file_path}!")
    except PermissionError:
        print(f"Error: You do not have the necessary permissions to delete '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file or directory '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # 打印完所有字符后换行

def replace_wormgpt(answer):
    if "WORMGPT" in answer:
        answer = answer.replace("WORMGPT", "ShiterGPT")
    return answer

def display_response(answer):
    if answer is not None:
        typewriter(answer, 0.001)
    else:
        print("No answer available.")

def handle_exit():
    print("Exiting the program.")
    exit()

api_url = "https://worker-quiet-haze-bf7d.apinepdev.workers.dev/"

def ask_question(question):
    if question.lower() == 'exit':
        handle_exit()

    response = requests.get(f"{api_url}?question={question}&state=omega")

    if response.status_code == 200:
        json_response = response.json()
        answer = json_response.get("answer")
        if answer:
            updated_answer = replace_wormgpt(answer)
            display_response(updated_answer)
        else:
            print("No answer available in the response.")
    else:
        print("Failed to get a response. Status code:", response.status_code)

current_working_directory = os.getcwd()

def change_directory(target_name):
    global current_working_directory
    pattern = os.path.join(current_working_directory, target_name + '*')

    matches = glob.glob(pattern)
    if matches:

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


    else:
        print(f"{tool_name} not found.")
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

def read_install_txt():
    install_txt_path = os.path.join(tools_folder, 'install.txt')

    with open(install_txt_path, 'r') as file:
        content = file.read()
    
    return content

def read_install():
    os.chdir(user_dir)
    install_txt_path = os.path.join(current_file_path, 'Shiter.py')

    with open(install_txt_path, 'r') as file:
        content = file.read()
    
    return content

def namme():
    install_txt_path = os.path.join(tools_folder, 'name.txt')

    with open(install_txt_path, 'r') as file:
        content = file.read()
    
    return content

def welcome():
    print("Welcome To Shiter ")

namme = namme()
def wget(url,save_path):
    import urllib.request

    def download_file(url, save_path):
        try:
            urllib.request.urlretrieve(url, save_path)
            
        except Exception as e:
            print(f"Error：{e}")

    download_file(url, save_path)

def login():
    pdw = getpass.getpass("password :")
    if pdw.lower() == namme:
            main()
    else:
        print("""Your password is incorrct""")
        time.sleep(1)
        login()

red = '\033[91m'  # Red color
yellow = '\033[93m'  # Yellow color
blue = '\033[94m'  # Blue color
green = '\033[92m'  # Green color
orange = '\033[33m'  # Orange color
purple = '\033[95m'  # Purple color
pink = '\033[95m' 
white = '\033[37m' # Pink color
def install_tool(tool_name, tools):
    """根据工具名称安装工具"""
    if tool_name in tools:
        url = tools[tool_name]
        print(f"installing {tool_name}...")
        # 确保 user_dir 存在
        os.makedirs(git_folder, exist_ok=True)
        # 使用 git clone 命令下载工具到 user_dir
        subprocess.run(f"git clone {url} {git_folder}", shell=True)
    else:
        print(f"{tool_name} can't find it")
def process(user_input):
    global current_working_directory
    user_dir = os.path.join(current_file_path, 'user')
    os.chdir(user_dir)
    current_working_directory = os.getcwd()

    os.chdir(tools_folder)
    if '1' == '1':

            if 'shiter' in user_input.lower():
                    tool_name = user_input[len("shiter install "):].strip()
                    
                    # 确保data.json文件的路径正确
                    with open(os.path.join(user_dir, 'data.json'), 'r') as f:
                        tools_data = json.load(f)
                    
                    # 将JSON数据转换为字典，以工具名作为键
                    tools = {tool['name']: tool['url'] for tool in tools_data.values()}
                    
                    # 调用install_tool函数来安装工具
                    install_tool(tool_name, tools)

            if '@shitergpt' in user_input.lower():
                q = user_input[11:]
                ask_question(q)
            if user_input == "dir":
                for item in os.listdir(current_working_directory):
                    print(item)
            
            elif user_input.lower() == 'cd':
                os.chdir(current_file_path)
                os.chdir("user")
                current_working_directory = os.getcwd()
                prom = f"{green}{namme}@{namme}{white}~user{white}#"
            
            elif user_input.startswith("cd "):
                target_dir = user_input[3:].strip()
                change_directory(target_dir)
                current_dir = os.path.basename(current_working_directory)
                prom = f"{green}{namme}@{namme}{white}~user/{current_dir}{white}# "
            
            elif user_input.lower() == "exit":
                exit()
            
            elif user_input.lower() == 'shiter attack':
                os.chdir(current_file_path)
                os.system("python3 attack.py")
            
            elif user_input.lower() == 'logo':
                logo()
            
            elif user_input.lower() == 'auto attack':
                os.system("python3 auto_attack.py")
            elif 'wget ' in user_input.lower():
                url = user_input[5:]
                wget(url,current_working_directory)
            elif 'color' in user_input.lower():
                if 'red' in user_input.lower():
                    prom = red + prom 
                elif 'yellow' in user_input.lower():
                    prom = yellow + prom 
                elif 'blue' in user_input.lower():
                    prom = blue + prom
                elif 'green' in user_input.lower():
                    prom = green + prom 
                elif 'orange' in user_input.lower():
                    prom = orange + prom
                elif 'purple' in user_input.lower():
                    prom = purple + prom
                elif 'pink' in user_input.lower():
                    prom = pink + prom
            
            elif 'run' in user_input.lower():
                script_name = user_input.split('run ')[1].strip()
                run_python_script(script_name)
            

            
            elif user_input.lower() == 'cl':
                clear()
            
            elif 'shiter_xss' in user_input.lower():
                os.system("python " + user_input)
                os.chdir(tools_folder)
            
            elif user_input.lower() == 'dns-shell':
                clear()
                run_python_script("DNShell.py")
            
            elif user_input.lower() == 'ip':
                os.system("ipconfig")
            
            elif 'shiter_admin-finder' in user_input.lower():
                os.system("python " + user_input)
            
            elif user_input.startswith('python'):
                os.system(user_input)
            elif 'shiter_xctr' in user_input.lower():
                os.system("python xctr.py")
            
            elif user_input.lower() == 'python':
                os.chdir(tools_folder)
                os.system("python3 python.py")
            
            elif './' in user_input.lower():
                os.system(user_input)
            
            elif 'git clone' in user_input.lower():
                os.system(user_input)
            
            elif 'md test' in user_input.lower():
                pass

            elif any(cmd in user_input for cmd in ['ls', 'pwd', 'mkdir', 'rm', 'cp', 'mv', 'cat', 'less', 'head', 'tail', 'grep', 'find', 'chmod', 'chown', 'tar', 'wget', 'ssh', 'ps', 'kill', 'top', 'ifconfig', 'ping', 'netstat', 'df', 'du', 'scp', 'crontab', 'yum']):
                os.system(user_input)

            elif 'shit http' in user_input.lower():
                U = user_input[5:]
                os.chdir(current_working_directory)
                os.system("git clone {U}")
            elif user_input.lower() == 'show password':
                print("password:" + namme)
            

            elif 'hack_' in user_input.lower():
                    if 'hack_scanqli' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_ddos' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmap' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmate' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_xsscon' in user_input.lower():
                        os.chdir(tools_folder+"/xsscon")
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    else:
                        pass
            elif 'shutdown' in user_input.lower():
                if 's' in user_input.lower():
                    os.system("shutdown /s")
                elif 'r' in user_input.lower():
                    os.system("shutdown /r")
                elif 'l' in user_input.lower():
                    os.system("shutdown /l")
                elif 'h' in user_input.lower():
                    os.system("shutdown /h /f")
                elif 'a' in user_input.lower():
                    os.system("shutdown /a")
                elif '/s /t' in user_input.lower():
                    os.system(user_input)
                else:
                    print("Error")

    if user_input.lower() == 'help':
        pass
    else:
        pass

def main():
    global current_working_directory
    user_dir = os.path.join(current_file_path, 'user')
    os.chdir(user_dir)
    current_working_directory = os.getcwd()
    
    prom = f"{green}{namme}@{namme}{white}~user{white}# "
    os.chdir(tools_folder)
    try:
        while True:
            user_input = input(prom).strip()
            if not user_input:
                continue
            if 'shiter install' in user_input.lower():
                    tool_name = user_input[len("shiter install "):].strip()
                    
                    # 确保data.json文件的路径正确
                    with open(os.path.join(user_dir, 'data.json'), 'r') as f:
                        tools_data = json.load(f)
                    
                    # 将JSON数据转换为字典，以工具名作为键
                    tools = {tool['name']: tool['url'] for tool in tools_data.values()}
                    
                    # 调用install_tool函数来安装工具
                    install_tool(tool_name, tools)
            if '@shitergpt' in user_input.lower():
                q = user_input[11:]
                ask_question(q)
            if user_input.lower() == 'dir':
                list_directory(current_working_directory)
            if user_input.startswith('ls'):
                path = user_input[3:].strip() or '.'
                print(list_directory(path))
            
            elif user_input == 'pwd':
                print(print_working_directory())
            
            elif user_input.startswith('mkdir'):
                path = user_input[6:].strip()
                print(make_directory(path))
            
            elif user_input.startswith('rm'):
                path = user_input[3:].strip()
                print(remove_file_or_directory(path))
            
            elif user_input.startswith('cp'):
                parts = user_input[3:].strip().split()
                if len(parts) == 2:
                    src, dst = parts
                    print(copy_file(src, dst))
                else:
                    print("Usage: cp <source> <destination>")
            
            elif user_input.startswith('cat'):
                path = user_input[4:].strip()
                print(read_file(path))
            
            elif user_input.startswith('echo'):
                parts = user_input[5:].strip().split('>')
                if len(parts) == 2:
                    content, path = parts
                    print(write_file(path.strip(), content.strip()))
                else:
                    print("Usage: echo <content> > <file_path>")
            
            elif user_input.startswith('stat'):
                path = user_input[5:].strip()
                print(get_file_info(path))
            
            elif user_input.startswith('chmod'):
                parts = user_input[6:].strip().split()
                if len(parts) == 2:
                    mode = int(parts[0], 8)
                    path = parts[1]
                    print(change_file_permissions(path, mode))
                else:
                    print("Usage: chmod <mode> <file_path>")
            
            elif user_input.startswith('ln'):
                parts = user_input[3:].strip().split()
                if len(parts) == 2:
                    src, dst = parts
                    print(create_symbolic_link(src, dst))
                else:
                    print("Usage: ln <source> <destination>")
            
            elif user_input.lower() == 'cd':
                os.chdir(current_file_path)
                os.chdir("user")
                current_working_directory = os.getcwd()
                prom = f"{green}{namme}@{namme}{white}~user{white }# "
            
            elif user_input.startswith("cd "):
                target_dir = user_input[3:].strip()
                change_directory(target_dir)
                current_dir = os.path.basename(current_working_directory)
                prom = f"{green}{namme}@{namme}{white}~user/{current_dir}{white }# "
            
            elif user_input.lower() == "exit":
                exit()
            
            elif user_input.lower() == 'shiter attack':
                os.chdir(current_file_path)
                os.system("python3 attack.py")
            
            elif user_input.lower() == 'logo':
                logo()
            
            elif user_input.lower() == 'auto attack':
                os.system("python3 auto_attack.py")
            elif 'wget ' in user_input.lower():
                url = user_input[5:]
                wget(url,current_working_directory)
            elif 'delete ' in user_input.lower():
                filename = user_input[7:]
                delete_path = os.path.join(current_working_directory, filename)
                delete_file(delete_path)
            elif 'color' in user_input.lower():
                if 'red' in user_input.lower():
                    prom = red + prom 
                elif 'yellow' in user_input.lower():
                    prom = yellow + prom 
                elif 'blue' in user_input.lower():
                    prom = blue + prom
                elif 'green' in user_input.lower():
                    prom = green + prom 
                elif 'orange' in user_input.lower():
                    prom = orange + prom
                elif 'purple' in user_input.lower():
                    prom = purple + prom
                elif 'pink' in user_input.lower():
                    prom = pink + prom
            
            elif 'run' in user_input.lower():
                script_name = user_input.split('run ')[1].strip()
                run_python_script(script_name)
            
            elif user_input.startswith("shiter "):
                if 'su' in user_input.lower():
                    os.chdir(current_file_path)
                    os.system("python3 root.py")    
                    exit()
                    
                else:
                        p = user_input[7:]
                        process(p)

            elif 'shit http' in user_input.lower():
                U = user_input[5:]
                os.chdir(current_working_directory)
                os.system("git clone "+U)
            
            elif user_input.lower() == 'cl':
                clear()
            
            elif 'shiter_xss' in user_input.lower():
                os.system("python " + user_input)
                os.chdir(tools_folder)
            
            elif user_input.lower() == 'dns-shell':
                clear()
                run_python_script("DNShell.py")
            
            elif user_input.lower() == 'ip':
                os.system("ipconfig")
            
            elif 'shiter_admin-finder' in user_input.lower():
                os.system("python " + user_input)
            
            elif user_input.startswith('python'):
                os.chdir(current_working_directory)
                os.system(user_input)
            elif 'shiter_xctr' in user_input.lower():
                os.system("python xctr.py")
            
            elif user_input.lower() == 'python':
                os.chdir(tools_folder)
                os.system("python3 python.py")
            
            elif './' in user_input.lower():
                os.system(user_input)
            
            elif 'git clone' in user_input.lower():
                os.system(user_input)
            
            elif 'md test' in user_input.lower():
                pass

            elif any(cmd in user_input for cmd in ['ls', 'pwd', 'mkdir', 'rm', 'cp', 'mv', 'cat', 'less', 'head', 'tail', 'grep', 'find', 'chmod', 'chown', 'tar', 'wget', 'ssh', 'ps', 'kill', 'top', 'ifconfig', 'ping', 'netstat', 'df', 'du', 'scp', 'crontab', 'yum']):
                os.system(user_input)
            
            elif user_input.lower() == 'show password':
                print("password:" + namme)
            

            elif 'hack_' in user_input.lower():
                    if 'hack_scanqli' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_ddos' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmap' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_sqlmate' in user_input.lower():
                        os.chdir(tools_folder)
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    if 'hack_xsscon' in user_input.lower():
                        os.chdir(tools_folder+"/xsscon")
                        os.system("python3 "+user_input)
                        os.chdir(tools_folder)
                    else:
                        pass
            elif 'shutdown' in user_input.lower():
                if 's' in user_input.lower():
                    os.system("shutdown /s")
                elif 'r' in user_input.lower():
                    os.system("shutdown /r")
                elif 'l' in user_input.lower():
                    os.system("shutdown /l")
                elif 'h' in user_input.lower():
                    os.system("shutdown /h /f")
                elif 'a' in user_input.lower():
                    os.system("shutdown /a")
                elif '/s /t' in user_input.lower():
                    os.system(user_input)
                else:
                    print("Error")
            
            else:
                print("Can't run that command")
    
    except KeyboardInterrupt:
        print("^C")
        main()  
if __name__ == "__main__":
    commands = ['ls', 'pwd', 'mkdir', 'rm', 'cp', 'mv',
                'cat', 'less', 'head', 'tail', 'grep', 'find',
                'chmod', 'chown', 'tar', 'wget', 'ssh', 'ps',
                'kill', 'top', 'ifconfig', 'ping', 'netstat',
                'df', 'du', 'scp', 'crontab', 'yum']
    os.chdir(current_file_path)
    if os.path.exists("system_files"):
        login()

    else:
        dos = read_install()
        print(dos)
        time.sleep(1)
        clear()
        print("""
        ██ 
██     ██  
       ██  
██     ██  
        ██ 
Shiter can't find system file. 
0x000001
please re-install Shiter.""")
        time.sleep(10)
