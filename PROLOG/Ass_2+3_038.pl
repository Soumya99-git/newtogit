male(suman).
male(pradip).
male(joy).
male(rajib).
male(sudip).

female(ritu).
female(amita).
female(mita).
female(dipti).

parent(suman,pradip).
parent(suman,mita).
parent(ritu,pradip).
parent(ritu,mita).
parent(pradip,joy).
parent(pradip,rajib).
parent(amita,joy).
parent(amita,rajib).
parent(dipti,sudip).
parent(rajib,sudip).


father(X,Y):-parent(X,Y),male(X).

grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandfather(X,Y):-grandparent(X,Y),male(X).
grandchild(X,Y):-parent(Z,X),parent(Y,Z).

brother(X,Y):-parent(Z,Y),parent(Z,X),male(X),X\==Y.
sister(X,Y):-parent(Z,Y),parent(Z,X),female(X),X\==Y.

predecessor(X,Y):-parent(X,Y).
predecessor(X,Y):-parent(X,Z),predecessor(Z,Y).

successor(X,Y):-parent(Y,X).
successor(X,Y):-parent(Y,Z),successor(X,Z),X\==Y.
