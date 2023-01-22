# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
countries = get_countries()
# 1


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {}
    passport['name'] = name
    passport['date_of_birth'] = date_of_birth
    passport['place_of_birth'] = place_of_birth
    passport['height'] = height
    for country in countries:
        if country == nationality:
            passport['nationality'] = nationality
    return passport


def add_stamp(passport, country):
    passport = create_passport(
        'Jan', '2002-12-31', 'Alphen', '1.78', 'Algeria'
        )
    if country != passport.get(country):
        passport['stamps'] = country
    return passport


passport = {
    'name': 'Jan',
    'date_of_birth': '2002-12-31',
    'place_of_birth': 'Alphen',
    'height': '1.78',
    'nationality': 'Algeria'
}


def add_biometric_data(passport, bio, data, date):
    if 'biometric' not in passport:
        x = {
            'biometric': {
                bio: {
                    'value': data,
                    'date': date
                }
            }
        }
        passport.update(x)
    else:
        passport['biometric'][bio] = {
                'date': date,
                'value': data
                }
    return passport


if __name__ == "__main__":
    create_passport('Jan', '2002-12-31', 'Alphen', '1.78', 'Algeria')
    add_stamp('Jan', 'Bahamas')
    add_biometric_data(passport, "eye_color_left", "blue", "2020-05-05")
    add_biometric_data(passport, "eye_color_right", "green", "2020-05-05")
