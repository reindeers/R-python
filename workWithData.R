# Subseting and sorting data

set.seed(123456789)
X <- data.frame("var1"=sample(1:9), "var2"=sample(9:17))
X <- X[sample(1:3),]; X$var2[c(1,3)] = NA
X
X[,1]
X[,"var1"]
X[1:2, "var2"]

## Logical 
X[(X$var1 > 3  ),]

## sorting
sort(X$var2)

## ordering
X[order(X$var1),]

## adding rows and columns
X$var3 <- rnorm(3)
X

Y <- cbind(X, rnorm(3))
Y

#summarizing
url <- "https://data.baltimorecity.gov/api/views/n4ma-fj3m/rows.csv?accessType=DOWNLOAD"
download.file(url, destfile="./data/parking.csv")
doc <- read.csv("./data/parking.csv")
doc_s <- doc[1:50,]
doc_s <- doc_s[c(-13)]

head(doc_s, n=3)
tail(doc_s, n=3)

summary(doc_s)

str(doc_s)


