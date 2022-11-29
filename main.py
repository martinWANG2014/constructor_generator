# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def generator(class_name, param_list):
    # constructor
    code = "class " + class_name + ":\n\tdef __init__(self," + ",".join(param_list) + "):\n"
    for param in param_list:
        code += "\t\tself." + param + " = " + param + "\n"

    code += "\n"

    # setters and getters
    for param in param_list:
        code += "\t@property\n\tdef " + param + "(self):\n\t\treturn self.__" + param + "\n\n"
        code += "\t@" + param + ".setter\n\tdef " + param + "(self, new_" + param + "):\n\t\tself.__" + param + " = new_" + param + "\n\n"

    return code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # parameter_list = ['fare_class', 'unit_fare_value', 'volume', 'container_type', 'orig', 'dest', 'date_avail', 'date_due', 'cat_customer']
    # my_code = generator("Demand", parameter_list)
    parameter_list = ['network', 'demand']
    my_code = generator("DataInstance", parameter_list)
    print(my_code)
