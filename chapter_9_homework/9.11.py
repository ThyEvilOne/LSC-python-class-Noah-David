# Type code for classes here
cart_items = []
class ShoppingCart:
  def __init__(self, name = 'none', date = 'January 1, 2016'):
    self.customer_name = name
    self.current_date = date
    self.cart_items = [1,2,3,4]
    self.cost = 0
    self.total_cart = 0
  def add_item(self,item):
    self.cart_items.append(item)
    
  def get_num_items_in_cart(self):
      return len(self.cart_items)

  def get_cost_of_cart(self):
      return 10
  #def remove_item(self):
  #  requested_item = input('Enter item to remove:\n')
   # if requested_item in newlist.cart_items:
   #   newlist.cart_items.remove(requested_item)
   # else:
   #   print('Item not found in cart. Nothing removed.')
    
  #def modify_item(self):
   # requested_item = input('Enter item to modify:\n')
    #if requested_item in self.cart_items:
     # if requested_item.
    #else:
     # print('Item not found in cart. Nothing modified')
    
class ItemToPurchase:
  def __init__(self):
    self.item_name = 'none'
    self.item_price = 0
    self.item_quantity = 0
    self.purchase_cost = 0
    self.item_description = 'none'
    
  def print_item_description(self):
    print('%s: %s' % (self.item_name, self.item_description))
    
  def print_item_cost(self):
    total_cost = self.item_price * self.item_quantity
    print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total_cost))

def print_menu(menu_input):
    if menu_input == 'o':
        print('OUTPUT SHOPPING CART')
        print('%s\'s Shopping Cart - %s' % (cust1.customer_name, cust1.current_date))
        print('Number of Items: %d\n' % cust1.total_cart)
        print('SHOPPING CART IS EMPTY\n')
        print('Total: $%d\n' % cust1.cost)
        menu_input = 'q'
    if menu_input == 'a':
        print('ADD ITEM TO CART')
        print('Enter the item name:')
        print('Enter the item description:')
        print('Enter the item price:')
        print('Enter the item quantity:\n')
        
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit\n')  
    print('Choose an option:')
    
    
    while menu_input != 'q':
        menu_input = input('Choose an option:\n')

if __name__ == "__main__":
# Type main section of code here
    cust1 = ShoppingCart
    cust1.customer_name = input('Enter customer\'s name:\n')
    cust1.current_date = input('Enter today\'s date:\n')
    cust1.total_cart = 0
    cust1.cost = 0
    print('\nCustomer name: %s' % cust1.customer_name)
    print('Today\'s date: %s\n' % cust1.current_date)
    print_menu(input())
