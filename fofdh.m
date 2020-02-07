%%=================DISCRETE FORM OF NEWTONS COOLING LAW===================
% script name: fofdh.m
% variables: 
% uk = temperature of well sturred liquid,
% usur = surrounding room temperature,
% h = small changes in time,
% c = measure of the apertures (e.g. a cup) insulation
% uk+1 - uk = ch(usur - uk)
% uk+1 = (1 - ch)uk +ch*usur
% or, uk+1 = A*uk + B; A = 1 - ch & B = ch*usur
%
% as k increases, uk should converge to usur
% when usur = constant, uk will converge monotonically to usur
%for this to happen, impose the statbility condition:
% 0 < A = 1 - ch
%%=========================================================================

% The code belows applies the first order finite difference algorithm
% to Newtons law of cooling 

t(1) = 0; %initial time
h = 1; %time step
n = 300; %number of time steps of length h
h_obs = 5; %time of observation
u(1) = 200; %initial temperature
u_obs = 190; %observed temperature at observed time h_obs
usur = 70;
c = ((u_obs - u(1))/h_obs)/(usur - u(1));
A = 1 - c*h;
B = c*h*usur;
%
% run the algorithm 
%
for k = 1:n
    
    u(k+1) = A*u(k) + B;
    t(k+1) = t(k)+ h;
    
end

%plot results
plot(t,u,'r')
xlabel('Time (s)')
ylabel(['Temperature ' char(176) ' F'])
title('Application of the First Order Finite Difference Algorithm to Newtons Law of Cooling')
ax = gca;
ax.TitleFontSizeMultiplier = 1;









