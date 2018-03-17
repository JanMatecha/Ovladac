import network
"""
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active()
ap_if.active()
ap_if.ifconfig()

sta_if.active(True)

sta_if.connect('A', '000AABB87DA6C')
sta_if.isconnected()
sta_if.ifconfig()
"""

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('A', '000AABB87DA6C')
        while not sta_if.isconnected():
            pass
    text = 'network config:', sta_if.ifconfig()
    print(text)
    return text
