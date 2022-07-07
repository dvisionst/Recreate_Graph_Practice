# Recreate_Graph_Practice

Task
The dataset given to you here is the mortgage dataset used previously in this course. Your goal is to reproduce the graph. The black plot is the 30 year mortgage at 5% and the blue line is the 30 year mortgage at 3%. What is graphed is the cumulative interest paid over the course of the loan. Note that this isn't a beautiful graph. It doesn't say which line is for which mortgage and the graph itself isn't the most visually appealing graph, but it is a great start towards visualizing your data!

Use Python to recreate this graph:


Don't forget to mount your drive, import libraries, upload your data, and smile!!

1. Create a filter so the Mortgage Name is '30 Year'.  Use the len() to find how many rows correspond to 30 years.

2. Create a filter for an interest rate of 3% (notice how it is written in the data!).  

3. Define a new dataframe based on both the year and the interest filters you have created.  

4. We have a choice for the 5% interest rate:

We can just create another filter where df.['Interest Rate'] == .05 

OR 

We can use the negate symbol (~) with our current filter to give us everything EXCEPT what we have defined in the filter. This works here because we only have two interest rates (any value that is NOT 3% is 5%)

5. Since we want to graph the cumulative sum of the interest paid, you can use the function .cumsum().  What are the first three values in the output for the cumulative sum of the 3% rate?

6. Use plt.plot(x, y, c=color) to plot the black line (5%).  We want the x values to be the ['Month'] and the y values to be the cumulative sum of the Interest Paid.  You can use the code from the previous question to define your y values within the plt.plot() function!  Hint: for black, c = 'k'

7. To get both lines on the same graph, just put two plt.plot() functions one after the other in same code block and run it!

Submit your code and reproduced graph! Hint: for blue, c = 'b'
