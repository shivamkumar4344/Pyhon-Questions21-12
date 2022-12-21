sample_dict = {
    "name": "Avinash",
    "age": 45,
    "salary": 98000,
    "city": "London"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)