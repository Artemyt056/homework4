from decimal import Decimal
from pywebio.input import input as pw_input, slider, FLOAT
from pywebio.output import put_success, put_warning, put_code, popup, put_error, toast

PRICE_ONE_KILO_CALORIE = 0.32541

# on 100 gram
ENERGY_OSTRICH_EGG = 118
ENERGY_RABBIT = 197
ENERGY_BANANA = 87
ENERGY_SEA_BASS = 123
ENERGY_SWEET_RED_PEPPER = 26
ENERGY_PARSLEY_GREEN = 45
ENERGY_WAFFLES = 425
ENERGY_WHEAT_BREAD_OF_FIRST_GRADE_FLOUR = 246
ENERGY_PISTACHOS = 555
ENERGY_KEFIR_2_AND_5_TEN_PERCENT = 51

total_energy = 0

portion_ostrich_egg = pw_input(f'Enter the desired portion of ostrich eggs, grams. '
                               f'Caloric content {ENERGY_OSTRICH_EGG} kcal/100g', type=FLOAT)
portion_ostrich_egg_energy = (float(portion_ostrich_egg) * ENERGY_OSTRICH_EGG) / 100
total_energy = total_energy + portion_ostrich_egg_energy
put_success(f'You ordered {portion_ostrich_egg} grams of ostrich eggs,\n'
            f'Calorie content of a portion {portion_ostrich_egg_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_rabbit = slider(f'Enter the desired portion of rabbit, grams. '
                        f'Caloric content {ENERGY_RABBIT} kcal/100g', min_value=1, max_value=2500)
portion_rabbit_energy = (float(portion_rabbit) * ENERGY_RABBIT) / 100
total_energy = total_energy + portion_rabbit
put_success(f'You ordered {portion_rabbit} grams of rabbit,\n'
            f'Calorie content of a portion {portion_rabbit_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_banana = pw_input(f'Enter the desired portion of banana, grams. '
                               f'Caloric content {ENERGY_BANANA} kcal/100g', type=FLOAT)
portion_banana_energy = (float(portion_banana) * ENERGY_BANANA) / 100
total_energy = total_energy + portion_banana
put_success(f'You ordered {portion_banana} grams of banana,\n'
            f'Calorie content of a portion {portion_banana_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_sea_bass = pw_input(f'Enter the desired portion of sea bass, grams. '
                          f'Caloric content {ENERGY_SEA_BASS} kcal/100g', type=FLOAT)
portion_sea_bass_energy = (float(portion_sea_bass) * ENERGY_SEA_BASS) / 100
total_energy = total_energy + portion_sea_bass
put_success(f'You ordered {portion_sea_bass} grams of sea bass,\n'
            f'Calorie content of a portion {portion_sea_bass_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_sweet_red_pepper = pw_input(f'Enter the desired portion of sweet red pepper, grams. '
                               f'Caloric content {ENERGY_SWEET_RED_PEPPER} kcal/100g', type=FLOAT)
portion_sweet_red_pepper_energy = (float(portion_sweet_red_pepper) * ENERGY_SWEET_RED_PEPPER) / 100
total_energy = total_energy + portion_sweet_red_pepper
put_success(f'You ordered {portion_sweet_red_pepper} grams of sweet red pepper,\n'
            f'Calorie content of a portion {portion_sweet_red_pepper_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_parsley_green = pw_input(f'Enter the desired portion of parsley green, grams. '
                               f'Caloric content {ENERGY_PARSLEY_GREEN} kcal/100g', type=FLOAT)
portion_parsley_green_energy = (float(portion_parsley_green) * ENERGY_PARSLEY_GREEN ) / 100
total_energy = total_energy + portion_parsley_green
put_success(f'You ordered {portion_parsley_green} grams of parsley green,\n'
            f'Calorie content of a portion {portion_parsley_green_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_waffles = pw_input(f'Enter the desired portion of waffles, grams. '
                               f'Caloric content {ENERGY_WAFFLES} kcal/100g', type=FLOAT)
portion_waffles_energy = (float(portion_waffles) * ENERGY_WAFFLES) / 100
total_energy = total_energy + portion_waffles
put_success(f'You ordered {portion_waffles} grams of waffles,\n'
            f'Calorie content of a portion {portion_waffles_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_wheat_bread_of_first_grade_flour = pw_input(f'Enter the desired portion of wheat breadof first grade flour, grams. '
                               f'Caloric content {ENERGY_WHEAT_BREAD_OF_FIRST_GRADE_FLOUR} kcal/100g', type=FLOAT)
portion_wheat_bread_of_first_grade_flour_energy = (float(portion_wheat_bread_of_first_grade_flour) * ENERGY_WHEAT_BREAD_OF_FIRST_GRADE_FLOUR) / 100
total_energy = total_energy + portion_wheat_bread_of_first_grade_flour
put_success(f'You ordered {portion_wheat_bread_of_first_grade_flour} grams of wheat bread of first_grade flour,\n'
            f'Calorie content of a portion {portion_wheat_bread_of_first_grade_flour_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_pistachos = pw_input(f'Enter the desired portion of pistachos, grams. '
                               f'Caloric content {ENERGY_PISTACHOS} kcal/100g', type=FLOAT)
portion_pistachos_energy = (float(portion_banana) * ENERGY_PISTACHOS) / 100
total_energy = total_energy + portion_pistachos
put_success(f'You ordered {portion_pistachos} grams of pistachos,\n'
            f'Calorie content of a portion {portion_pistachos_energy}\n'
            f'total calorie content of the order: {total_energy}')


portion_kefir_2_and_5_ten_percent = pw_input(f'Enter the desired portion of kefir_2_and_5_ten_percent, grams. '
                               f'Caloric content {ENERGY_KEFIR_2_AND_5_TEN_PERCENT} kcal/100g', type=FLOAT)
portion_kefir_2_and_5_ten_percent_energy = (float(portion_kefir_2_and_5_ten_percent) * ENERGY_KEFIR_2_AND_5_TEN_PERCENT) / 100
total_energy = total_energy + portion_kefir_2_and_5_ten_percent
put_success(f'You ordered {portion_kefir_2_and_5_ten_percent} grams of kefir_2_and_5_ten_percent,\n'
            f'Calorie content of a portion {portion_kefir_2_and_5_ten_percent_energy}\n'
            f'total calorie content of the order: {total_energy}')

if total_energy < 1000:
    toast('I must be hungry')
elif 1000 <= total_energy <= 1500:
 toast("This is exactly my version of dinner")

else:
    toast("I won't eat that much, but it's money in the trash")

coast_of_diner = total_energy * PRICE_ONE_KILO_CALORIE
rounding_coast_of_diner = Decimal(coast_of_diner).quantize(Decimal('0.01'))
put_success(f'This is your account {rounding_coast_of_diner}')
