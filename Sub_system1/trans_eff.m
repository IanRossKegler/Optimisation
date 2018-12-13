%% Defining function to be used in opt_scrit_effKVDF
function y = trans_eff(X)

mw = X(1);
mb = X(2);
h = X(3);
n = X(4);
%absorption coefficients room materials octave 1kHz, units % 
octave1floor = 0.15; 
octave1emptychair = 0.07;
octave1seatedpeople = 0.76;
octave1ceiling = 0.03;


%Other room parameters 
V = 14 * 17 * h; %volume in m^3
c20 = 343; %speed of sound at 20 degrees in dry air 
sw = (2 * 14 * 4) + (2 * 17 *4); %surface area wall 
sr = 14 * 17; %surface area roof 
sf = 14 * 17; %surface area floor 
sh = 1.9; %surface area human
sc = 0.4; % surface area chair 
sb = (2*14*2) + (2*14*0.3) ; % surface area designed absorption barrier 

%RT60 desired time, in seconds (energy dissipation quanitification) 
RT60M = 1.2; %RT60 music tone
RT60S = 0.6; %RT60 speech intelligibility

y = (RT60M - ((24 * log(10))/c20)*(V/(sw*mw+sr*octave1ceiling+sf*octave1floor+n*sh*octave1seatedpeople+sc*octave1emptychair+0*sb*mb)))^2 + (RT60S - ((24 * log(10))/c20)*(V/(sw*mw+sr*octave1ceiling+sf*octave1floor+n*sh*octave1seatedpeople+sc*octave1emptychair+sb*mb)))^2;
end 




