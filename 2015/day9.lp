% Generate
1{start(X) : node(X)}1.
1{end(Y) : node(Y)}1.
:- start(X), end(X). % starting and ending in the same place will never be optimal
{ cycle(X,Y) : edge(X,Y) } = 1 :- end(Y).
{ cycle(X,Y) : edge(X,Y) } = 1 :- cycle(Y,_), not start(Y).

% Define
reached(X) :- start(X).
reached(Y) :- cycle(X,Y), start(X).
reached(Y) :- cycle(X,Y), reached(X).
% Test
:- node(Y), not reached(Y).
% Display
#show cycle/2.
#show start/1.
#show end/1.

% Optimize
#minimize { C,X,Y : cycle(X,Y), cost(X,Y,C) }.

% Nodes
node(S) :- cost(_,S,_).
% (Directed) Edges
edge(A,B) :- cost(A,B,_).

cost(I,J,C) :- cost(J,I,C).

% Edge Costs
% cost(london, dublin, 464).
% cost(london, belfast, 518).
% cost(dublin, belfast, 141).

cost(faerun, tristram, 65).
cost(faerun, tambi, 129).
cost(faerun, norrath, 144).
cost(faerun, snowdin, 71).
cost(faerun, straylight, 137).
cost(faerun, alphacentauri, 3).
cost(faerun, arbre, 149).
cost(tristram, tambi, 63).
cost(tristram, norrath, 4).
cost(tristram, snowdin, 105).
cost(tristram, straylight, 125).
cost(tristram, alphacentauri, 55).
cost(tristram, arbre, 14).
cost(tambi, norrath, 68).
cost(tambi, snowdin, 52).
cost(tambi, straylight, 65).
cost(tambi, alphacentauri, 22).
cost(tambi, arbre, 143).
cost(norrath, snowdin, 8).
cost(norrath, straylight, 23).
cost(norrath, alphacentauri, 136).
cost(norrath, arbre, 115).
cost(snowdin, straylight, 101).
cost(snowdin, alphacentauri, 84).
cost(snowdin, arbre, 96).
cost(straylight, alphacentauri, 107).
cost(straylight, arbre, 14).
cost(alphacentauri, arbre, 46).