import socket
from enum import Enum
import os, sys

# parametros de controle para transmissao de mensagens
# sao valores padrao

ACK_TIMEOUT = 2.0

ACK_RANDOM_FACTOR = 1.5

MAX_RETRANSMIT = 4

NSTART = 1

PORTA = 5683


class TipoMensagem(Enum):
	CON = b'\x00'  # confirmacao destino
	NON = b'\x10'  # nao confirmacao destino
	ACK = b'\x20'  # confirmacao de recebimento
	RST = b'\x30'  # mensagem recebida com erro

class Requisicao(Enum):
	EMPTY_MSG = b'\x00'
	GET = b'/x01'    # solicita ao webserver
	POST = b'/x02'   # cria um recurso no webserver.
	PUT = b'/x03'    # muda o estado de um recurso do webserver
	DELETE = b'/x04' # remove o recurso ou alterar para um estado vazio
	
class Confirmacao(Enum):
	CREATED =  b'\x41'
	DELETED =  b'\x42'
	VALID =  b'\x43'
	CHANGED =  b'\x44'
	CONTENT = b'\x45'
	

class Erro_Cliente(Enum):
	BAD_REQUEST =  b'\x80'
	UNAUTHORIZED = b'\x81'
	BAD_OPTION = b'\x82'
	FORBIDDEN =  b'\x83'
	NFOUND =  b'\x84'
	METHOD_NALLOW =  b'\x85'
	NACCEPTABLE =  b'\x86'
	PRECONDITION_FAILED =  b'\x8C'
	REQUEST_ENTITY_TLARGE =  b'\x8D'
	UNSUPPORTED_FORMAT =  b'\x8F'
	

class Erro_Servidor(Enum):
	INTERNAL_SERVER_ERR =  b'\xA0'
	NIMPLEMENT =  b'\xA1'
	BAD_GW =  b'\xA2'
	SERVICE_UNAVAILABLE =  b'\xA3'
	GW_TIMEOUT =  b'\xA4'
	PROXYING_NSUPPORTED =  b'\xA5'
	
	
class Delta(Enum):
	IF_MATC =  b'\x01'
	URI_HOST =  b'\x03'
	ETAG =  b'\x04'
	IF_NONE_MATCH =  b'\x05'
	URI_PORT =  b'\x07'
	LOCATION_PATH =  b'\x08'
	URI_PATH =  b'\x0B'
	CONTENT_FORMAT =  b'\x0C'
	MAX_AGE =  b'\x0E'
	URI_QUERY =  b'\x0F'
	ACCEPT =  b'\x11'
	LOCATION_QUERY =  b'\x14'
	PROXY_URI =  b'\x23'
	PROXY_SCHEME =  b'\x27'
	SIZE1 = B'\x3C'
	

class Coap:
	def __init__(self):
		# ver = versao sempre 40
		# tipo = TipoMensagem
		# token = utilizado para controle de requisições e repostas (0 e 8 bytes)
		# code = separados em 3-bit mais significativos para classes e 5-bits menos significativos para detalhe
                    # payload usada para deduplicação de mensagens e confirmacao ou reset de mensagens.
                    self.ver = b'\x40'
                    self.tipo = b'\x00'
                    self.token = b'\x00'
                    self.code = b'\x00'
                    self.IdMensagem = b'\x00'
                    self.delta = b'\x00'
		self.tamanho = b'\x00'
		self.opcoes = b'\x00'
		self.payload = b'OlaMundo!'
		self.quadro = b''
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		
		
	def GeraIdMsg(self):
                    idM = os.urandom(2)
                    return idM

          def QuadroPayload(self, IdMsg):
                    self.quadro = b''
		self.IdMensagem = IdMsg
		self.quadro = (self.ver[0] | self.tipo[0] | self.token[0]).to_bytes(1, byteorder='big')
		self.quadro += self.codigo + self.IdMensagem
		self.quadro += (self.delta[0] << 4 | self.tamanho).to_bytes(1, byteorder='big')
		self.quadro += self.opcoes + self.payload

          def Quadro(self, IdMsg):
                    self.quadro = b''
                    self.IdMensagem = IdMsg
		self.quadro = (self.ver[0] | self.tipo[0] | self.token[0]).to_bytes(1, byteorder='big')
		self.quadro += self.codigo + self.IdMensagem
		self.quadro += (self.delta[0] << 4 | self.tamanho).to_bytes(1, byteorder='big')
		self.quadro += self.opcoes

	def Get(self, uri, host):
                    origem = (host, PORTA)
		self.tipo = TipoMensagem.CON.value
		self.codigo = Requisicao.GET.value
		self.tamanho = len(uri)
		self.opcoes = uri
		self.delta = Delta.URI_PATH.value
		self.host = host
		
		# Montando quadro get
		IdM = self.GeraIdMsg()
		self.Quadro(IdM)
		
		print('\n---------------------------\n')
		print('Quadro: ' + (self.quadro))
		print('\n---------------------------\n')
		
		# Envia socket
		self.sock.sendto(self.quadro, origem)
		
		# Aguarda resposta
		mensagem , endereco = self.sock.recvfrom(1024)
		print('IP: ' + (endereco))
		print('Mensagem: ' + (mensagem))
		
	def Post(self, uri, host):
	          origem = (host, PORTA)
		self.tipo = TipoMensagem.CON.value
		self.codigo = Requisicao.POST.value
		self.tamanho = len(uri)
		self.opcoes = uri
		self.delta = Delta.URI_PATH.value
		self.payload = payload
		self.host = host
		
		# Montando quadro get
		IdM = self.GeraIdMsg()
		self.QuadroPayload(IdM)
		
		print('\n---------------------------\n')
		print('Quadro: ' + (self.quadro))
		print('\n---------------------------\n')
		
		# Envia socket
		self.sock.sendto(self.quadro, origem)
		
		# Aguarda resposta
		mensagem , endereco = self.sock.recvfrom(1024)
		print('IP: ' + (endereco))
		print('Mensagem: ' + (mensagem))
		
	def Put(self, uri, host):
	          origem = (host, PORTA)
		self.tipo = TipoMensagem.CON.value
		self.codigo = Requisicao.PUT.value
		self.tamanho = len(uri)
		self.opcoes = uri
		self.delta = Delta.URI_PATH.value
		self.payload = payload
		self.host = host
		
		# Montando quadro get
		IdM = self.GeraIdMsg()
		self.QuadroPayload(IdM)
		
		print('\n---------------------------\n')
		print('Quadro: ' + (self.quadro))
		print('\n---------------------------\n')
		
		# Envia socket
		self.sock.sendto(self.quadro, origem)
		
		# Aguarda resposta
		mensagem , endereco = self.sock.recvfrom(1024)
		print('IP: ' + (endereco))
		print('Mensagem: ' + (mensagem))
		
	def Delete(self, uri, host):
                    origem = (host, PORTA)
		self.tipo = TipoMensagem.CON.value
		self.codigo = Requisicao.DELETE.value
		self.tamanho = len(uri)
		self.opcoes = uri
		self.delta = Delta.URI_PATH.value
		self.host = host
		
		# Montando quadro get
		IdM = self.GeraIdMsg()
		self.Quadro(IdM)
		
		print('\n---------------------------\n')
		print('Quadro: ' + (self.quadro))
		print('\n---------------------------\n')
		
		# Envia socket
		self.sock.sendto(self.quadro, origem)
		
		# Aguarda resposta
		mensagem , endereco = self.sock.recvfrom(1024)
		print('IP: ' + (endereco))
		print('Mensagem: ' + (mensagem))