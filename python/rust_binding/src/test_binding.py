import rust_binding

print(rust_binding.__doc__)
print(rust_binding.sum_as_string(5, 6))

my_number = rust_binding.Number(5)
print(my_number)
