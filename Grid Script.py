class BrainMap():
    def __init__(self,xsize,ysize,zsize):
        self.xmax = xsize
        self.ymax = ysize
        self.zmax = zsize
        self.xcoord = range(1,(self.xmax + 1))
        self.ycoord = range(1, (self.ymax + 1))
        self.zcoord = range(1, (self.zmax + 1))
        self.neuraldictionary = {}
        self.energytotal = 1
    def Add_Neuron(self,DigiNeuron_Object,Coordinates):
        self.newdictionaryentry = {DigiNeuron_Object:Coordinates}
        self.neuraldictionary.update(self.newdictionaryentry)
    def Populate_Grid(self):
        self.currentcount = 1
        self.listsize = self.xmax * self.ymax * self.zmax
        self.neurallist = [DigiNeuron() for n in list(range(1,(self.listsize + 1)))]

        self.current_listpos = 1
        self.current_xpos  = 1
        self.current_ypos = 1
        self.current_zpos = 1
        for neuron in self.neurallist:
            neuron.Set_Position(x=self.current_xpos,y=self.current_ypos,z=self.current_zpos)
            if self.current_ypos > self.ymax:
                self.current_xpos = 1
                self.current_ypos = 1
                self.current_zpos = self.current_zpos + 1
            elif self.current_xpos > self.xmax:
                self.current_xpos = 1
                self.current_ypos = self.current_ypos + 1
            elif self.current_xpos < self.xmax:
                self.current_xpos = self.current_xpos + 1
        self.sensorywall = 1
        self.sensoryrange = range(((self.sensorywall * self.xmax * self.ymax) + 1),( ( (self.sensorywall + 1) * self.xmax * self.ymax) + 1))
        for n in self.sensoryrange:
            self.neurallist[(n + 1)].Set_Neural_Class('Sensory')

        self.xmid = round(self.xmax/2)
        self.ymid = round(self.ymax/2)
        self.harvestpos = self.zmax * self.ymid * self.xmid
