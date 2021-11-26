get_deler = 0
for i in range(1, 100):
    max_devisor = 1
    for j in range(1, i-1):
        if i % j == 0:
            max_devisor = j
    print(f"{i} | {max_devisor}")
    if max_devisor/i >= get_deler:
        get_deler = max_devisor/i
print(get_deler)
