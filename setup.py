import os
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path, 'system_files')
os.chdir(tools_folder)
os.system("py unzip")
os.system("python3 unzip")
