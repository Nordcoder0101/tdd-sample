def coins(change):
    coinObject = {
      'quarters': 0,
      'dimes': 0,
      'nickels': 0,
      'pennies': 0
    }

    if change == 0:
      return coinObject
    else: 
      while change >= 25:
          change -= 25
          coinObject['quarters'] += 1
      while change >= 10:
          change -= 10
          coinObject['dimes'] += 1
      while change >= 5:
          change -= 5
          coinObject['nickels'] += 1
      coinObject['pennies'] = change
      print(coinObject)
      return coinObject    

