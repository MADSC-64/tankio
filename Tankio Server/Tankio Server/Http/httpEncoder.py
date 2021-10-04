def generate_Http_response(response_code,content):

    response = f'HTTP/1.1 {response_code}\nCache-Control: no-cache\nServer: libnhttpd\ntext/plain\nContent-Length:{len(content)}\n\n{content}'

    return response






