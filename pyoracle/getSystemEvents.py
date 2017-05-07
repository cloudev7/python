# -*- coding: utf-8 -*-
import cx_Oracle
import pprint
import json
import calendar, time
import sys
import os

def getEpochSeconds():
  return calendar.timegm(time.strptime('11 18 2016 11:30:00', '%m %d %Y %H:%M:%S'))



try:
 con = cx_Oracle.connect('ttcoe2/ttcoe2@172.25.40.253/exchdb')
finally:
 try:
   print con.version
   cur = con.cursor()
   #cur.execute('select * from VERSION_INFO')
   #cur.execute("select EVENT_DATE, EVENT_TIME, EVENT_TYPE, EVENT_ID, USER_ID, REASON from ATS_MM_ACTIVITY_LOG where EVENT_ID = -6 and EVENT_DATE = '2015/06/28'")
   cur.execute("select EVENT_DATE, EVENT_TIME, EVENT_TYPE, EVENT_ID, USER_ID, REASON from ATS_MM_ACTIVITY_LOG WHERE EVENT_DATE = '2015/06/28'")
   #row = cur.fetchone()
   #print row
   #rows = cur.fetchmany(numRows=3)
   #rows = cur.fetchall()

   col_names = []
   for i in range(0, len(cur.description)):
       col_names.append(cur.description[i][0])
   #pp = pprint.PrettyPrinter(width=1024)
   #pp.pprint(col_names)

   print len(col_names);
   for row in cur:

      dt = row[0].split("/");
      #dts = str(dt[1])+" "+str(dt[2])+" "+str(dt[0])
      dts = "11 18 2016 "
      tm = row[1].split(":");
      tms = str(tm[0])+":"+str(tm[1])+":"+str(tm[2])
      timestamp=dts+" "+tms
      epochtime = calendar.timegm(time.strptime(timestamp, '%m %d %Y %H:%M:%S'))

      txt='{ "@timestamp" : "' + str(epochtime) + '"'

      sep=", "
      for i in range(0,6): 
        txt=txt + sep + '"' + str(col_names[i])+ '" : "' + str(row[i]) + '"'
      txt=txt+" }"
      print txt
      os.system("curl -XPOST http://localhost:9200/exchange/events -d '"+txt+"'");

   cur.close()
   con.close()
 except:
   pass
