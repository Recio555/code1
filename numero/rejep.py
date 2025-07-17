import rpy2.robjects as ro
ro.r('data(input)')
ro.r('x <-HoltWinters(input)')