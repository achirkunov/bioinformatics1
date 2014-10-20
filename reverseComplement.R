reverseString <- function(input) {
  output <- ""
  len <- nchar(input)
  for(i in 1:len) {
    output[i] = substr(input,len-i+1,len-i+1)
  }
  return(paste(output,collapse=""))
}

complement <- function(symbol) {
  switch(symbol, "A" = "T", "C" = "G", "G" = "C", "T"= "A")
}

reverseComplement <- function(input) {
  input <- reverseString(input)
  output <- ""
  for(i in 1:nchar(input)) {
    output[i] <- complement(substr(input,i,i))
  }
  return(paste(output,collapse=""))
}