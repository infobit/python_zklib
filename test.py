from zklib import zklib



maquina = zklib.ZKLib(ip='192.168.188.202', port=4370)
maquina.connect()


print maquina.getAttendance()

maquina.disconnect()
