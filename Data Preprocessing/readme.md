# Steps

- modified column names
- checking & removing extremely sparse features
- expand room and price column (3000 -> 3729 data points)
- standardize room type column (added 1 to 6 bedrooms)
- grab other features out such as whether has den

# Initial Findings

- Price range:
   - '345.0 ~ 1084.65': 48,
   - '1084.65 ~ 1824.3': 642,
   - '1824.3 ~ 2563.95': 1912,
   - '2563.95 ~ 3303.6': 764,
   - '3303.6 ~ 4043.25': 228,
   - '4043.25 ~ 4782.9': 50,
   - '4782.9 ~ 5522.55': 32,
   - '5522.55 ~ 6262.2': 19,
   - '6262.2 ~ 7001.85': 17,
   - '7001.85 ~ 7741.5': 3
   
   
| <img src="https://github.com/JJtheNOOB/Rental_price/blob/master/Data%20Preprocessing/location.png" width="400" height="250"> | <img src="https://github.com/JJtheNOOB/Rental_price/blob/master/Data%20Preprocessing/bedroom.png" width="400" height="250"> |
|:--:| :--:|
| *location* | *bedroom* |
