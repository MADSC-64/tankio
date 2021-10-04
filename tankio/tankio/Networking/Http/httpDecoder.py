

#Gets Data From Http Request
def decodeHttpMessage(msg):
    lines = msg.splitlines()

    #Get Data from Response Line
    response_code = lines[0]



    body = lines[len(lines)-1]

    return (method,body)



