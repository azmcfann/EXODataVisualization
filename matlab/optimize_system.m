

%%
% x_human = [] % read in maker center position
% xd_human = [] % read in marker center veloctiy
% x_exo = [] % read in marker side position
% xd_exo = [] % read in marker side velocity


% get the delta vectors
delta_x = x_human - x_exo
delta_xd = v_human - v_exo
tf = 1;
%fit polynomals to the delta equations for interpolation
t =  linspace(0, tf, length(delta_x));
poly_x = polyfit(t, transpose(delta_x),15);
poly_v = polyfit(t,delta_xd,15);



% set up opt varibles
A = []
b = []
Aeq = []
beq = []
lb = [800;80];
ub = [8000;500];
x0 = [6000,100]; % Initial guess

fnc_obj =  @(x)objective(x, x_human,v_human, poly_x, poly_v);

% run the optimzation
[gains,fval,exitflag,output]  = fmincon(fnc_obj,x0,A,b,Aeq,beq,lb,ub);


y0 = [x_human(1);v_human(1)];


my_path = ode45(@(t,y) model(t,y, gains(1),gains(2), poly_x, poly_v), [0 1], y0);
    

% model function
function dydt = model(t,y,K,B, poly_x, poly_v)
  dydt = zeros(2,1);
  dydt(1) = y(2);
  dydt(2) = K* polyval(poly_x,t) + B*polyval(poly_v,t);
end


% objective funtion
function f = objective(x, x_human,v_human, poly_x, poly_v)
    % Get the optimization vars
    K = x(1)
    B = x(2)
    
    % set up the initial state of the model 
    x0 = [x_human(1);v_human(1)];
    
    % run the model 
    % sol = ode45(@model,[0 1],x0, K, B, poly_x, poly_v);
    
    sol = ode45(@(t,y) model(t,y, K, B, poly_x, poly_v), [0 1], x0);
    
    % get the RMSE error
    tspane2 =  linspace(0,1, length(x_human));

    poly_human = polyfit(tspane2,x_human,15);
    poly_path = polyfit(sol.x ,sol.y(1,:),15);
    
    path_human = polyval( poly_human, tspane2);
    path = polyval( poly_path,tspane2);
    
    
    f = sum(sqrt( (path - path_human).^2))/length(x_human); 
   
end
