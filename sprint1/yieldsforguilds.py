from math import ceil
def assess_yield(number_of_plants, average_weight):
    total_weight = float(number_of_plants*average_weight/1000)
    if ceil(total_weight)>float(0):
        if ceil(total_weight)>float(100):
            return total_weight, 'Ожидается отличный урожай.'
        elif float(50)>=ceil(total_weight)>=float(100):
            return total_weight, 'Ожидается хороший урожай.'
        elif ceil(total_weight)<float(50):
            return total_weight, 'Урожай будет так себе.'
    else:
        return total_weight, 'Урожая не будет.'
total_weight, rating = assess_yield(101, 500)
print(total_weight, 'кг.', rating)