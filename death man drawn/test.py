class animal:
    type = 'none'
    name = ''
    def __init__(self, name) -> None:
        self.name = name
    def makeNoise(self):
        print('None')
class dog(animal):
    type = 'dog'
    def makeNoise(self):
        print('con cho sua cac cac cac')#cho sua la vl
cho = dog('concho')
print(isinstance(cho, dog))