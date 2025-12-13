#apple = int(input('Введите кол-во яблок: '))
#child = int(input('Введите кол-во детей: '))
#print(apple // child)
#print(apple % child)

class apple:
    def __init__(self, count_apples):
        self.count_apples = count_apples
    def show_apples(self):
        return self.count_apples
    
class child:
    def __init__(self, count_children):
        self.count_children = count_children
    def show_children(self):
        return self.count_children
    
ap = apple(50)
ch = child(6)
print(f'Количество яблок каждому: {ap.show_apples() // ch.show_children()}, остаток яблок: {ap.show_apples() % ch.show_children()}')
