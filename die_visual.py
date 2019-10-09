from die import Die
import pygal


# create a two D6 dice
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling three D6 1000 times'
hist.x_labels = []
for x in range(3, max_result+1):
    hist.x_labels.append(str(x))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

# "" """ ''