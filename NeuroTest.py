
class Bit():
	def __init__ (self):
		self.bit_value = 0
	def report(self):
		return(self.bit_value)
	def modify_positive(self):
		if self.bit_value == 0:
			self.bit_value = 1
	def modify_negative(self):
		if self.bit_value == 1:
			self.bit_value = 0
		

class Trit():
	def __init__(self):
		self.trit_value = 0
	def report(self):
		return(self.trit_value)
	def modify_positive(self):
		if self.trit_value < 1:
			self.trit_value += 1
	def modify_negative(self):
		if self.trit_value > -1:
			self.trit_value -= 1
		
class Digineuron2():
	def __init__(self,address):
		self.firestate = Trit()
		# -1 Inhibited, 0 Neutral, 1 Fire
		self.firetype = Trit()
		# -1 Inhibitory, 0 Non-Active, 1 Excitatory
		
		self.orientation = [Trit(),Trit()] 
		#-1-1 SenseF MotorF;-10 SenseR MotorL
		#0-1 DownF UpR; 00 INVALID
		#10 SenseL MotorR; 01 DownR UpF
		#11 MotorF, SenseR
		self.connections = []
		for trit in range(0, 27):
			self.connections.append(Trit())
		#Establish Trits as connection gates. -1 Closed 0 Not in use 1 Open
		#If output open, can fire
		#If input open, can receive
		
	
 
class Neuro_central_processor():
	def __init__(self):
		self.input_address = []
		for trit in range(0,9):
			self.fire_input_address.append(Trit())
		self.fire_input_firetype = Trit()
	
	def fire_neuron(self,initial_address,output_address,gate,valence):
		if gate == -1:
			

class Neuro_address_memory():
	def __init__(self):
		self.trit_address = []
		for trit in range(0, 9):
			self.trit_address.append(Trit())


class Neuro_memory():
	def __init__(self,xdim,ydim,zdim):
		self.brain_list =