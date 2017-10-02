syms n f g

n = linspace(-1, 10);

%a
%{
f = n.^0.25;
g = n.^0.5;
%}

%b
%{
f = log10(n.^2);
g = log(n);
%}

%c
%{
f = n.*log10(n);
g = n.*sqrt(n);
%}

%d
%{
f = 4.^n;
g = 3.^n;
%}

%e
%{
f = 2.^n;
g = 2.^(n+1);
%}

%f
%{
f = 2.^n;
g = sym('n!');
%}


f = exp(0.332.*n);
g = n.^3.38;


hold on;
plot(n, f, n, g, '--');
%set(gca, 'YScale', 'log')
%ylabel('f(n) = n as solid line; g(n) = n log(n) as dashed line')
xlabel('n [-1, 10]')
legend('f(n)', 'g(n)')
hold off;