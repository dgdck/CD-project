# Do not modify trm_acthese lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
weather = 'rainy'
time_of_day = 'night'
cow_milking = False
cow_location = 'cowshed'
season = 'winter'
slurry_tank_status = False
grass_status = True

def main():
    farm_action(weather, time_of_day,cow_milking,cow_location,season,slurry_tank_status,grass_status)

def farm_action(weather, time_of_day,cow_milking,cow_location,season,slurry_tank_status,grass_status):
    if cow_location == 'pasture':
        if weather == 'rainy' or time_of_day == 'night':
            if cow_milking == True:
                if slurry_tank_status == True:
                    if weather == 'rainy' or 'neutral':
                        return 'take cows to cowshed\nmilk cows\nfertilize pasture'
                else:
                    return 'take cows to cowshed\nmilk cows'
            else:
                return 'take cows to cowshed'
            if slurry_tank_status == True:
                    if weather == 'rainy' or 'neutral':
                        return 'take cows to cowshed\nfertilize pasture'
        elif weather == 'neutral':
            if slurry_tank_status == True:
                if cow_milking == True:
                    return 'take cows to cowshed\nmilk cows\nfertilize pasture\ntake cows back to pasture'
                if cow_milking == False:
                    if weather == 'neutral':
                        return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
            elif slurry_tank_status == False:
                if cow_milking == True:
                    return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        elif weather == 'sunny' and season == 'spring':
                if cow_milking == True:
                    return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
                elif cow_milking == False:
                    return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
        elif weather == 'sunny':
            if cow_milking == True:
                return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        else:
            return 'take cows to cowshed'
    elif cow_location == 'cowshed':
        if cow_milking == True:
            return 'milk cows'
        elif slurry_tank_status == True:
            if weather == 'neutral' or 'rainy':
                return 'fertilize pasture'
        elif grass_status == True:
            if weather == 'sunny' and season == 'spring':
                return 'mow grass'
            else:
                return 'wait'
    else:                                                    
        return 'wait'

if __name__ == '__main__':
    main()