class MyClass:
    def __init__(self):
        self._protected_variable = "Thos os a private variable"

        def _protected_method(self):
            print("This is a private method")

my_class = MyClass()

print(my_class.__protected_variable)
print(my_class.__protected_method())