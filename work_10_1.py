enter_the_cities_past_10_years = set(
    input('Enter cities where you have visited in the past 10 years:  ').title().split())
enter_the_cities_will_10_years = set(
    input('Enter cities where you wants to go in the next 10 years:  ').title().split())
like_city = enter_the_cities_past_10_years.intersection(enter_the_cities_will_10_years)
if like_city:
    print('probably liked it a lot in the cities', str(like_city).replace('{', '').replace('}', ''))
else:
    print('the user is open to something new')
