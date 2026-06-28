from pymodbus.client import ModbusTcpClient
import sys

ip = sys.argv[1]
# Configure connection
client = ModbusTcpClient(ip, port=502)

if client.connect():
    # Read Holding Registers (FC03)
    response = client.read_holding_registers(address=0, count=20, slave=1)
    if not response.isError():
        print("Registers:", response.registers)
    
    # Write Register (FC06)
    client.write_register(0,65535)
    
    result = client.write_coil(15,False)
    # Read Coils (FC01)
   # response = client.read_coils(address=0, count=20, slave=1) 
   # print("Coil Status:", response.bits[0])
    client.close()

