# get data from xml (download)

if (!file.exists("data")) {
  dir.create("data")
}

fileUrl <- "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.xml?accessType=DOWNLOAD"
download.file(fileUrl, destfile="./data/cameras.xml")
list.files("./data")

doc <- xmlTreeParse("./data/cameras.xml", useInternal = TRUE)
rootNode <- xmlRoot(doc)
xmlName(rootNode)
names(rootNode)
rootNode[[1]][[1]][["street"]]

# get data from web
## with xml parser
url <- "http://krstc.ru/"
doc <- htmlTreeParse(url, useInternalNodes = TRUE)
xpathSApply(doc, "//p", xmlValue)

## with httr pack

library("httr"); doc2 <- GET(url)
content <- content(doc2, as="text")
parsedHtml <-htmlParse(content, asText = TRUE)

# with passwords

# using handles

# mining with API's
## twitter API

myapp <- oauth_app("twitter", 
                   key="", 
                   secret = "")
sign <- sign_oauth1.0(myapp, 
                      token = "", 
                      token_secret = "")
home <- GET("https://api.twitter.com/1.1/statuses/home_timeline.json", sign)

json1 <- content(home)
json2 <- jsonlite::fromJSON(toJSON(json1))


