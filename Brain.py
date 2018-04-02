import Neurons as neur

class Brain():
    def __init__(self,xsize,ysize,zsize):
        self.xmax = xsize
        self.ymax = ysize
        self.zmax = zsize
        self.xcoord = range(1,(self.xmax + 1))
        self.ycoord = range(1, (self.ymax + 1))
        self.zcoord = range(1, (self.zmax + 1))

        self.neuraldictionary = {}

        self.energytotal = 100
        self.passiveenergyloss = 1
    def add_processor(self,neuron_object,object_coordinates):
        self.newdictionaryentry = {(object_coordinates[0],object_coordinates[1],object_coordinates[2]):
                                   neuron_object}
        self.neuraldictionary.update(self.newdictionaryentry)
    def populate_grid(self):
        self.currentcount = 1
        self.dictsize = self.xmax * self.ymax * self.zmax
        self.neuraldictionary = {}
        self.current_listpos = 1
        self.current_xpos  = 1
        self.current_ypos = 1
        self.current_zpos = 1
        for neuron in range(1,(self.dictsize + 1)):
            self.neuraldictionary.update({(self.current_xpos, self.current_ypos, self.current_zpos):
                                              neur.DigiNeuron(x=self.current_xpos,y=self.current_ypos,
                                                              z=self.current_zpos)})
            if self.current_ypos > self.ymax:
                self.current_xpos = 1
                self.current_ypos = 1
                self.current_zpos = self.current_zpos + 1
            elif self.current_xpos > self.xmax:
                self.current_xpos = 1
                self.current_ypos = self.current_ypos + 1
            elif self.current_xpos < self.xmax:
                self.current_xpos = self.current_xpos + 1
    def passive_energy(self):
        self.energytotal = self.energytotal - self.passiveenergyloss
        if self.energytotal <= 0:
            self.network_death()
    def network_death(self):
