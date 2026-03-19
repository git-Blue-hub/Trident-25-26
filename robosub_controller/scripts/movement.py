import subprocess
import time
 
# ═══ THRUSTER TOPICS ═══
HRL = '/buoyant_robosub/thruster_hrl'  # Horizontal rear left
HRR = '/buoyant_robosub/thruster_hrr'  # Horizontal rear right
HFL = '/buoyant_robosub/thruster_hfl'  # Horizontal front left
HFR = '/buoyant_robosub/thruster_hfr'  # Horizontal front right
VL  = '/buoyant_robosub/thruster_vl'   # Vertical left
VR  = '/buoyant_robosub/thruster_vr'   # Vertical right
 
def send_thrust(topic, value):
    subprocess.run([
        'gz', 'topic',
        '-t', topic,
        '-m', 'gz.msgs.Double',
        '-p', f'data: {value}'
    ])

#Resets the thrusters back to 0 so no more forces acting upon it 
def set_thrusters(hrl=0.0, hrr=0.0, hfl=0.0, hfr=0.0, vl=0.0, vr=0.0):
    send_thrust(HRL, hrl)
    send_thrust(HRR, hrr)
    send_thrust(HFL, hfl)
    send_thrust(HFR, hfr)
    send_thrust(VL,  vl)
    send_thrust(VR,  vr)
 

#Stop runs the function above to stop it from moving
def stop():
    set_thrusters()
 
#sets teh rear thrusters to 1 for it to start moving forward
def forward(speed=1.0):
    set_thrusters(hrl=speed, hrr=speed)
 
#Sets the rear thrusters to -1 for it to go backwards 
def backward(speed=1.0):
    set_thrusters(hrl=-speed, hrr=-speed)

#rear thrusters and front right thruster is ran for it go right
def forward_left(speed=1.0,turn=0.3):
    set_thrusters(hrl=-speed, hrr=speed,hfr=turn)
 
#rear thrusters and front left thruster is ran for it to go left
def forward_right(speed=1.0,turn=0.3):
    set_thrusters(hrl=speed, hrr=-speed,hfl=turn)
 
#currently doesn't work 
def dive(speed=1.0):
    set_thrusters(vl=speed, vr=speed)
 
def rise(speed=1.0):
    set_thrusters(vl=-speed, vr=-speed)
 
def roll_left(speed=1.0):
    set_thrusters(vl=-speed, vr=speed)
 
def roll_right(speed=1.0):
    set_thrusters(vl=speed, vr=-speed)
 
#running some commands 
if __name__ == '__main__':

    print("Forward")
    forward(1.0,0.3)
    time.sleep(1)
    
    print("Stop...")
    stop()
    time.sleep(1)
 
    print("Forward left...")
    forward_left(1.0, 0.3)
    time.sleep(3)
 
    print("Stop...")
    stop()
    time.sleep(1)
 
    print("Forward right...")
    forward_right(1.0, 0.3)
    time.sleep(3)
 
    print("Stop...")
    stop()
    time.sleep(1)
    
    print("Done. Stopping all thrusters.")
    stop()