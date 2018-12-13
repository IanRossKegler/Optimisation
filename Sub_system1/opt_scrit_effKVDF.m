clear
clc


FUN = @(X)trans_eff(X);
%Setting initial starting point, to orientate and initialise gradient-step
X0 = [0.09 ; 0.60; (3) ; 80];
%Inequality constraints, Ax>-B
A = [1/(0.8*(248)) 64.4 0 0; 0 0 17 0; 0 0 (-1) 0; 0 0 0 0];  
B = [1;952;(-2.1); 0];
%Bounded constraints, lower and upper bound
LB = [0.08 0.18 2.1 40];
UB = [0.12 0.75 4 100];

%% Fmincon -- in combination with GlobalSearch machine learning
options = optimset('MaxFunEvals',Inf,'MaxIter',10000,...
    'Algorithm','interior-point','Display','iter', ...
    'PlotFcn', {@optimplotfval});
%Uncomment below, to run sqp 
%options = optimoptions('fmincon','Display','iter','Algorithm','sqp');

%To find fmicon minimum values without GlobalSearch, type Xopt in command
%window
[Xopt, min_inveff, E, O, ~, Grad, Hess] = fmincon(FUN,X0,A,B,[],[],LB,UB,[],options);
 
%Generate Trial Points; searching for a global minimum 
rng default % For reproducibility
gs = GlobalSearch;
acoustics = @(X)trans_eff(X);
problem = createOptimProblem('fmincon','x0',[0.09 ; 0.60; (3) ; 80],...
    'objective',acoustics,'lb',[0.08 0.18 2.1 40],'ub',[0.12 0.75 4 100]);

x = run(gs,problem)
hold on 
plot(0.08, 0.75);
hold off



