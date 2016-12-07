import os
import re
import sys
import platform
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

import tkMessageBox

class SnowRanScan(object):

  def main_run(self, m_folder, save_it):  
    mod_folder = m_folder.strip('\n').replace('\"', '') 
    check = SnowRanScan().find_bad_files(mod_folder, save_it)
    amount_c = str(len(check))    
    return "Found %s total infected files\nHere are the files\n  %s\n" %(amount_c, ' '.join(map(str, check)))

  def find_bad_files(self, folder, save_it):
    known_ext = re.compile('.*\.(ecc|ezz|exx|zzz|locky|micro|zepto|cerber3|axx|ecc|ezz|exx|crypz|cerber2|odin|cryptowall|enciphered|cryptolocker|cryp1|breaking_bad|LeChiffre|aesir|enigma|rrk|zzzzz|zzzz|coverton|good|wflx|crjoker|enc|crinf|windows10|zyklon|pdcr|abc|EnCiPhErEd|xyz|kkk|fantom|PoAr2w|pzdc|odcodc|legion|darkness|payms|crptrgr|czvxce|btc|kraken|bitstalk|rdm|magic|SecureCrypted|73i87A|vvv|CCCRRRPPP|kernel_time|kernel_complete|cry|rokku|payrms|globe|venusf|purge|kernel_pid|pays|kratos|paymts|fun|padcrypt|locklock|p5tkjw|1txt|szf|unabailable|shit|realfsOciety@sigaint.org.fsOciety|dharma|paymst|herbst|rekt|kimcilware|raid10|R16m01d05|kimcilware|raid10|nuclear56|lock93|dCrypt|coded|xyz|aaa|abc|ccc|vvv|xxx|ttt|micro|encrypted|locked|crypto|_crypt|lol|crinf|r5a|XRNT|XTBL|crypt|R16M01D05|pzdc|good|LOL!|OMG!|RDM|RRK|encryptedRSA|crjoker|EnCiPhErEd|LeChiffre|keybtc@inbox_com|0x0|bleep|1999|vault|HA3|toxcrypt|magic|SUPERCRYPT|CTBL|CTB2|locky|)$')
    inf_list = []
    if platform.system() == 'Windows':
      win_dir = SnowRanScan().convert_folder_windows(folder)
      for root, dirnames, filenames in os.walk(win_dir):
       for filename in filter(lambda name:known_ext.match(name),filenames):          
           inf_list.append(os.path.join(root, filename))
    else:
      lin_dir = folder
      for root, dirnames, filenames in os.walk(lin_dir):
       for filename in filter(lambda name:known_ext.match(name),filenames):
           inf_list.append(os.path.join(root, filename))
    if save_it == 1:
      SnowRanScan().save_results_to_file(inf_list)  
    
    return inf_list    
    
  def save_results_to_file(self, *args):
    file_to_save = open("SnowRanScanResults.txt", 'a')
    for arg in args:
      rd = map(lambda x: x + '\n', arg)
      for xd in rd:
        file_to_save.writelines(xd)
    

  def convert_folder_windows(self, folder):
    win_folder = folder.replace('\\', '\\')
    return win_folder


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

root = Tk()

save_2_file = IntVar()
#root.iconbitmap(r'icon\favicon2.ico')
root.title("SnowRanScan 1.2")
root.geometry("500x125")
e1 = Entry(root)
e1.pack()
b_file = Button(root, text="Browse", command= get_file_path)
b_file.pack()

check = Checkbutton(root, text="Save", variable=save_2_file)
check.pack()
btnEnts = Button(root, text="Search", command= run_it)
btnEnts.pack()
root.bind('<Return>')

root.mainloop()




