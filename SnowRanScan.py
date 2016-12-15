import os
import re
import sys
import ttk
import time
import glob
import platform
from Tkinter import *
from RanExtDB import * 
import Tkinter, Tkconstants, tkFileDialog

import tkMessageBox


class SnowRanScan(object):

  def main_run(self, m_folder, save_it):  
    mod_folder = m_folder.strip('\n').replace('\"', '') 
    check = SnowRanScan().find_bad_files(mod_folder, save_it)
    amount_c = str(len(check))    
    return "Found %s total infected files\nHere are the files\n  %s\n" %(amount_c, ' '.join(map(str, check)))

  def find_bad_files(self, folder, save_it):
    known_ext = FetchRanExt().grab_data()
    inf_list = []
    num_folders = 0
    if platform.system() == 'Windows':
      win_dir = SnowRanScan().convert_folder_windows(folder)
      for root, dirnames, filenames in os.walk(win_dir):
       num_folders += 1
       for filename in filter(lambda name:known_ext.search(name),filenames):          
           inf_list.append(os.path.join(root, filename))
    else:
      lin_dir = folder
      for root, dirnames, filenames in os.walk(lin_dir):
       num_folders += 1
       for filename in filter(lambda name:known_ext.search(name),filenames):
           inf_list.append(os.path.join(root, filename))
    self.update_progress_bar(num_folders) 
    if save_it == 1:
      SnowRanScan().save_results_to_file(inf_list)  
    
    filt_list = filter(lambda exc_f_type: not exc_f_type.endswith(FetchRanExt().ok_ext()), inf_list)

  
    return filt_list    
    
  def save_results_to_file(self, *args):
    file_to_save = open("SnowRanScanResults.txt", 'a')
    for arg in args:
      rd = map(lambda x: x + '\n', arg)
      for xd in rd:
        file_to_save.writelines(xd)
    

  def convert_folder_windows(self, folder):
    win_folder = folder.replace('\\', '\\')
    return win_folder

  def update_progress_bar(self, number_of_files):
   k = 0
   if number_of_files < MAX:
     number_of_files = 101 
   while k <= number_of_files:
     progress_var.set(k)
     k += 1
     time.sleep(0.001)
     root.update_idletasks()


okToPressEnter = True

def run_it():
  folder = e1.get()
  xa = save_2_file.get()
  x = SnowRanScan().main_run(folder, xa)
  if len(x) > 1:
    if xa == 1:
      infected_save()
    else:
      infected_y(x)
  else:
    infected_n("No infected files :)")



def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
      for f in funcs:
        f(*args, **kwargs)
    return combined_func

def infected_save():
   tkMessageBox.showinfo("Infected files", "Saved to file")  

def infected_y(infe):
   tkMessageBox.showinfo("Infected files", infe)

def infected_n(infe):
   tkMessageBox.showinfo("Infected files", infe)


             

def get_file_path():
  file = tkFileDialog.askdirectory()
  if file: 
    e1.delete(0,END)
    e1.insert(0,str(file))
  return

MAX = 100
root = Tk()


save_2_file = IntVar()
progress_var = DoubleVar()

#root.iconbitmap(r'icon\favicon2.ico')
root.title("SnowRanScan 1.3")
root.geometry("500x125")
e1 = Entry(root)
e1.pack()
b_file = Button(root, text="Browse", command= get_file_path)
b_file.pack()

check = Checkbutton(root, text="Save", variable=save_2_file)
check.pack()
btnEnts = Button(root, text="Search", command=run_it)
btnEnts.pack()

progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
progressbar.pack(fill=X, expand=1)
root.bind('<Return>')

root.mainloop()




