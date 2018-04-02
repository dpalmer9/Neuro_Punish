
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
		self.firestate = 0
		# -1 Inhibited, 0 Neutral, 1 Fire
		self.firetype = 0
		# -1 Inhibitory, 0 Non-Active, 1 Excitatory
		
		self.orientation = [1,1]
		#-1-1 SenseF MotorR;-10 SenseR MotorL
		#0-1 DownF UpR; 00 INVALID
		#10 SenseL MotorR; 01 DownR UpF
		#11 MotorF, SenseR
		self.connections = []

	def report_firestate(self):
		return(self.firestate)
	def modify_firestate(self,value):
		self.firestate = value

	def report_firetype(self):
		return(self.firetype)
	def modify_firetype(self,value):
		self.firetype = value

	def modify_orientation(self,pos1,pos2):
		self.orientation = [pos1,pos2]

	def report_output(self):
		return(self.connections)
	def add_output(self,xcord,ycord,zcord):
		self.connections.append([xcord,ycord,zcord])
	def remove_output(self,xcord,ycord,zcord):
		self.remove_target = [xcord,ycord,zcord]
		self.connections.remove(self.remove_target)

		
	
 
class Neuro_central_processor():
	def __init__(self):
		self.neuron_cyclemax = 0
		self.active_neurons = 0
		self.input_address = []
		for trit in range(0,3):
			self.fire_input_address.append(0)
		self.fire_input_firetype = 0

	def attach_nam(self,nam):
		self.nam = nam

	def reduce_cycle(self):
		self.cyclemax -= 1

	def reduce_cycle_custom(self,reduce_amount):
		self.cyclemax = self.cyclemax - reduce_amount

	def increase_cycle_custom(self, increase_amount):
		self.cyclemax = self.cyclemax + increase_amount

	def activate_new_neuron(self,coordinates):
		self.nam[[x]][[y]][[z]].modify_firetype()
	def fire_neuron(self,source_coord):
		self.nam[]

class Neuro_address_memory():
	def __init__(self):
		self.trit_address = []
		for trit in range(0, 9):
			self.trit_address.append(Trit())


class Neuro_memory():
	def __init__(self):
		self.nam_storage = []

	def initialize_nam(self,x,y,z):
		self.nam_list_sub1 = []
		self.nam_list_sub2 = []
		for zcord in range(0,z):
			self.nam_list_sub2.append(Digineuron2)
		for ycord in range(0,y):
			self.nam_list_sub1.append(self.nam_list_sub2)
		for xcord in range(0,x):
			self.nam_storage.append(self.nam_list_sub1)

####################################
nam1 = Neuro_memory() # Initialize memory
nam1.initialize_nam(51,51,51) # Specify 51x51x51 Array

npu1 = Neuro_central_processor() # Initialize NPU
npu1.attach_nam(nam1) #Attach NAM to Processor
nam1 = 0 # Destroy Original NAM



