function cutCancerCells(organism){

  return organism.replace(/c|[a-z]?C[a-z]?/g,'')

}