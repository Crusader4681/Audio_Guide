
def gps():

    import gpsd
    import time
    gpsd.connect
    time.sleep(20) 
    #gives time gor gps to connect
    packet = gpsd.get_current()
    values = packet.position()
    return (values)
    
