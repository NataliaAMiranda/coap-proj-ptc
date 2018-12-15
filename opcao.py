class opcao:
		def __init__(self, numOp):
			self.numOp = numOp
			self.tamanho = b'/x00'
			self.delta = numOp
		
		def calculoDelta(self, anterior):
			delta = self.numOp - anterior 
			return to_bytes(delta, 'big')

