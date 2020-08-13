# install.packages("plyr")
# install.packages("BiocManager")
# install.packages("reshape")
# install.packages("ggplot2")
# BiocManager::install("biomaRt")

library(biomaRt)
# library(dplyr)
library(reshape2)
library(ggplot2)
library(grid)
# library(gridExtra)
# library(RColorBrewer)

setwd("Results/Expression")

mart <- useEnsembl("ensembl",dataset="hsapiens_gene_ensembl")
biomartcols <- c("ensembl_gene_id", "percentage_gene_gc_content", "gene_biotype",
                 "start_position","end_position","hgnc_id","hgnc_symbol","chromosome_name")
Annot <- getBM(attributes = biomartcols, mart=mart) # GET ALL GENES

get.expr.by.gene <- function(gname, annot) {
  # gene.specs <- Annot[grep("SLC6A19", Annot$hgnc_symbol), ]
  # gene.specs <- Annot[Annot$hgnc_symbol == "PLG", ]
  gene.specs <- annot[annot$hgnc_symbol == gname, ]
  ensembl <- gene.specs[["ensembl_gene_id"]]
  print(ensembl)
  
  fnames <- c("ctrl", "stagei", "stageii", "stageiii", "stageiv")
  nombres <- c("Control", "Stage I",  "Stage II",  "Stage III",  "Stage IV")
  
  metadata <- data.frame(fnames, nombres)
  
  dd = data.frame(etapa = numeric(0), value= numeric(0))
  for(i in 1:nrow(metadata)) {
    row <- metadata[i,]
    print(row["nombres"])
    expr <- read.table(file = paste0("kidney-",row["fnames"],".tsv")
                       , sep = '\t', header = TRUE)
    gexpr <- t(expr[expr$gene == ensembl,-1])
    colnames(gexpr)[1] <- row["nombres"]
    row.names(gexpr) <- NULL
    gexpr <- melt(gexpr)
    gexpr <- gexpr[,-c(1)]
    colnames(gexpr) <- c("etapa","value")
    gexpr$X1 <- NULL
    dd <- rbind(dd,gexpr)
  }
  
  dd$etapa <- as.factor(dd$etapa)
  return(dd)
}

plot.gene <- function(data, gname, xd){
  colores <- c("#7FC97F","#FDC086","#BEAED4","#d4d420","#386CB0")
  grob <- grobTree(textGrob(gname, x=xd,  y=0.95, hjust=0,
                            gp=gpar(fontsize=30)))
  p <- ggplot(data, aes(x=etapa, y=value)) + 
    stat_boxplot(geom ='errorbar', width = 0.3) +
    geom_boxplot(show.legend = F, aes(fill=etapa)) +
    scale_y_log10(breaks=2*c(1,10,100,1000,10000)) +
    scale_fill_manual(values=colores) +
    # scale_fill_brewer(palette = "Accent") +
    annotation_custom(grob) +
    theme_light() +
    theme(axis.title.x = element_blank(),
          axis.title.y = element_blank(), 
          text = element_text(size=25)) 
  return(p)
}


dd1 <- get.expr.by.gene("SLC6A19",Annot)
dd2 <- get.expr.by.gene("PLG",Annot)

p1 <- plot.gene(dd1,"SLC6A19",0.76)
p1
p2 <- plot.gene(dd2,"PLG",0.87)
p2


  