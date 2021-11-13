
x_human = [] % read in maker center position
xd_human = [] % read in marker center veloctiy
x_exo = [] % read in marker side position
xd_exo = [] % read in marker side velocity


% get the delta vectors
delta_x = x_human - x_exo
delta_xd = xd_human - xd_exo
tf = 1;
%fit polynomals to the delta equations for interpolation
t =  linspace(0, tf, 10000);
poly_x = polyfit(t,delta_x,15);
poly_xd = polyfit(t,delta_xd,15);

% set up opt varibles
A = []
B = []
Aeq = []
Beq = []
lb = [800;80];
ub = [8000;500];
x0 = [6000,100]; % Initial guess

% run the optimzation
sol = fmincon(@objective,x0,A,b,Aeq,beq,lb,ub)


% model function
function dydt = model(t,y,K,B)
  dydt = zeros(2,1);
  dydt(1) = y(2);
  dydt(2) = K*poly_x(t) + B*poly_xd(t);
end


% objective funtion
function f = objective(x)
    % Get the optimization vars
    K = x(1)
    B = x(2)
    
    % set up the initial state of the model 
    x0 = [x_human(1);xd_human(1)];
    
    % run the model 
    sol = ode45(@model,[0,tf],x0, K, B);
    % get the RMSE error
    path = sol.x(1,:);
    f = sum(sqrt( (path - x_human).^2)) ; 
   
end
