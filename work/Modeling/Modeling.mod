/*********************************************
 * OPL 20.1.0.0 Model
 * Author: rudal
 * Creation Date: Jun 4, 2021 at 5:08:52 AM
 *********************************************/
int place = ...;
int candidate = ...;
range ps = 1..place;
range cs = 1..candidate;

int c[ps][cs] = ...;

 // D.V
dvar boolean y[ps][cs] ;
 
 // obj.to
 maximize sum(i in ps, j in cs) c[i][j]*y[i][j];
 
 
 //subj.to 
 subject to{
   forall(i in ps)
    sum(j in cs) y[i][j] == 1;
   sum(i in ps,j in cs) y[i][j] >= 1;     
   sum(i in ps,j in cs) y[i][j] == 7; 
 }