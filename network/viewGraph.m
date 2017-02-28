M = csvread('actors_colleagues.csv',0,0);
sz=size(M);
G=graph;
for i=1:sz(1)
    for j=1:sz(2)
        if(M(i,j)>0)
            G = addedge(G,i,j,M(i,j));
        end
    end
end
%G=graph(ones(4) - diag([1 1 1 1]))

plot(G,'EdgeLabel',G.Edges.Weight)

