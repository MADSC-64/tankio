

#Gets Data From Http Request
def decodeHttpMessage(msg):
    lines = msg.splitlines()

    #Get URL from Request Line
    url = lines[0].split(" ")[1]

    print(url)
