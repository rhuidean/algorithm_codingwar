function cutCancerCells(organism){
  
  //first cut out of advanced stage cancer cell
  organism=organism.replace(/[a-z]C[a-z]/g,"");

  //second cut out of advanced stage cancer cell
  organism=organism.replace(/[a-z]C/g,"");

  //third cut out of advanced stage cancer cell
  organism=organism.replace(/C[a-z]/g,"");
  
  //fourth cut of advanced stage cancer cell
  organism=organism.replace(/C/g,"");  
 
  //final cut of cancer
  organism=organism.replace(/c/g,"");
  return organism
 
}