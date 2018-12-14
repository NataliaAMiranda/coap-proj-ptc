import coap


#.well-known/core

print('Informe a Uri')
uri = input()

print('Informa o Ip')
ip = input()

clienteCoap = coap.Coap()

clienteCoap.Get(uri,ip)