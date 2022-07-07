import pandas as pd
import matplotlib.pyplot as plt

mortgage_df = pd.read_csv('mortgages.csv')
year_30 = mortgage_df['Mortgage Name'] == '30 Year'

# print(len(mortgage_df[year_30])) This outputs 720 mortgages that are 30 years

three_pct_fill = mortgage_df['Interest Rate'] == 0.03

# print(len(mortgage_df[three_pct_fill])) This outputs 540 mortgages that have a 3% interest rate.

thirty_at_three_df = mortgage_df[year_30 & three_pct_fill]
# print(len(thirty_at_three_df))
# print(thirty_at_three_df.head())
thirty_at_five_df = mortgage_df[year_30 & ~three_pct_fill]
# print(len(thirty_at_five_df))
# print(thirty_at_five_df.head())
#
# print(thirty_at_three_df['Interest Paid'].cumsum()) 0        1000.00, 1998.28, 2994.84

three_cume = thirty_at_three_df['Interest Paid'].cumsum()
five_cume = thirty_at_five_df['Interest Paid'].cumsum()

plt.plot(x=thirty_at_three_df['Month'], y=three_cume, c='b')
plt.plot(x=thirty_at_five_df['Month'], y=five_cume, c='k')

