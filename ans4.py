employees = ['Ravi', 'Aman']
defaults = {"designation": 'Accountant', "salary": 7800}

res = dict.fromkeys(employees, defaults)
print(res)
print(res["Aman"])