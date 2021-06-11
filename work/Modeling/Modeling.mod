
// Variables
int place = ...;
int candidate = ...;
range ps = 1..place;
range cs = 1..candidate;

tuple poss {
   key int necsite;
   key int cand;
}

int c[cs] = ...;

{poss} Poss = ...;

 // D.V
dvar boolean y[cs] ;
 
// obj.to
 maximize 
   
   sum(j in cs) c[j]*y[j];
 

// subj.to
 subject to{
  
 
   forall(i in ps)   sum( <i ,j > in Poss) y[j] >= 1;
   
   sum(j in cs) y[j] == 6; 
   
 }                                                                      
 
 
  execute DISPLAY {
    for(var j in cs )
    if(y[j] > 0) write(j); 
} 
                                                               
 
 
 
 
 
 
                 