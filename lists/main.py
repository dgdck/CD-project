# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def main():
    alphabetical_order(movies)
    won_golden_globe(movie)
    remove_toto_albums(albums)

# 1


movies = ['The Poseidon Adventure', 'Cinderella Liberty', 'Jaws']


def alphabetical_order(movies):
    movies.sort()
    return movies

#2
awards = ['jaws', 'Star Wars: Episode IV - A New Hope', 'Memoirs of a Geisha', 'E.T. the Extra-Terrestrial']
movie = 'JAWS'
lo_awards = [x.lower() for x in awards] #lowercase list
def won_golden_globe(movie):
    if str.lower(movie) in lo_awards:
        return True
    return False

#3
albums = ['Fahrenheit', 'The seventh one', 'Toto xx', 'Falling in between', 'I am alive', '3', 'Vertigo']
toto_albums = ['Fahrenheit', 'The seventh one', 'Toto xx', 'Falling in between', 'Toto XIV', 'Old Is New']
def remove_toto_albums(albums):
    i = 0
    while i < len(albums):
        if albums[i] in toto_albums:
            del albums[i]
            continue
        i +=1
    return albums

if __name__ == '__main__':
    main()