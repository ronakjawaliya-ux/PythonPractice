# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_dollars = lambda data: (data[0],data[1]*96.22)    # (1 USD = 96.22 INR)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)




store2 = [("shirt",2400.00),
         ("pants",2700.00),
         ("jacket",4500.00),
         ("socks",300.00)]

to_dollars = lambda data: (data[0],data[1]*96.22)  #INR --> USD  (1 USD = 96.22 INR)
to_euros = lambda data: (data[0],data[1]*110.38)     #INR --> EUR  (1 EUR = 110.38 INR)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)