import unittest
from shoppingListApp import shoppingList
class shoppingListTestCase(unittest.TestCase) 
    def setUp(self):
        self.mylist=shoppingList()

    def test_list(self):
        self.assertEqual(self.mylist.list,[])

    def test_print_list(self):
        self.assertEqual(self.mylist.print_list,item)

    def test_add_item_to_list(self):
        self.assertEqual(self.mylist.add_item_to_list,item, len(shoppingList))
    
    def test_delete_item_from_list(self)
        self.assertEqual(self.mylist.add_item_to_list,item, len(shoppingList))

    def test_main(self):
        self.assertEqual(self.mylist.main,main())

        if __name__ == '__main__':
    unittest.main()