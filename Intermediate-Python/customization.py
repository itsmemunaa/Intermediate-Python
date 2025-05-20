# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('gdp_cap')
plt.ylabel('life_exp')


# Add title
plt.title("World Development in 2007")

# After customizing, display the plot
plt.show()