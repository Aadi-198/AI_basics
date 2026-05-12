def linear_expressions(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        return "Error"
    
    result = sum(a * b for a, b in zip(vector_1, vector_2))
    return result

v1 = [float(x) for x in input("Enter values: ").split()]
v2 = [float(x) for x in input("Enter values: ").split()]

output = linear_expressions(v1, v2)
print(f"The output is {output:g}")