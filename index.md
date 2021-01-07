# Improving the Efficiencies of a Local Business

<img src="/breakfastfiesta/deliverymap.png" alt="delivery" width="1000"/>

My girlfriend is the owner of an IG business called [BreakfastFiesta](https://www.instagram.com/breakfastfiesta/) that makes and delivers ___.

I help her out______.


## Data preprocessing and processing

When a customer makes an order, we get a bunch of data from them. But not all of it is necessary.

To get the data we care about for making deliveries, we can run the following code in Python.

```python
{
import pandas as pd

# read file
df = pd.read_csv('BreakfastFiestaOrderLog.csv', usecols = ['Cliente', 'Orden', 'Delivery Address'], index_col='Cliente')

# remove all orders that will be picked up
df = df[~df['Delivery Address'].isin(['Pickup'])]

# drop blank cells
df = df.dropna()
}
```

That gives us who we're delivering to, what they purchased, and where to go. 

We get something along the lines of


| Instagram Handle  | Address  | Order |
| :------------ |:---------------:| -----:|
| exampleperson      | 123 Apple St, Miami, FL 33015 | Combo #5 |
| alsoaperson     | 8352 Pine Cone Ln, Hialeah FL 33018 | Combo #2 |
| imahuman | 1112 Peanut Blvd, Weston, FL 33326 | Combo #7 |




# A collapsible section with markdown
<details>
  <summary>Click to expand!</summary>
  
  ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets
</details>


<button name="button">Click me</button>