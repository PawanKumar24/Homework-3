
# Pawan Kumar
# ID: 2046222
class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0, serving = '0.00'):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.serving = serving
        

    def get_calories(self, val):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * val
        return calories

    def setServing(self, val):
        self.serving = val
        

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print(f'Number of calories for {refactor(self.serving)} serving(s): {refactor(self.calories_calculator())}')
        

    def calories_calculator(self):
        return str(float(self.serving) * ((9*self.fat)+(4*self.carbs)+(4*self.protein)))
        

def refactor(phrase):
    wordArr = [word for word in phrase]
    for i in range(len(wordArr)):
        if wordArr[i] =='.':
            if (i+2)==len(wordArr):
                wordArr.append('0')
            
    
    val = ''.join(item for item in wordArr)
    return val

if __name__ == '__main__':
    name = str(input())
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    serving = input()
    item1 = FoodItem()
    item1.setServing(serving)
    item1.print_info()
    print()
    item2 = FoodItem(name, fat, carbs, protein, serving)
    item2.print_info()
