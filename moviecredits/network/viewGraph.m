
A = load('test.mat');
G = graph(double(A.x));
plot(G);
S = adjacency(G);
[dist, path, pred] = graphshortestpath(S, 111, 222)

