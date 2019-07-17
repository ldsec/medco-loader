X= repmat([1 5 10 25 50 100],[8,1]);
Y= repmat([7 52 150 451 585 940 1366 1511]',[1,6]);
Z=[773.32, 2060.64, 4364.54, 11387.88, 14367.74, 22074.04, 30283.7, 33912.3;
   1795.56, NaN, 18274.42, NaN, 66450.3, NaN, 142159.9, NaN;
   NaN, 14052.88, NaN, 101787.8, NaN, 203333.4, NaN, 314200.2;
   6573.55, NaN, 87225.5, NaN, 325984.7, NaN, 701851.7, NaN;
   NaN, 68134.1, NaN, 501835.9, NaN, 1021297.4, NaN, 1562792.0;
   24194.7, NaN, 345820, NaN, 1302635.0, NaN, 2807409.2, NaN];

Z2 = abs(inpaint_nans(Z));
[X3,Y3] = meshgrid(1:2:100,7:15:1511);
Z3 = interp2(X,Y,Z2',X3,Y3);
Z3 = Z3/1000;
surf(X3,Y3,log10(Z3))

xlabel('Number of query terms')
ylabel('Size of the result set')
zlabel('Runtime (s)')
