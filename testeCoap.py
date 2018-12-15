import coap
import os
import sys

#.well-known/core

print('Informe a Uri')
uri = input()

print('Informa o Ip')
ip = input()

clienteCoap = coap.Coap()
uri_bytes = uri
clienteCoap.Get(uri_bytes,ip)
#clienteCoap.Post(uri_bytes,ip)
