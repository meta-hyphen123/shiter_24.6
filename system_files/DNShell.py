import os
import subprocess
from rich import print
from rich.console import Console

# 设置颜色
console = Console()

logo = """
usage: DNS-shell.py [-h] [-l] [-r RECURSIVE] [-d DIRECT]"""

# 使用颜色设置
colored_logo = f"[bold #CF6417]{logo}[/bold #CF6417]"

print(logo)

# 获取当前脚本所在的目录
directory_path = os.path.dirname(os.path.abspath(__file__))

def run_sqlmap(user_input):
    if user_input.lower() == 'exit':
        exit()

    else:
    

        try:
            # 切换到指定目录
            os.chdir(directory_path)

            # 构建命令，将用户输入作为参数传递给 sqlmap.py
            command = ["python", "DNS-shell.py"] + user_input.split()

            # 在命令行中运行命令
            subprocess.run(command)

        except FileNotFoundError:
            console.print("", style="bold red")
        except subprocess.CalledProcessError as e:
            console.print(f"", style="bold red")
        except Exception as e:
            console.print(f"", style="bold red")
yellow = '\33[46m '
none = '\33[0m'
while True:
    shitermaininput = yellow + "dns shell" +  none+":#"

    # 用户输入的参数
    user_input = input(shitermaininput)

    # 检查用户输入是否为 "exit"
    if user_input.lower() == "exit":
        break  # 如果是 "exit"，则退出循环

    else:# 运行程序，并将用户输入作为参数传递

        run_sqlmap(user_input)
