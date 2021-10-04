

#Gets Data From Http Request
def decodeHttpMessage(msg):
    lines = msg.splitlines()

    #Get Data from Request Line
    request_parts = lines[0].split(" ")

    url = request_parts[1]
    type = request_parts[0]

    body = lines[len(lines)-1]

    print((url,type,body))

    return (url,type,body)



