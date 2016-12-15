import re
import os
import sys
import sqlite3 as lite

class FetchRanExt(object):


  def grab_data(self):

    set_db_in_desktop = os.path.expanduser("~/Desktop/RanExt.db")

    ext = []

    con = lite.connect(set_db_in_desktop)

    with con:    
    
      cur = con.cursor()    
      cur.execute("SELECT * FROM RanExt")

      rows = cur.fetchall()
      for row in rows:
        ext.append(row[0])
        
    make_re = '|'.join(ext)


    known_ext = re.compile('.*\.(|{}|)$'.format(make_re.encode('utf-8')))

    return known_ext
   
        
  def ok_ext(self): 
    set_db_in_desktop = os.path.expanduser("~/Desktop/RanExt.db")

    ext = []

    con = lite.connect(set_db_in_desktop)

    with con:

      cur = con.cursor()
      cur.execute("SELECT * FROM OkExt")

      rows = cur.fetchall()
      for row in rows:
        ext.append(row[0])

    return tuple(ext)


FetchRanExt().ok_ext()
