class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        if len(self.collection) == 0:
            return -1
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) == 0:
            return -1
        return len(self.collection) // self.item_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if len(self.collection) == 0:
            return -1
        if page_index >= self.page_count() or page_index < 0:
            return -1
        else:
            if page_index == self.page_count() - 1:
                return len(self.collection) - (page_index * self.item_per_page)
            else:
                return self.item_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if len(self.collection) == 0:
            return -1
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            return item_index // self.item_per_page


# pag_helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
# # print(pag_helper.page_index(5))
# # print(pag_helper.page_index(2))
# # print(pag_helper.page_index(-20))
# # print(pag_helper.page_count())
# # print(pag_helper.item_count())
# print(pag_helper.page_item_count(1))


collection = range(1, 25)
helper = PaginationHelper(collection, 10)
print(helper.page_count())
print(helper.page_index(23))
print(helper.item_count())
print(helper.page_index(24))
