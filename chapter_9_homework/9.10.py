# Type code for classes here
class ItemToPurchase:
  def __init__(self):
    self.item_name = 'none'
    self.item_price = 0
    self.item_quantity = 0
    self.purchase_cost = 0
    
  def print_item_cost(self):
    total_cost = self.item_price * self.item_quantity
    print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total_cost))
    
if __name__ == "__main__":
    # Type main section of code here
    #object 1
    item1 = ItemToPurchase()
    print('Item 1')
    item1.item_name = str(input('Enter the item name:\n'))
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    item1.purchase_cost = (item1.item_price * item1.item_quantity)

    #object 2
    item2 = ItemToPurchase()
    print('\nItem 2')
    item2.item_name = str(input('Enter the item name:\n'))
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    item2.purchase_cost = (item2.item_price * item2.item_quantity)
  
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()

    print('\nTotal: $%d' % (item1.purchase_cost + item2.purchase_cost))
