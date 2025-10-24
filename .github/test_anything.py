from Model import Item

def test_item():
    item = Item('milk',4,10)
    assert Item.name == 'milk'
