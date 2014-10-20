patternCount <- function(filename) {
  file <- file(filename,open="r")
  lines <- readLines(file,n=2)
  text <- lines[1]
  pattern <- lines[2]
  count <- 0
  for(i in 1:nchar(text)-nchar(pattern)) {
    if(substr(text,i,i+nchar(pattern)-1) == pattern) {
      count <- count + 1 
    }
  }
  return(count)
}