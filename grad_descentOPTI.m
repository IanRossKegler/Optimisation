function [xopt,fopt,niter,gnorm,dx] = grad_descent(varargin)
% grad_descent.m demonstrates how the gradient descent method can be used
% to solve a simple unconstrained optimization problem. Taking large step
% sizes can lead to algorithm instability. The variable alpha below
% specifies the fixed step size. Increasing alpha above 0.32 results in
% instability of the algorithm. An alternative approach would involve a
% variable step size determined through line search.
%
% This example was used originally for an optimization demonstration in ME
% 149, Engineering System Design Optimization, a graduate course taught at
% Tufts University in the Mechanical Engineering Department.
%
% Author: James T. Allison, Assistant Professor, University of Illinois at
% Urbana-Champaign
% Date: 3/4/12
%Note: This has been used towards a university optimization module
%coursework. Additional inputs; refer to calcgradient.m in the github folder. 

if nargin==0
    % define starting point
    x0 = [0.2 0.2]';
elseif nargin==1
    % if a single input argument is provided, it is a user-defined starting
    % point.
    x0 = varargin{1};
else
    error('Incorrect number of input arguments.')
end

% termination tolerance
tol = 1e-6;

% maximum number of allowed iterations, 10000-100000 no major changes
maxiter = 10000;

% minimum allowed perturbation
dxmin = 1e-6;

% step size ( 0.33 causes instability, 0.1 quite accurate)
alpha = 0.1;

% initialize gradient norm, optimization vector, iteration counter, perturbation
gnorm = inf; x = x0; niter = 0; dx = inf;


%absorption coefficients room materials octave 1kHz, units % 
octave1floor = 0.15; 
octave1emptychair = 0.07;
octave1seatedpeople = 0.76;
octave1ceiling = 0.03;


%Other room parameters 
V = 14 * 17 * 4; %volume in m^3
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


f = @(mw,mb) (RT60M - ((24 .* log(10))./c20).*(V./(sw.*mw+sr.*octave1ceiling+sf.*octave1floor+sh.*octave1seatedpeople+sc.*octave1emptychair+0.*sb.*mb)))^2 + (RT60S - ((24 .* log(10))./c20).*(V./(sw.*mw+sr.*octave1ceiling+sf.*octave1floor+sh.*octave1seatedpeople+sc.*octave1emptychair+sb.*mb)))^2;

% plot objective function contours for visualization:
figure(1); clf; ezcontour(f,[-1.0 1.0 -1.0 1.0]); axis equal; hold on
%title('Plot of Objective function contours between -1 and 1')
% redefine objective function syntax for use with optimization:
f2 = @(x) f(x(1),x(2));

% gradient descent algorithm:
while and(gnorm>=tol, and(niter <= maxiter, dx >= dxmin))
    % calculate gradient:
    g = grad(x);
    gnorm = norm(g);
    % take step:
    xnew = x - alpha*g;
    % check step
    if ~isfinite(xnew)
        display(['Number of iterations: ' num2str(niter)])
        error('x is inf or NaN')
    end
    % plot current point
    plot([x(1) xnew(1)],[x(2) xnew(2)],'ko-')
    refresh
    % update termination metrics
    niter = niter + 1;
    dx = norm(xnew-x);
    x = xnew;
    
end
xopt = x;
fopt = f2(xopt);
niter = niter - 1;

% define the gradient of the objective, refer to calcgradient.m 
function g = grad(x)
g = [- (10706837995693590345*(345381870828825495/(2251799813685248*(248*x(1) + (322*x(2))/5 + 5539/125)) - 3/5))/(140737488355328*(248*x(1) + (322*x(2))/5 + 5539/125)^2) - (10706837995693590345*(345381870828825495/(2251799813685248*(248*x(1) + 5539/125)) - 6/5))/(140737488355328*(248*x(1) + 5539/125)^2)
                                                                                                                                   -(11121296240688180939*(345381870828825495/(2251799813685248*(248*x(1) + (322*x(2))/5 + 5539/125)) - 3/5))/(562949953421312*(248*x(1) + (322*x(2))/5 + 5539/125)^2)];


