patternCount <- function(text,pattern) {
  count <- 0
  for(i in 1:(nchar(text)-nchar(pattern))) {
    if(substr(text,i,i+nchar(pattern)-1) == pattern) {
      count <- count + 1 
    }
  }
  return(count)
}

frequentWords <- function(text,k) {
  frequentPatterns <- c()
  count <- rep(0,nchar(text)-k)
  for(i in 1:(nchar(text)-k)) {
    pattern <- substr(text,i,i+k-1)
    count[i] <- patternCount(text,pattern)
  }
  for(i in 1:(nchar(text)-k)) {
    if(count[i] == max(count)) {
      pattern <- substr(text,i,i+k-1)
      frequentPatterns <- append(frequentPatterns, pattern)
    }
  }
  frequentPatterns <- unique(frequentPatterns)
  return(frequentPatterns)
}