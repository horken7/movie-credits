function [ ] = PageRank( )
clc;
clear;

adjMat = csvread('actors_colleagues.csv');

index = 1:length(adjMat);
index = index';

% We want actors = colleagues
nRows = size(adjMat, 1); % number of colleagues
nCols = size(adjMat, 2); % number of actors

if nRows ~= nCols
    fprintf('Error: This matrix is not symmetrical! Therefore, this is not an adjacency matrix.');
end

% Amount of actor pairings with weight = 0
w0 = sum(adjMat(:)==0);

% Input Values
P = 0.85;            % P is a scalar damping factor
A = adjMat;          % adjacency matrix
d = 1;               % vector containing the out-degree of each node in the graph
n = nRows;           % scalar number of nodes in the graph
s = w0;              % scalar sum of PageRank scores for pages with no links

%% PageRank Algorithm

rold = ones(nRows, 1);
for i = 1:100
    rnew = (1-P)./n + P*(A'*(rold./d) + s./n); % r is a vector of PageRank scores
    rComp = abs(rnew - rold);
    rCompTot = sum(rComp);
    
    rold = rnew;
end
rnew;

%% Plot

for k1 = 1:nRows
    for k2 = 1:nCols
        adjPlot = adjMat(k1,k2);
    end
end

G = digraph(index,index);
plot(G,'Layout','force');


%% Top Actors

pRank = [index, rComp];
order = sortrows(pRank,[-2 1]);

num = 5;
topNum = zeros(num,1);
for i=1:num
    topNumList = [order(i,1)];
    vec = topNum(i,:) + topNumList;
    topNum(i,:) = vec;
end

topNum;

end