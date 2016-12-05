import os
import re
import sys
import platform
import Tkinter
import tkMessageBox

class SnowRanScan(object):

  def main_run(self, m_folder):  
    mod_folder = m_folder.strip('\n').replace('\"', '') 
    check = SnowRanScan().find_bad_files(mod_folder)
    amount_c = str(len(check))    
    return "Found %s total infected files\nHere are the files\n  %s\n" %(amount_c, ' '.join(map(str, check)))

  def find_bad_files(self, folder):
    known_ext = re.compile('.*\.(ecc|ezz|exx|zzz|locky|micro|zepto|cerber3|axx|ecc|ezz|exx|crypz|cerber2|odin|cryptowall|enciphered|cryptolocker|cryp1|breaking_bad|LeChiffre|aesir|enigma|rrk|zzzzz|zzzz|coverton|good|wflx|crjoker|enc|crinf|windows10|zyklon|pdcr|abc|EnCiPhErEd|xyz|kkk|fantom|PoAr2w|pzdc|odcodc|legion|darkness|payms|crptrgr|czvxce|btc|kraken|bitstalk|rdm|magic|SecureCrypted|73i87A|vvv|CCCRRRPPP|kernel_time|kernel_complete|cry|rokku|payrms|globe|venusf|purge|kernel_pid|pays|kratos|paymts|fun|padcrypt|locklock|p5tkjw|1txt|szf|unabailable|shit|realfsOciety@sigaint.org.fsOciety|dharma|paymst|herbst|rekt|kimcilware|raid10|R16m01d05|kimcilware|raid10|nuclear56|lock93|dCrypt|coded|xyz|aaa|abc|ccc|vvv|xxx|ttt|micro|encrypted|locked|crypto|_crypt|crinf|r5a|XRNT|XTBL|crypt|R16M01D05|pzdc|good|LOL!|OMG!|RDM|RRK|encryptedRSA|crjoker|EnCiPhErEd|LeChiffre|keybtc@inbox_com|0x0|bleep|1999|vault|HA3|toxcrypt|magic|SUPERCRYPT|CTBL|CTB2|locky|)$')
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

    return inf_list    
    
       

  def convert_folder_windows(self, folder):
    win_folder = folder.replace('\\', '\\')
    return win_folder

okToPressEnter = True

def run_it():
  folder = e1.get()
  x = SnowRanScan().main_run(folder)
  if len(x) > 1:
    infected_y(x)
  else:
    infected_n("No infected files :)")
          

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
      for f in funcs:
        f(*args, **kwargs)
    return combined_func

def infected_y(infe):
   tkMessageBox.showinfo("infected files", infe)

def infected_n(infe):
   tkMessageBox.showinfo("infected files", infe)   

root = Tkinter.Tk()
root.title("")
root.geometry("300x300")
m_label = Tkinter.Label(root, text="SnowRanScan", font=('Helvetica', 15))
m_label.pack()
e1 = Tkinter.Entry(root)
e1label = Tkinter.Label(root, text="Folder", font=('Helvetica', 12))
e1.pack()
e1label.pack()
btnEnts = Tkinter.Button(root, text="Search", command= run_it)
btnEnts.pack()
root.bind('<Return>')

root.mainloop()




