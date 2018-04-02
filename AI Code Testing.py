class Digineuron2():
    def __init__(self):
        self.firestate = 0
        # -1 Inhibited < 0 Neutral < 1 Fire
        self.firetype = 0
        # -1 Inhibitory < 0 Non-Active < 1 Excitatory

        self.orientation = [1, 1]
        # -1-1 SenseF MotorR;-10 SenseR MotorL
        # 0-1 DownF UpR; 00 INVALID
        # 10 SenseL MotorR; 01 DownR UpF
        # 11 MotorF, SenseR
        self.connections = {}

        self.synapse_modifier = 0.1

        self.output_controlled = False
        self.input_controlled = False

    def report_firestate(self):
        return (self.firestate)

    def modify_firestate(self, value):
        self.firestate = value

    def report_firetype(self):
        return (self.firetype)

    def modify_firetype(self, value):
        self.firetype = value

    def modify_orientation(self, pos1, pos2):
        self.orientation = [pos1, pos2]

    def report_output(self):
        return (self.connections)

    def add_output(self, xcord, ycord, zcord):
        self.connections.update({(xcord, ycord, zcord):0.1})

    def strengthen_output(self, xcord, ycord, zcord):
        self.connections[(xcord, ycord, zcord)] += self.synapse_modifier

    def weaken_output(self, xcord, ycord, zcord):
        self.connections[(xcord, ycord, zcord)] -= self.synapse_modifier

    def remove_output(self, xcord, ycord, zcord):
        self.remove_target = (xcord, ycord, zcord)
        del self.connections[self.remove_target]

    def set_output(self):
        self.output_controlled = True
    def set_input(self):
        self.input_controlled = True


class Brain():
    def __init__(self,xsize,ysize,zsize):
        self.xmax = xsize
        self.ymax = ysize
        self.zmax = zsize
        self.xcoord = range(1,(self.xmax + 1))
        self.ycoord = range(1, (self.ymax + 1))
        self.zcoord = range(1, (self.zmax + 1))

        self.neuraldictionary = {}

        self.energytotal = 1
        self.passiveenergyloss = 1

        self.inputdict = {}
        self.outputdict = {}

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
                                              Digineuron2(x=self.current_xpos,y=self.current_ypos,
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

    def set_input(self,label,xpos,ypos,zpos):
        self.inputdict.update({label:(xpos,ypos,zpos)})
        self.neuraldictionary[(xpos,ypos,zpos)]
    def set_output(self,label,pos):
        self.outputdict.update({label:(xpos,ypos,zpos)})