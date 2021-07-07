f = open("ROM.bin","w+")
s=chr(3)+chr(3)+chr(1)+chr(0)+chr(192)+chr(0)+chr(24)+chr(8)+chr(8)+chr(0)+chr(15)+chr(0)+chr(96)+chr(96)+chr(0)+chr(24)+chr(16)+chr(0)+chr(240)+chr(160)+chr(0)+chr(48)+chr(0)+chr(15)+chr(3)+chr(1)+chr(0)+chr(240)+chr(15)+chr(0)
f.write(s)
f.close()

'''
Please keep the first two inputs positive numbers in order for the circuit to work(The first one if garbage). And just give a single zero between different blocks.
'''
