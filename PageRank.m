function [ r ] = PageRank( )

clc;
clear;

adjMat = csvread('actors_colleagues.csv');
% adjMat = csvread('testAdj.csv');

% We want actors = colleagues
nRows = size(adjMat, 1); % number of colleagues
nCols = size(adjMat, 2); % number of actors

if nRows ~= nCols
    fprintf('Error: This matrix is not symmetrical! Therefore, this is not an adjacency matrix.');
end

% Amount of actor pairings with weight = 0
w0 = sum(adjMat(:)==0);

% Input Values
P = 0.85;                               % P is a scalar damping factor
A = adjMat;                             % adjacency matrix
d = 1;                                  % vector containing the out-degree of each node in the graph
n = nRows;                              % scalar number of nodes in the graph
s = w0;                                 % scalar sum of PageRank scores for pages with no links

% PageRank Algorithm
% r = (1-P)/n + P.*(A'.*(r./d) + s/n) % r is a vector of PageRank scores

% Rearranged for r
r = ((1-P)./n + P.*(s./n))./(1-(P*A')./d);

end