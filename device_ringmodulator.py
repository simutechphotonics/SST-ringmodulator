import ansys.lumerical.core as lumapi
import os.path

from pydantic.v1.parse import load_file


class DeviceRingModulator:
    def __init__(self):
        self.wg_thickness = 0.22 #um, depth of the waveguide
        self.wg_width = 0.50 #um, width of the waveguide
        self.uppercladding_thickness = 2.0 #um, depth of the top oxide cladding
        self.lowercladding_thickness = 2.0 #um, depth of the buried oxide cladding
        self.sidewall_angle = 90 #angle, sidewall angle of the waveguide components
        self.ring_radius = 10 #um
        self.ring_gap = 0.2 #um
        self.wavelength_start = 1.5 #um
        self.wavelength_stop = 1.6 #um
        self.ring_racetrack_length = 5 #um, length of the racetrack coupling section
        self.slab_thickness = 0  # um, use 0 for strip waveguides.
        # Simulation region
        self.sim_width = 2.0e-6  # um, span amount around wg
        self.sim_height = 1.0e-6  # um,  span amount around wg
        # Materials, in Lumerical name format
        self.material_uppercladding = "SiO2 (Glass) - Palik"
        self.material_lowercladding = "SiO2 (Glass) - Palik"
        self.material_wg = "Si (Silicon) - Palik"

    def load_file(self,fspfilename = "device_ringmodulator.fsp"):
        #creates the fsp file if it doesn't exist, otherwise, loads the existing file.
        # returns the FDTD object associated with that file
        if os.path.isfile(fspfilename):
            return lumapi.FDTD(filename = fspfilename)
        else:
            return lumapi.FDTD()

    def setup_device(self,fdtd):
        function = open("RingFunctions.lsf").read() #loads the lsf file
        #function = "?1+1;?2+2;"
        fdtd.eval(function) #execute the contents of the lsf file
        #fdtd.feval("RingFunctions.lsf")
        # Use setup script's function
        fdtd.setup_RingModulator(
            self.wg_thickness,
            self.wg_width,
            self.uppercladding_thickness,
            self.lowercladding_thickness,
            self.sidewall_angle,
            self.ring_radius,
            self.ring_gap,
            self.ring_racetrack_length,
            self.wavelength_start,
            self.wavelength_stop,
            self.slab_thickness,
            self.sim_width,
            self.sim_height,
            self.material_uppercladding,
            self.material_lowercladding,
            self.material_wg
        )

    def run_simulation(self,fdtd):
        fdtd.run()

    def run_sparam_sweep(self,fdtd):
        fdtd.runsweep("SParam")
        fdtd.exportsweep("SParam","sparam_ringmodulator.dat","lumerical")

    def main(self):
        fdtd = self.load_file()  # get FDTD object
        self.setup_device(fdtd) # set up device geometry
        fdtd.save("test.fsp") #save file
        self.run_sparam_sweep(fdtd)
        fdtd.close() #close program and release license

if __name__ == "__main__":
    MyRing = DeviceRingModulator()
    MyRing.main()