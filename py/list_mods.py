from modulefinder import ModuleFinder
f = ModuleFinder()

fname = input("Please specify the script: ")
# Run the main script
f.run_script(fname)

# Get names of all the imported modules
names = list(f.modules.keys())

# Get a sorted list of the root modules imported
basemods = sorted(set([name.split('.')[0] for name in names]))
# Print it nicely
print("\n".join(basemods))

