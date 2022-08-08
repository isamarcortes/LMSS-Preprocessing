library(dplyr)

root_dir <- glue::glue(
  "C:/Users/Priscilla Baltezar/OneDrive/Documents/bda/", 
  "Bulk Order South East Asia - Myanmar, Thailand, Cambodia/", 
  "Landsat 1-5 MSS C2 L1/output/"#where my already untarred files live
)

# use this when you need to untar the files in the directory first
# dir_tar <- list.files(path = root_dir, pattern = "*.tar", exdir = "~./output") %>% lapply(., untar)
# #list only tif files
# my_dir <- dir(path = "~./output", pattern = "*.TIF")

my_dir <- dir(root_dir, pattern = "*.TIF$") 

# create tibble for grouping and indexing files from different dates
indexer <- as_tibble(my_dir) %>% 
  mutate(img = value) %>% 
  tidyr::separate(value, paste0("v", 1:10)) %>% 
  mutate(index = glue::glue("{v3}_{v4}")) %>% 
  select(img, index)

# check to see that index makes consistent groups of 6 bands
indexer %>% group_by(index) %>% 
  count() %>% pull(n) %>% range(.)

stack_list <- lapply(unique(indexer$index), function(x) {
  pths <- indexer %>% 
    filter(index == x) %>% 
    pull(img)
  #print(file.path(root_dir, pths))

  #terra function 1 #######################################################
  #stack the raster bands to their corresponding images
  r <- terra::rast(file.path(root_dir, pths))
  
  #terra function 2#######################################################
  #write raster to disk first attempt
  terra::writeRaster(r, names(r), filetype = "GTiff")#write the image to disk
  
  #write raster to disk 2nd attempt
  #terra::writeRaster(r, filename = stringr::str_sub(r@ptr[["names"]], 1,7), filetype = "GTiff")

}) 

#incorporate lines 47 - 60 in above fxn
NewNameList <- list() 

for (i in stack_list[[]]@ptr[["names"]]){
  V1 <- strsplit(i,'_')[[1]][1]
  V2 <- strsplit(i,'_')[[1]][2]
  V3 <- strsplit(i,'_')[[1]][3]
  V4 <- strsplit(i,'_')[[1]][4]
  V5 <- strsplit(i,'_')[[1]][5]
  V6 <- strsplit(i,'_')[[1]][6]
  V7 <- strsplit(i,'_')[[1]][7]
  NewName <- paste(V1,V2,V3,V4,V5,V6,V7,sep='_')
  NewNameList <- append(NewNameList,list(NewName))
}
NewNameList <-unique(NewNameList)
