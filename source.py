import openmc

# Define a thermal neutron source (0.0253 eV = 2.53e-8 MeV)
source = openmc.Source()
source.space = openmc.stats.Point((0.0, 0.0, 0.0))  # Center of geometry
source.angle = openmc.stats.Isotropic()
source.energy = openmc.stats.Discrete([2.53e-8], [1.0])  # Thermal neutrons

# Simulation settings
settings = openmc.Settings()
settings.source = source
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
settings.run_mode = 'fixed source'  # Since we're not modeling a reactor
settings.export_to_xml()
