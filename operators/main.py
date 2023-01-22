# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#1
Switzerland_language = "German"
Spain_language = "Castilian Spanish"
print(Switzerland_language == Spain_language)
#2
Switzerland_religion = "Roman Catholic"
Spain_religion = "Roman Catholic"
print(Switzerland_religion == Spain_religion)
#3
Switzerland_capital = "Bern"
Spain_capital = "Madrid"
print(len(Spain_capital) != len(Switzerland_capital))
#4
Switzerland_GDP = 590710000000
Spain_GDP = 1714860000000
print(Switzerland_GDP > Spain_GDP)
#5
Switzerland_pop_growth = 0.65
Spain_pop_growth = 0.13
print(Switzerland_pop_growth < 1 and Spain_pop_growth < 1)
#6
Switzerland_population = 8.5
Spain_population = 47.1
print(Switzerland_population > 10 or Spain_population > 10)
#7
print(Switzerland_population > 10 and Spain_population <= 10 or Spain_population > 10 and Switzerland_population <= 10)