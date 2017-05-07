# -*- coding: utf-8 -*-
import cx_Oracle
import pprint

def rows_as_dicts(cursor):
   colnames = [i[0] for i in cursor.description]
   for row in cursor:
     yield dict(zip(colnames, row))

try:
 con = cx_Oracle.connect('ttcoe2/ttcoe2@172.25.40.253/exchdb')
finally:
 try:
   print con.version
   cur = con.cursor()
   #cur.execute('select * from VERSION_INFO')
   cur.execute("select EVENT_DATE, EVENT_TIME, EVENT_TYPE, EVENT_ID, USER_ID, REASON from ATS_MM_ACTIVITY_LOG where EVENT_ID = -6 and EVENT_DATE = '2015/06/28'")
   #row = cur.fetchone()
   #print row
   #rows = cur.fetchmany(numRows=3)

   col_names = []
   for i in range(0, len(cur.description)):
       col_names.append(cur.description[i][0])
   #pp = pprint.PrettyPrinter(width=1024)
   #pp.pprint(col_names)

   for row in rows_as_dicts(cur):
      item1 = row["col1"]
      item2 = row["col2"]
      print "%s, $s",item1,item2;

   #   for i in col_names:
   #     print result[i];

   #   print

   cur.close()
   con.close()
 except:
   pass
