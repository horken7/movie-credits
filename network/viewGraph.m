%N = csvread('actors_colleagues.csv',0,0);

%M=N;
G=gr    aph(N);
plot(G,'EdgeLabel',G.Edges.Weight)
%[dist, path, pred] = graphshortestpath(G, S, T)
figure(2)
G=graph;
for j=2:size(M,1)
    for i=2:size(M,2)
        if(M(j,i)>0)
            G=addedge(G,M(j,1),M(1,i),M(j,i))
        end
    end
end
    
plot(G,'EdgeLabel',G.Edges.Weight)
