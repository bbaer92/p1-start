import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename, delimiter= ",", skiprows=32)   # Attempts to load filename into local variable data.

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.
	#python plot.py ______ function no longer errors when running. Continuing. 

## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)

Stress= data[:,3]
Strain= data[:,7]

plt.plot(Strain,Stress,color="k",linestyle="--",label='raw data')
plt.title('Stress vs Strain')
plt.xlabel('Strain [Exten.] %')
plt.ylabel('Stress (MPa)')

## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable
	#Unable to view graph due to remote operation.
	# I believe I need to set up Tunneling access between SSH source to 
	#allow the transfer of diplays but unsure how.
	# No Syntax errors so continuing. 

## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)

Slope,y_int = np.polyfit(Strain,Stress,1)
linear_fit = np.poly1d((Slope,y_int))
plt.plot(Strain,linear_fit(Strain),color='r',label="linear regression")
plt.legend(loc='best')
plt.show();
## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.
