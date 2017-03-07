function [  ] = weight( )

clc;
clear;

weight = csvread('weight_index.csv');

% Sort weighted column in terms of top actors
weight = sortrows(weight,[-3 1]);
weight = sortrows(weight,[-1 1]);

totLen = length(weight);

actorCol = weight(:,1);
colleagueCol = weight(:,2);
weightCol = weight(:,3);

actors = sort(unique(actorCol), 'descend');
colleagues = sort(unique(colleagueCol),'descend');

fprintf('There are %d actors and %d colleagues.', length(actors), length(colleagues));

% weight
% actorCol
counter = 0;
oldC = 1;
for val = 1:length(actors)
    eq = weight(find(actorCol==actors(val,:)));
    l = length(eq);
    oldC;
    counter = counter + l;
    
%     a = 1;
%     if a == 1
%         indiv = zeros(l,3);
%     end
%     for iii = a:l
%         for ii = oldC:counter
%             sepA = [eq(1), colleagueCol(ii), weightCol(ii)];
%             
%             mat = indiv(iii,:) + sepA;
%             indiv(iii,:) = mat;
%             a = a + 1;
%         end
%     end
        
    for ii = oldC:counter
        indiv = zeros(l,3);
        sepA = [eq(1), colleagueCol(ii), weightCol(ii)]
        for iii = 1:l
            mat = indiv(iii,:) + sepA;
            indiv(iii,:) = sepA;
        end
    end
    oldC = counter + 1; 
    indiv
end


% indiv = zeros(l,3)
% for iii = 1:l
%     mat = indiv(iii,:) + sepA
%     indiv(iii,:) = mat
% end

num = 3;
topNum = zeros(num,3);

for i=1:num
    pairs = [actorCol(i), colleagueCol(i), weightCol(i)];
    row = topNum(i,:) + pairs;
    topNum(i,:) = row;
end
% topNum


% if actor == colleague
%     fprintf('Same');
% end

end