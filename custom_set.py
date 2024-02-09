class CustomSet:
    def __init__(self) -> None:
        self.custom_set: list[object] = []

    def add(self, item: object) -> None:
        if item not in self.custom_set:
            self.custom_set.append(item)
        else:
            print(f"{item} is already in the set")

    def remove(self, item: object) -> None:
        if item in self.custom_set:
            self.custom_set.remove(item)
        else:
            print(f"{item} is not in the set")

    def as_list(self) -> list[object]:
        return self.custom_set

    def clear(self) -> None:
        self.custom_set = []

def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list())

    my_set.remove("item 2")
    print(my_set.as_list())

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving forward")
    
    my_set.clear()

    print(my_set.clear())

if __name__ == "__main__":
    main()
