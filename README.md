# Scripted Simulation Template: Ring Modulator
This script is a Setup Script for Lumerical FDTD. The script generates a parameterized Ring Modulator geometry and FDTD simulation objects.

# Prerequisites
- Python 3
- PyLumerical

# Installation
Run the following commands in a command prompt to install the library requirements:
```
python -m pip install -U pip
python -m pip install ansys-lumerical-core
```

# How to use
## Lumerical
Open the `0_SetupScript.lsf` inside Lumerical FDTD, adjust parameters, and run script.

## Python
For direct running of the script:
1. In Windows, launch a command prompt and navigate to the project folder where these files are located.
2. Run the commands `python ./device_ringmodulator.py`

For integration into larger python workflows:
1. Place `device_ringmodulator.lsf` in the associated folder for the workflow script.
2. Add `import device_ringmodulator.lsf` at the top of the workflow script.
3. Initialize the device object via `MyRing = DeviceRingModulator()`.
4. (Optiona) Set variables to the device object via `MyRing.wg_thickness = 0.22`.
5. Run the setup and simulation via the built-in function `MyRing.simulate_fdtd()`

`device_ringmodulator.py` includes an example of the class' usage if directly run.

