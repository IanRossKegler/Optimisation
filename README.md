# Optimisation
Optimisation of Dyson Library - DE4 Optimisation Project 

This code was used towards a paper outlining an optimisation of the Dyson Library for generalised acoustic performance. Both gradient based and non-gradient based algorithms were used to optimise the material properties of the walls, height of the ceiling, properties of added sound absorbing materials, number of receivers, position of source and receiver layout.

# The Study 

The goal of the study was to generate a novel seating layout for acoustic performance for the Dyson Library. In this model subsystem 1 (SS1) alters material and geometric parameters of the room to optimize its reverberation properties for music and speech. It also generates an optimum number of seated people. This parameter is used directly in the second subsystem (SS2) which generates a source position and layout based on the delay of first order reflections and the sound pressure level (SPL) at the receiver. There is an anticipated trade-off between the number of audience members required (and therefore the size of the layout) and the minimum required SPL.

# Software

Matlab 2018a in addition to Global Optimisation Toolbox https://uk.mathworks.com/products/global-optimization.html

# Fmincon and GlobalSearch

execute [opt_scrit_effKVDF](https://github.com/Kvdf/Optimisation/blob/master/Sub_system1/opt_scrit_effKVDF.m) to run fmincon and GlobalSearch algorithm.

# Gradient Descent 

execute [grad_descentOPTI](https://github.com/Kvdf/Optimisation/blob/master/Sub_system1/grad_descentOPTI.m) to run gradient descent algorithm.

# Run with
operation time *1.133 seconds* 
MacOS, 2.2 GHz Intel Core i7, 2400 MHz DDR4. 

