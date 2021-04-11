age_list = [47, 12, 28, 52,35]

for i, age in enumerate(age_list):
    if age < 18:
        is_minor = True
        age_list[i] = "minor"
    
print(age_list)