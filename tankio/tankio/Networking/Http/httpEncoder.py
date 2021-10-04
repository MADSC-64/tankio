
def generate_Http_response(method,url,content):

    response = f'{method} {url} HTTP/1.1\nHost host:5005\nContent-Type: text/plain\nContent-Length:{len(content)}\n\n{content}'

    return response






