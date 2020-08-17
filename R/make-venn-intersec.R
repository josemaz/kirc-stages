library(VennDiagram)
library(RColorBrewer)
library(stringr)

args = commandArgs(trailingOnly=TRUE)
# cut <- "1K"
cut <- args[1] # 1st Parameter cut. Ex, "1K"

etapas <- c("ctrl","stagei","stageii","stageiii","stageiv")
# etapas <- c("ctrl","stagei","stageii")


sets <- list()
for (etapa in etapas){
      fname <- paste0("Results/cuts-mi/",cut,"/kirc-",etapa,"-",cut,".txt")
      print(fname)
      set <- read.table(fname,col.names=c("src", "dst", "mi"))
      set <- set[1:2]
      set <- transform(set, newcol=paste(src, dst, sep="_"))
      sets[[etapa]] <- as.vector(set$newcol)
}

colors <- c("#6b7fff", "#c3db0f", "#7FC97F", "#BEAED4", "#FDC086")
colors <- colors[1:length(sets)]
print(colors)

fout <- paste0('Plots/venn-',cut,'.png')
t <- paste0('Interaction sets,  MI cut=',cut)
venn.diagram(x = sets,
            category.names = etapas,
            filename = fout,
            main = t,
            output=TRUE,
            imagetype="png", 
            scaled = FALSE,
            col = "black",
            fill = colors,
            cat.col = colors,
            cat.cex = 1,
            cat.dist = 0.25,
            margin = 0.15,
            cex = 0.7
)

all <- Reduce(intersect, sets[1:5])
df <- data.frame(rel = all)
df <- str_split_fixed(df$rel, "_", 2)
colnames(df)<- c("src","dst")
fout <- paste0("Results/cuts-mi/",cut, "/inter-all-groups-",cut,".tsv")
write.table(df, file = fout, row.names = FALSE, quote=FALSE, sep='\t')

alletapas <- setdiff( Reduce(intersect, sets[2:5]) ,all)
df <- data.frame(rel = alletapas)
df <- str_split_fixed(df$rel, "_", 2)
colnames(df)<- c("src","dst")
fout <- paste0("Results/cuts-mi/",cut, "/inter-only-stages-",cut,".tsv")
write.table(df, file = fout, row.names = FALSE, quote=FALSE, sep='\t')





