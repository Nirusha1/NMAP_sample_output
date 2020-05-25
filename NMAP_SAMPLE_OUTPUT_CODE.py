from datetime import datetime
import pytz


timezone_now=pytz.timezone('Asia/Kathmandu')
lh="127.0.0.1"
port_list=[4330,9050,902,631,4000,43435,18083,44321,44322,43291]


def look_at_time():
    current_time=datetime.now(timezone_now)
    return current_time

def time_conversion(time_to_convert):
    hh,mm=map(int,time_to_convert.split(':'))
    time_converted=hh*100+mm
    return time_converted

def test():
    initiating_time=look_at_time().strftime('%H:%M')
    initiating_time_converted=time_conversion(initiating_time)
    print(f"Initiating NSE at {initiating_time}")
    completion_time=look_at_time().strftime('%H:%M')
    completion_time_converted=time_conversion(completion_time)
    elapsed_time=completion_time_converted-initiating_time_converted
    print(f"Completed NSE at {completion_time},{elapsed_time}s elapsed")

print(f"Starting Nmap 7.80 (https://nmap.org) at {look_at_time().strftime('%Y-%m-%d %H:%M')} EST") 
print("NSE:Loaded 151 scripts for scanning")
print("NSE:Script Pre-scanning")
test()
test()
test()
print(f"Scanning localhost ({lh}) [2 ports]")
initiating_time=look_at_time().strftime('%H:%M')
initiating_time_converted=time_conversion(initiating_time)
print(f"Initiating Ping Scan at {initiating_time}")
completion_time=look_at_time().strftime('%H:%M')
completion_time_converted=time_conversion(completion_time)
elapsed_time=completion_time_converted-initiating_time_converted
print(f"Completed Ping Scan at {completion_time},{elapsed_time}s elapsed (1 total hosts)")
print(f"Initiating Connect Scan at {look_at_time().strftime('%H:%M')}")
print(f"Scanning localhost {lh} [65535 ports]")
print(f"Completed Ping Scan at {look_at_time().strftime('%H:%M')}")
for i in port_list:
    print(f"Discovered open port {i}/tcp on {lh}")







