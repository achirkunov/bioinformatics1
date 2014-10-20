symbolToNumber <- function(symbol) {
  switch(symbol, "A" = 0, "C" = 1, "G" = 2, "T"= 3)
}

numberToSymbol <- function(number) {
  switch(as.character(number), "0" = "A", "1" = "C", "2" = "G", "3" = "T")
}

patternToNumber <- function(pattern) {
  if(nchar(pattern) == 0) {
    return(0)
  }
  a <- substr(pattern, 1, nchar(pattern)-1)
  b <- substr(pattern, nchar(pattern), nchar(pattern))
  return(4*patternToNumber(a) + symbolToNumber(b))
}

numberToPattern <- function(number,k) {
  if(k == 1) {
    return(numberToSymbol(number))
  }
  prefixIndex <- number %/% 4
  r <- number %% 4
  prefixPattern <- numberToPattern(prefixIndex, k-1)
  symbol <- numberToSymbol(r)
  return(paste(c(prefixPattern,symbol),collapse=""))
}

computingFrequencies <- function(text,k) {
  frequencyArray <- rep(0,4^k)
  for(i in 1:(nchar(text)-k+1)) {
    pattern <- substr(text,i,i+k-1)
    j <- patternToNumber(pattern)
    frequencyArray[j+1] <- frequencyArray[j+1] + 1
  }
  return(frequencyArray)
}

fasterFrequentWords <- function(text,k) {
  text <- toupper(text)
  frequentPatterns <- c()
  frequencyArray <- computingFrequencies(text,k)
  maxCount <- max(frequencyArray)
  for(i in 1:4^k) {
    if(frequencyArray[i] == maxCount) {
      pattern <- numberToPattern(i-1,k)
      frequentPatterns <- append(frequentPatterns, pattern)
    }
  }
  return(frequentPatterns)
}