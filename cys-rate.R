library(reshape2)
library(ggplot2)

setwd("Extras")

cis.rate <- read.table(file = "cys-rate-kirc.tsv",
                  sep = '\t', header = TRUE)

mdata <- melt(cis.rate, id="Chromosome")
mdata$Chromosome <- factor(mdata$Chromosome, levels=c(1:22,"X","Y"))

colores <- c("#7FC97F","#FDC086","#BEAED4","#d4d420","#386CB0")
ggplot(data=mdata, aes(x=Chromosome, y=value, fill=variable)) +
  geom_bar(stat="identity", position=position_dodge()) +
  scale_fill_manual(values=colores) +
  # scale_fill_brewer(palette = "Accent") +
  labs(y = "cis-rate", fill = "") +
  theme_light() +
  theme(axis.line = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text.x = element_text(size=12),
        axis.title.x = element_text(size = 16),
        axis.text.y = element_text(size=12),
        axis.title.y = element_text(size = 16)) +
  scale_y_continuous(limits = c(0,4.5), expand = c(0, 0))
    
