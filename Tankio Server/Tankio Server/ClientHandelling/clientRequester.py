import Http.httpDecoder as decoder
import Http.httpEncoder as encoder
import json

def perform_request(request):
    #request_body = decoder.decodeHttpMessage(request)

    #response = get_response(request_body)

    encoder.generate_Http_response("200 OK","test")


def get_response(request_body):
    print("")
