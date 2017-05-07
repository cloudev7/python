# -*- coding: utf-8 -*-
import cx_Oracle
import pprint
import json
import calendar, time
import sys
import os

def getEpochSeconds():
  return calendar.timegm(time.strptime('11 18 2016 11:30:00', '%m %d %Y %H:%M:%S'))

dictActions = {
  "3001": "Start Day",
  "3002": "End Day",
  "3003": "Start Market",
  "3004": "End Market",

  "3005": "Change Schedule",
  "3006": "Start Session",
  "3007": "Manual Session Start",
  "3008": "Session End",
  "3010": "Request Day Status",
  "3011": "Query Schedules",
  "3012": "Notify Dirty",
  "3013": "Change Schedule With Session Start",
  "3014": "Reset Schedule"
}

try:
 con = cx_Oracle.connect('ttcoe2yaan/ttcoe2yaan@172.25.40.253/exchdb')

finally:
 try:
   print con.version
   cur = con.cursor()
   cur.execute("select TIMESTAMP, ACTION, OWNER, DESCRIPTION, REJECT_REASON FROM AUDIT_TRAIL WHERE CATEGORY = 'Market Manager' and REJECT_REASON is NULL")

   col_names = []
   for i in range(0, len(cur.description)):
       col_names.append(cur.description[i][0])

   print len(col_names);
   for row in cur:

      dt = row[0].split("-");
      dts = str(dt[0][4:6])+" "+str(dt[0][6:8])+" "+str(dt[0][0:4])

      tm = dt[1].split(":");
      tms = str(tm[0])+":"+str(tm[1])+":"+str(tm[2])
      timestamp=dts+" "+tms

      epochtime = calendar.timegm(time.strptime(timestamp, '%m %d %Y %H:%M:%S'))

      txt='{ "@timestamp" : "' + str(epochtime) + '"'
      sep=", "

      for i in range(0,5): 

	if ( i == 1 ):
          action = row[1];

          for key in dictActions:
            if ( key == str(action) ):
	      action = dictActions[str(key)]
              txt=txt + sep + '"' + str(col_names[i])+ '" : "' + str(action) + '"'
	      break
        else:        
          txt=txt + sep + '"' + str(col_names[i])+ '" : "' + str(row[i]) + '"'

      txt=txt+" }"
      print txt

   cur.close()
   con.close()
 except:
   pass

