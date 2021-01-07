# Improving the Efficiencies of a Local Business

<img src="/breakfastfiesta/deliverymap.png" alt="delivery" width="1000"/>

My girlfriend is the owner of an IG business called [BreakfastFiesta](https://www.instagram.com/breakfastfiesta/) that makes and delivers ___.

I help her out______.


## Data processing

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

We collected a bunch of data from customers, but with the above code we could boil it down to what we care about: who we're delivering to, what they purchased, and where to go. And we get something along the lines of

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