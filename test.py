from zklib import zklib



maquina = zklib.ZKLib(ip='10.0.8.11', port=4370)
maquina.connect()


print maquina.getAttendance()

maquina.disconnect()