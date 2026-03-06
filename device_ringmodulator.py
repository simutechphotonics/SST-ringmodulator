import ansys.lumerical.core as lumapi

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
        self.configuration_halfring = False #bool, draws a half_ring device instead
        self.configuration_racetrack = False #bool, draws a racetrack device instead
        self.ring_racetrack_length = 5 #um, length of the racetrack coupling section
        self.slab_thickness = 0  # um, use 0 for strip waveguides.
        # Simulation region
        self.sim_width = 2.0e-6  # um, span amount around wg
        self.sim_height = 1.0e-6  # um,  span amount around wg
        # Materials, in Lumerical name format
        self.material_uppercladding = "SiO2 (Glass) - Palik"
        self.material_lowercladding = "SiO2 (Glass) - Palik"
        self.material_wg = "Si (Silicon) - Palik"

    def setup_device(self,fdtd):
        fdtd.RingFunctions() #this requires RingFunctions.lsf to be in the current directory or search path
        fdtd.setup_RingModulator(
        thick_Si,
        width_Si,
        thick_Clad,
        thick_BOX,
        sidewall_angle,
        ring_radius,
        gap,
        wavelength_start,
        wavelength_stop,
        racetrack_length,
        thick_Slab,
        bool_half_ring,
        bool_racetrack,
        sim_width,
        sim_height,
        material_Clad,
        material_BOX,
        material_Si,
        Zmin,
        Zmax
        )

    def run_simulation(self):
        pass

    def run_sparam_sweep(self):
        pass

    def simulate_fdtd(self):
        fdtd = lumapi.FDTD  # declare fdtd object
        self.setup_device(fdtd)

if __name__ == "__main__":
    MyRing = DeviceRingModulator()
    MyRing.simulate_fdtd()