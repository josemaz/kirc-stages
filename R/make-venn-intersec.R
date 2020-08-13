library(VennDiagram)


set1 <- read.table("Results/cuts-mi/1K/kirc-ctrl-1K.txt",
	col.names=c("src", "dst", "mi"))
set1 <- set1[1:2]
set1 <- transform(set1, newcol=paste(src, dst, sep="_"))
set1 <- as.vector(set1$newcol)

set2 <- read.table("Results/cuts-mi/1K/kirc-stagei-1K.txt",
	col.names=c("src", "dst", "mi"))
set2 <- set2[1:2]
set2 <- transform(set2, newcol=paste(src, dst, sep="_"))
set2 <- as.vector(set2$newcol)

colors <- c("#6b7fff", "#c3db0f")

venn.diagram(x = list(set1, set2) ,
            category.names = c("s1", "s2"),
            filename = 'Plots/datadaft_venn.png',
            output=TRUE,
            imagetype="png", 
            scaled = FALSE,
            col = "black",
            fill = colors,
            cat.col = colors,
            cat.cex = 2,
            cat.dist = 0.07,
            margin = 0.15
)

















# colors ＜- c("#6b7fff", "#c3db0f", "#ff4059", "#2cff21", "#de4dff")