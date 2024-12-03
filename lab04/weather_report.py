from pathlib import Path
import file_reader 
import weather_functions
# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 0)
avg_temp = sum(temp_list)/len(temp_list)

q1 = int(input("Vad vill du göra? Tryck 1 för medeltemperatur och 2 för vårens ankomst "))
if q1 == 1:
    q2 = int(input("Vilken månad vill du beräkna medeltemperaturen för? Ange månadsnummer"))
    weather_functions.calculate_avg_temp(file_reader.read_from_file(file_path, q2))
else:
    print("Letar efter våren...")
    print("Våren infaller på index", weather_functions.when_is_spring(temp_list))


weather_functions.when_is_spring(temp_list)
