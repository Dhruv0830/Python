#moment 1 - Mean(linear)
#moment 2 - Standard Deviation(Square) 
#moment 3 - Skewness(Cube in formula) (n/(n-1)*(n-2))(x-mean/s)^3
#moment 4 - Kurtosis(Degree four)(Curved arching-tailedness)

#Kurtosis-> More outliers or fat tailed(tail events) is more kurtosis

#Use :
#Finance : kurtosis risk refers to possibility of extreme outcomes occurring.

#Kurtosis(k) 
#k -3 if > 0 then leptokurtic(fatter tail), k-3 < 0 then platykurtic(less extreme values) , k-3 = 0 then mesokurtic(Normal disttribution)

#QQ(Quantile-Quantile) Plot, Visual inspection, Statistical tests- to find if given dist. is normal or not.

#QQ Plots:
#Assess the similarity of the distribution of two sets of data.One can be theoretical distribution and other can be our data.
#1.Pick a distribution(ND)
#2.Sort and find Quantiles(100)
#Plot the 100 points of both the curves and if the resulting plot follows a line then they are same.

#PLot a scatter plot using this.
# import statsmodel.api as sm
# fig = sm.qqplot(df['sepal_length'],line='45',fit=true)

#Skewness for uniform distribution is 0 as it is symmetric.

#Log normal distribution : Right skewed and log of the distribution is normally distributed.
# Ex- length of comments on reddit are log normally distributed or users dwell time on articles, length of chess games, income of 97-99% of population.

#Log normal is skewed.

#How to check ? We take a log and calculate the QQ plot.

#Pareto Distribution.
# Power law : y :: k*x^a
#80:20 Rule : 20 will produce 80 percent of result.Ex - Wealth of people
#Ex: File size distribution on internet. Few large files , alot of small files.

#This is skewed .

#How to find if Pareto?
#Log-Log plot : log (x) and log(y) same distribution is line with negative slope.
#Also we can find the QQ Plot.

#Transformations:
#Linear and Logistic regression works better with normal data.
#left-skewed - square transform or perform square on every data point.
#Right skewed - log normal
#Decision tree does not care about data but logistic can improve if normal distributed data.




#Hypothesis Testing

#A statistical test is a method of statistical inference used to decide whether the data at hand sufficiently supports a particular hypothesis. It helps us to make probabilistic statements about population parameters

#Null Hypothesis(status quo): Assumes that there is no significant effect or relationship between the variables being studied.

#Alternate Hypothesis(research hypothesis): It contradicts the null hypothesis. 

#Either null or alternate.

#Failing to reject the null hypothesis does not mean that the null hypothesis is true.

# Steps:
#Rejection region approach:

#1.Formulate the null and alternate hypothesis.
#2.Select a significance level (probability of rejecting the null when it is true. Generally 0.05-0.01)
#3.Check assumptions : data distribution, std available
#4.Check which test is appropriate: z-test:normal dist with given std , t-test: std not given , chi-square test : categorical, ANOVA
#5.Calculate the relevant test statistic.
#6.Conduct test.
#7.Reject or not reject null.
#8.Interpret the result.


#pop mean = 50 , pop std = 5
#After training program Pop mean = 53.

#Null: no change after training or mean =50
#Alterante : mean > 50
#Alpha is 0.05
#Assumptions : Thorugh CLT normal dist. and pop std known.
#Therefore z-test or find z.
# z = (mean' - pop mean)/(std/sqrt(n)) = 3.28
# z(aplha) = 1.65 
# 3.28 > 1.65 .Therefore in rejection.
# Strong evidence against null in favor of alternate.Therefore we reject the null.

#2 tailed test when searching for mean != 50 and we use z(alpha/2)

#When direction is known then one sided , if not equal to then two sided.

#Significance level : denoted as alpha  , is a predetermined threshold used in hypothesis testing to determine whether the null hypothesis should be rejected or not. It represents the probability of rejecting the null hypothesis when it is actually true , also known as type 1 error.

#If alpha increases then the acceptable region shrinks and vice versa

#The rejection(critical) region of values corresponds to the rejection of the null hypothesis at some chosen probability level.

#Problem with this.
#we cannot differentiate between z=15 and z=2 (both in rejection region)

#Therefore we calculate the p-values.

#Type 1 (false positive) and Type 2 (false negative) error

#One sided(single tailed ) test 
# When the researcher is interested in testing the effect in a specific direction.The alternate hypothesis contains either < or >.

#Double sided(two tailed) test
# When researcher is interested in testing the effect in both directions.The alternate hypothesis contains != sign 

#P-values
#It is the probability of getting a sample as or more extreme(having more evidence against Ho) than our own sample given in the null