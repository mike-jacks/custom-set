class CustomSet:
    def __init__(self):
        custom_set: list[object] = []

    def add(self, item: object) -> None:
        if item not in self.custom_set:
            self.custom_set.append(item)
    def remove(self, item: object) -> None:
        pass
    def as_list(self) -> list[object]:
        pass
    def clear(self) -> None:
        pass

def main():
    pass

if __name__ == "__main__":
    main()
