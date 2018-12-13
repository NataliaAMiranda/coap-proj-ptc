import socket	
from enum import Enum

# parametros de controle para transmissao de mensagens 
# sao valores padrao
ACK_TIMEOUT = 2.0

ACK_RANDOM_FACTOR = 1.5

MAX_RETRANSMIT = 4

NSTART = 1


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
		self.payload = b''
		self.quadro = b''
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def GET():
		
	def POST():
		
	def PUT():
		
	def DELETE():
		
