# list

stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

#info about a stock

s = "100 shares of AAPL at $150.00 each"

aapl = [100, 'AAPL', 150.00, "20251020"]

#how to get the price of aapl

aapl[2]

aapl_shares = 100
aapl_name = 'AAPL'
aapl_price = 150.00

#create dict to store same data
aapl_stock = {
    #key (collumn): value relationship
    'shares': 100,
    'name': 'AAPL',
    'price': 150.00,
}
# also called map, hashmap
aapl_stock["price"]

# how to read data from CSV file into dict

aapl_stock['name']

#add new key-value pair 

aapl_stock["date"] = "20251020"  
aapl_stock['date']

#modify existing key-value pair
aapl_stock['price'] = 262.24
aapl_stock['price']

for element in aapl:
    print(element)

for k in aapl_stock:
    print(k)

for k,v in appl_stock.items():
    print(k,v)

name = "arjun mascirelli"

# count the frequency of each letter in the name
# how to store the frequency data? what data structyure to use? 
a = 1
r = 1
j = 1
...
a+=1

#abcedfghijklmnopqrstuvwxyz
[3,0,1,]
"""you would have to memorize the index of each letter in the alphabet to know which index to increment"""

freq = {'a':3, 'b':0, 'c':1, ...}
freq['a']

name = "arjun mascirelli"
freq = {}
for c in name:
    if c not in freq: #first time seeing this character
        freq[c] = 1
    else:
        freq[c] += 1

name = 'python programing'
set(name)
tuple(name)
def f(a,b):
    return a + b, a*b
result = f(2,3)
print(result)
print(type(result))


