# This script plots the little decorative probability distributions used in Fig 1 (although they were edited further in Inkscape)

pdf(file = "cauchy.pdf")
plot(seq(0, 4, length.out=100), dcauchy(seq(0, 4, length.out=100), 0, 1), type = "l", lwd=10, col="#70CFF1", axes=F, xlab="", ylab="", ylim=c(-.01, .36), main = "Half-Cauchy", cex.main=6, family="sans", font.main=1)
axis(1, labels = FALSE, tck=0, lwd=8)
dev.off()

pdf(file = "categorical.pdf")
barplot(c(3,1,4,2), col="#70CFF1", border = F, axes=F, main = "Categorical", cex.main=6, family="sans", font.main=1, space=4)
axis(1, labels = FALSE, tck=0, lwd=8)
dev.off()

pdf(file = "multinomial.pdf")
barplot(c(3,1,4,2,2.5,1.5, 6, 1), col="#70CFF1", border = F, axes=F, main = "Multinomial", cex.main=6, family="sans", font.main=1, space=1)
axis(1, labels = FALSE, tck=0, lwd=8)
dev.off()

pdf(file = "poisson.pdf", height=5, width=6)
hist(rpois(10000, 8), border = F, col = "#70CFF1", main = "Poisson", xlab="", ylab="", cex.main=6, family="sans", font.main=1, axes=F)
axis(1, labels = FALSE, tck=0, lwd=8)
dev.off()
