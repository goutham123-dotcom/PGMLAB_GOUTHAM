import time
print("current time in sec:",time.time())
print("current time:",time.ctime())
print("current time after 30 sec:",time.ctime(time.time()+30))
t=time.localtime()
print("time:",t)
print("current Year:",t.tm_year)
print("current Month:",t.tm_mon)
print("current Day:",t.tm_mday)
print("current Hour:",t.tm_hour)
print("current week:",t.tm_wday)
print("Day of Year:",t.tm_yday) 
print("formated time:",time.strftime("%d /%m /%y    %H:%M:%S    %Y ",t))
print("formated time:",time.strftime("%c    %H:%M:%S    %Y ",t)) 

