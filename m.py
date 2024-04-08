class Cat:
  def __init__(self, age):
    self.age=age

  def set_age(self,num):
    self.age=num

  def get_age(self):
    return self

cat1=Cat(2)
cat2=Cat(4)
cat1.set_age(cat2.get_age())
cat2.set_age(5)
cat3=Cat(cat1.get_age() + cat2.get_age())
print(cat3.get_age())