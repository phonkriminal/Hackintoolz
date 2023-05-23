import shutil
import tkinter as tk
import os
from _githubdownload import get_appfiles
from _download import check_url
from tkinter import filedialog
from tkinter import messagebox
from _extract import extract_tar

url_path = 'https://raw.githubusercontent.com/phonkriminal/Hackintoolz/main/Binaries/Hackintools.tar'
install_path = ''
source_dir = os.path.realpath(os.getcwd())
print(source_dir)
exit_code = 0
exit_code = check_url(url_path)



x = 1
root = tk.Tk()
root.withdraw()

if (exit_code == 200):
    msgbox = messagebox.askokcancel('Connection Found.', 'Would you proceed to installation?')
    if (msgbox == False):
        exit()

while x > 0:
    install_path = filedialog.askdirectory()
    if (len(install_path)) > 0: 
         print(install_path)
         x -=1
    else:
        msgbox = messagebox.askokcancel('Warning!!!', 'No folder was selected\nWould you proceed to installation?')
        if (msgbox == False):
            exit()

print ('Starting Download...')
get_appfiles(url_path)
print('Download Completed!')
print('Decompressing Files...')

    #dest_dir = install_path + "/Hackintools"      
    
    #shutil.copytree(source_dir, dest_dir, copy_function=shutil.copy2, dirs_exist_ok = True) 
    
extract_tar(source_dir + '/Hackintools.tar', install_path)
    
print('Completed.')
os.remove(source_dir + '/Hackintools.tar')
print('Binaries Removed.')
exit()