class Sorter:
    def bubble(self, iterable, f=lambda x: x, reverse=False):
        if reverse:
            for i in range(len(iterable)):
                for j in range(len(iterable)):
                    if f(iterable[i]) > f(iterable[j]):
                        temp = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp
        else:
            for i in range(len(iterable)):
                for j in range(len(iterable)):
                    if f(iterable[i]) < f(iterable[j]):
                        temp = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp
