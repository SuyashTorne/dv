library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point()


library(ggplot2)
ggplot(economics, aes(x = date, y = unemploy)) +
  geom_line()


library(ggplot2)
ggplot(diamonds, aes(x = cut)) +
  geom_bar()


library(ggplot2)
ggplot(mpg, aes(x = hwy)) +
  geom_histogram()


library(ggplot2)
ggplot(mpg, aes(x = class, y = hwy)) +
  geom_boxplot()


library(ggplot2)
ggplot(faithfuld, aes(waiting, eruptions, z = density)) +
  geom_raster()


library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE)
