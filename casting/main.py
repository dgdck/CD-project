# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
#1
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')
#2
order_leek = 'leek 4'
sum_total = int(order_leek[order_leek.find(' ') + 1:]) * leek_price
print(sum_total)
#3
broccoli_price = 2.34
order_broccoli = 'broccoli 1.6'
sum_total_broccoli = float(order_broccoli[order_broccoli.find(' ') + 1:]) * broccoli_price
print(str(order_broccoli[order_broccoli.find(' ') + 1:]) + 'kg broccoli costs ' + str(round(sum_total_broccoli, 2)) + 'e')