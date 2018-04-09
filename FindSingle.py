# -*- coding:utf-8 -*-
"""
Description:
To find a value which occurs only once in a list, where the list has the following spec:
    there is only one item occurs once, the other items all occur twice
"""


def method1(targets):
    counter = {}
    for item in targets:
        if item not in counter.keys():
            counter[item] = 1
        else:
            counter[item] += 1
    for key, value in counter.items():
        if value == 1:
            return key


def method2(targets):
    item_collections = set(targets)
    for unique_item in item_collections:
        try:
            targets.remove(unique_item)
            targets.remove(unique_item)
        except ValueError:
            return unique_item


def method3(targets):
    item_collections = sorted(targets)
    index = 0
    while index < len(item_collections) - 1:
        if item_collections[index] != item_collections[index+1]:
            return item_collections[index]
        index += 2
    return item_collections[-1]


class FindSingle(object):
    def __init__(self, target_list, find_callback):
        assert isinstance(target_list, list)
        self.targets = target_list
        self.callback = find_callback

    def run(self):
        return self.callback(self.targets)


if __name__ == "__main__":
    find = FindSingle([1, 4, 1, 4, 7], find_callback=method2)
    print find.run()