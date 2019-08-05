X= repmat([3 6 9 12],[4,1]);
Y= repmat([7.11 9.51 14.25 28.2]',[1,4]);
Z= [75592.25, 100206.1, 153244.2, 314200.2;
    76578.25, 101961.35, 152531.25, 315635.45;
    76660.55, 102696.05, 154587.85, 318920.95;
    77362.85, 102513.2, 155200.8, 321368.65];

Z2 = abs(inpaint_nans(Z));
[X3,Y3] = meshgrid(3:1:12,7.11:0.1:28.2);
Z3 = interp2(X,Y,Z2',X3,Y3);
Z3 = Z3/1000;
surf(X3,Y3,Z3)
%set(gca,'zscale','log')

title('Total response time')
xlabel('Number of nodes')
ylabel('Size of the data set (billions of rows)')
zlabel('Runtime (s)')
