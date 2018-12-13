%Absorption coefficient parameters
octave1floor = 0.15; 
octave1emptychair = 0.07;
octave1seatedpeople = 0.76;
octave1ceiling = 0.03;

%Physical parameters
c20 = 343; %speed of sound at 20 degrees in dry air 

%Surface area parameters 
V = 14 * 17 * 4; %volume in m^3
sw = (2 * 14 * 4) + (2 * 17 *4); %surface area wall 
sr = 14 * 17; %surface area roof 
sf = 14 * 17; %surface area floor 
sh = 1.9; %surface area human
sc = 0.4; % surface area chair 
sb = (2*14*2) + (2*14*0.3) ; % surface area designed absorption barrier 

%RT60 desired time, in seconds (desired reverberation time) 
RT60M = 1.2; %RT60 musical tone
RT60S = 0.6; %RT60 speech intelligibility



% run code to find gradient of your objective function, that will be your input into line 103
% grad_descentOPTI.m
syms x y 
f = (RT60M - ((24 * log(10))/c20)*(V/(sw*x+sr*octave1ceiling+sf*octave1floor+sh*octave1seatedpeople+sc*octave1emptychair+0*sb*y)))^2 + (RT60S - ((24 * log(10))/c20)*(V/(sw*x+sr*octave1ceiling+sf*octave1floor+sh*octave1seatedpeople+sc*octave1emptychair+sb*y)))^2;
gradient(f, [x, y])

