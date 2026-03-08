import socket

t = "167.0.0.1"

print("scanning...")

for p in range(1,1024):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((t,p))
        print("port open ->",p)
    except:
        pass

    s.close()

print("done")
