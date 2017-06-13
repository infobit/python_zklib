import sys
from zklib import zklib
from zklib import zkconst
from zklib import zkuser
import time



zk = zklib.ZKLib("192.168.188.202", 4370)
ret = zk.connect()
print "connection:", ret
if ret:
	print "conectado ..."
	#zk.enableDevice()
	zk.disableDevice()
	#zk.clearUser()

	
	print "Crear usuario ..."
	zk.setUser(uid=10, userid='5', name='Saul Ventura', password='12345', role=zkconst.LEVEL_ADMIN)

	print "usuarios"
	data_user = zk.getUser()
	print "Get User:"
	if data_user:
	        for uid in data_user:
	            if data_user[uid][2] == 14:
        	        level = 'Admin'
	            else:
	                level = 'User'
	            print "[UID %d]: ID: %s, Name: %s, Level: %s, Password: %s" % (uid, data_user[uid][0], data_user[uid][1], level, data_user[uid][3])

	print "asistencias"
	attendance = zk.getsAtt('192.168.188.202')
	print "Get Attendance:"
	if (attendance):
        	for lattendance in attendance:
	            if lattendance[1] == 15:
	                state = 'Check In'
	            elif lattendance[1] == 0:
	                state = 'Check Out'
	            else:
	                state = 'Undefined'
		    print lattendance
	            print "date %s, Jam %s: %s, Status: %s" % (lattendance[2], lattendance[2], lattendance[0], state)

	print "desconectando..."
	zk.clearAdmin()
	zk.enableDevice()

