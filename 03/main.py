from functools import total_ordering


@total_ordering
class CustomList(list):
    """Custom list class implementation"""

    def __init__(self, var: list):
        self.body = var

    @property
    def body(self) -> list:
        return self.__body

    @body.setter
    def body(self, value) -> None:
        if isinstance(value, list):
            self.__body = value
        else:
            raise ValueError("You need to provide a list as a positional argument")

    def __str__(self):
        return f"{self.body}"

    def __add__(self, other):
        body2 = other.body if isinstance(other, CustomList) else other
        res = list(map(lambda x, y: x + y, self.body, body2))

        bigger = self.body if (len(self.body) > len(body2)) else body2
        res += bigger[min(len(self.body), len(body2)) : max(len(self.body), len(body2))]
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        body2 = other.body if isinstance(other, CustomList) else other
        res = list(map(lambda x, y: x - y, self.body, body2))

        zeros = (
            [0 for _ in range(len(body2) - len(self.body))]
            if len(body2) > len(self.body)
            else []
        )
        res += list(
            map(
                lambda x, y: x - y,
                zeros,
                body2[
                    min(len(self.body), len(body2)) : max(len(self.body), len(body2))
                ],
            )
        )
        res += list(self.body[len(body2) : len(self.body)])
        return res

    def __rsub__(self, other):
        tmp = self.body.copy()
        self.body = other.copy()
        other = tmp
        return self.__sub__(other)

    def __eq__(self, other):
        return sum(self.body) == sum(other.body)

    def __lt__(self, other):
        return sum(self.body) < sum(other.body)

    def __gt__(self, other):
        return sum(self.body) > sum(other.body)

    def __le__(self, other):
        return sum(self.body) <= sum(other.body)

    def __ge__(self, other):
        return sum(self.body) >= sum(other.body)

    def __ne__(self, other):
        return sum(self.body) != sum(other.body)


def main():
    print(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]))
    print(CustomList([1]) - [2, 5])
    print([2, 5] - CustomList([1]))
    print("----------------")
    print(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]))
    print(CustomList([1]) + [2, 5])
    print([2, 5] + CustomList([1]))


if __name__ == "__main__":
    main()
