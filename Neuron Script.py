class DigiNeuron():
    def __init__(self,xpos,ypos,type,strength):
        self.xpos = xpos
        self.ypos = ypos
        self.threshold = 100
        self.resource = 100
        self.type = type
        self.strength  = strength
        if self.type == "inhibitory":
            if self.strength == "weak":
                self.power = -25
            if self.strength == "strong":
                self.power = -50
        elif self.type == "excitatory":
            if self.strength == "weak":
                self.power = 25
            if self.strength == "strong":
                self.power = 50

class DigiNeuron():
    def __init__(self):
        self.energy = 1
        self.firestate = 0
        self.inputlist = {}
        self.outputlist = {}

        self.neuralclass = 'Undifferentiated'


        self.xsize = 1
        self.ysize = 1
        self.zsise = 1
    def Set_Position(self,x,y,z):
        self.xpos = x
        self.ypos = y
        self.zpos = z
    def Add_Input(self,InputNeuron):
        self.newentry = {InputNeuron:0.5}
        self.inputlist.update(self.newentry)
    def Remove_Input(self,InputNeuron):
        del self.inputlist[InputNeuron]
    def Add_Output(self,OutputNeuron):
        self.newentry = {OutputNeuron:0.5}
        self.outputlist.update(self.newentry)
    def Remove_Output(self,OutputNeuron):
        del self.outputlist[OutputNeuron]
    def Output_Received(self,InputStrength):
        self.firestate = self.firestate + InputStrength
        if(self.firestate < -1):
            self.firestate = -1
        if(self.firestate < 1):
            self.firestate = 1
            self.Fire_Neuron()
    def Fire_Neuron(self):
        for x in self.outputlist:
            x.Output_Received(self.firestrength)
        self.energy = self.energy - self.fireexpenditure
        self.firestate = 0
    def Set_Neural_Class(self,ClassType):
        if ClassType=='Neuron':
            self.firestrength = 0.1
            self.fireexpenditure = 0.1

        if ClassType=='Sensory':
            self.inputlist = {}

        if ClassType=='Action':
            self.outputlist = {}

        if ClassType = 'Harvest':
            self.outputlist = {}
    def Prune(self):

class BasicSensor():
    def __init__(self):
        self.energy = 1
        self.detectionstate = 0
        self.firestate = 0
        self.firestrength = 0.5
        self.fireexpenditure = 0.1
        self.outputlist = []
        self.neuralclass = 'NA'
    def Add_Output(self, OutputNeuron):
        self.outputlist.append(OutputNeuron)
    def Remove_Output(self, OutputNeuron):
        self.outputlist.remove(OutputNeuron)

class BasicAction():
    def __init__(self):
        self.energy = 1
        self.detectionstate = 0
        self.firestate = 0
        self.firestrength = 0.5
        self.fireexpenditure = 0.1
        self.outputlist = {}
        def Add_Output(self, OutputNeuron):
            self.newentry = {OutputNeuron: 0.5}
            self.outputlist.update(self.newentry)
        def Remove_Output(self, OutputNeuron):
            del self.outputlist[OutputNeuron]