# http://habrahabr.ru/post/217963/

colnames = c("RowNumber", "License", "RegPlate", "LegalName", "INN", "OGRN", "DocNum", "Car", "Year", "Status", "Void")
rawdata <- read.csv2(file="taxi.csv", header = TRUE, sep = ";",
                     colClasses = c("numeric", rep("character",8), "character", NA),
                     col.names = colnames,
                     strip.white = TRUE,
                     blank.lines.skip = TRUE,
                     stringsAsFactors = FALSE,
                     encoding = "UTF-8")

ptn <- "^(.+?) (.+)$" # regexp pattern to match first word
dt <- data.table(rawdata)[, 
                          list(RegPlate, LegalName, Car, OGRN,
                               OrgType  = gsub(ptn, "\\1" , toupper( LegalName )),
                               CarBrand = gsub(ptn, "\\1",  toupper( Car       )))                          
                          ]
#dt$OrgType[nchar(dt$OrgType) > 4] <- "ИП"
dt[!(dt$OrgType == "АО" & dt$OrgType == "ЗАО" & dt$OrgType == "ОАО" & dt$OrgType == "ООО"),] <- "ИП"
rm(rawdata)

sort(table(dt$OrgType))
str(dt$CarBrand)



# grepl(dt$OrgType, c("АО", "ЗАО",  "ОАО", "ООО"))
# ( dt$OrgType = "АО" || dt$OrgType = "ЗАО" || dt$OrgType = "ОАО" || dt$OrgType = "ИП" || dt$OrgType = "ООО" )

dt[dt$OrgType=="ООО"] <- "ИП"
dt[dt$OrgType=="ООО"]
