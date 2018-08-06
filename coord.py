vta = ''
class Coord():
	"""Input X,Y Coordinates"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.coords = (self.x,self.y)

	def __str__(self):
		return '{'+str(self.x)+','+str(self.y)+'}'

	def __getitem__(self, position):
		self.coords[position]

class Graph():
	"""Graph Out Coordinates"""
	def __init__(self, xlen=10, ylen=10):
		self.xlen = xlen*2
		self.ylen = ylen*2
		self.total = ylen*xlen*4
		self.line2 = '6'
		self.data = [['. '] for i in range(self.total) if ylen == xlen and ylen%2 == 0]
		self.gdata = int(((self.total//4)**0.5))
		self.line = str(('. '*(self.gdata)))
		self.half = str((self.line+'| '+self.line+'\n')*self.gdata)
		self.mline = str(('––'*self.gdata)+'+'+('––'*self.gdata))+'\n'
		self.graph = self.half+self.mline+self.half

	def datgraph(self):
		global vta
		endline = False
		for n,i in enumerate(self.data):
			vta += str(i[0])
			if (n+1) % self.gdata == 0 and n+1 != 0:

				print(1)
				if ((n+1)/self.gdata) % 1 == 0 and endline == False:
					print(2)
					vta += '| '
					endline = True
				elif ((n+1)/self.gdata) % 1 == 0 and endline == True:
					print(3)
					vta += '\n'
					endline = False
					print(n)
					if n+1 == self.total/2:
						vta += (' —'*(self.gdata*2))+'\n'
	def addpoint(self, coords):
		x,y = coords
		self.data[int(2*self.gdata**2-2*self.gdata*y+self.gdata+x-1)][0]='o '
	#def matgraph(self):
	#	return self.matgraph
	def __len__(self):
		return len(self.data)

	def __getitem__(self, position):
		return self.data[position]

c = Coord(2,7)
g = Graph(8,8)
g.addpoint(c.coords)
g.addpoint((5,3))
g.addpoint((-1,1))
#g[0].insert(0,5)
print(g.data)
g.datgraph()
print(vta)