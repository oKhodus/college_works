class Temp:
    def __init__(self):
        pass

    def __del__(self):
        print("Object deleted")

t = Temp()
del t