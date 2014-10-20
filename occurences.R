occurences <- function(pattern, genome) {
  output <- c()
  for(i in 1:(nchar(genome)-nchar(pattern))) {
    #if(substr(genome,i,i+nchar(pattern)-1) == pattern) {
    #  output <- append(output,i-1)
    #}
  }
  return(output)
}

occurencesFromFile <- function(filename) {
  file <- file(filename,open="r")
  lines <- readLines(file,n=2)
  pattern <- lines[1]
  genome <- lines[2]
  occurences <- occurences(pattern,genome)
  return(paste(occurences,collapse=" "))
}