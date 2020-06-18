
# Error seems to come from CANDLE is NOT updating as prices does.

# It should be creating prices constantly.
# Then, when (prices % 10):
#				Create and ADD a new candle.
# Go until 100 candles.


import random
import time

# INITIALIZE PRICES
prices 	= [1]
ohlc 	= []
candles = []

# INITIALIZE RANGE
minimum = 0
maximum = 0

# INITIALIZE TIMER
timer  	= 0

# Range of candle size to make.
candle_size = 0


# Update prices
while True:

	# Wait one second.
	time.sleep(1)
	timer += 1
	print("Timer:   ", timer)

	# Generate NEW price
	r = round((random.randint(-5, 5)/10000) + prices[-1], 4)
	# ADD new price
	prices.append(r)

	# # SHOW 'prices'
	# print(prices)

	# Create a new candle
	if (timer % 5 == 0):
		o = prices[-5]
		h = max(prices)
		l = min(prices)
		c = prices[-1]

		ohlc = [o, h, l, c]
		candles.append(ohlc)


		# SHOW 'candles'
		print("Candles: ", candles)
















# # Continuous price update and candle creation.

# import random


# prices  = [1]
# ohlc    = []
# candles = []
# minimum = 0
# maximum = 9

# 	# # INITIALIZE
# 	# if (prices == []):

# # Initialize FIRST 100 prices
# for x in range(100):
# 	# Generate NEW price
# 	r = round((random.randint(-5, 5)/10000) + prices[x], 4)
# 	# ADD new price
# 	prices.append(r)

		
# print(prices)


# while True:

# 	# Generate NEW price
# 	r = round((random.randint(-5, 5)/10000) + prices[0], 4)
# 	# Q: Add 'prices' to it BEFORE appending?


# 	# ADD new price
# 	prices.append(r)

# 	# If length of prices is divisable by 110, then do candles(ohlc), and then remove oldest 10 prices
# 	if (len(prices) % 110):		
# 		for y in range(10): 		# 10 TOTAL CANDLES

# 			o = prices[minimum]
# 			h = max(prices)
# 			l = min(prices)
# 			c = prices[maximum]

# 			# After values, bump up the range
# 			minimum += 10
# 			maximum += 10

# 			ohlc = [o, h, l, c]
# 			candles.append(ohlc)