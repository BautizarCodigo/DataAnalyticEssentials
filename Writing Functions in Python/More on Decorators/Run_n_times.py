# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')