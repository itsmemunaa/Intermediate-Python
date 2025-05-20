# Print the last item of gdp_cap and life_exp
import matplotlib.pyplot as plt 
print(gdp_cap[-1])
print(life_exp[-1])


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy vs GDP per Capita')
plt.show()

# Display the plot
plt.show()