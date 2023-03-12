from typing import *

class Sorting:
    """Class to contain all of the sorting algorithms
    """
    def bubble(
            self,
            iterable: Iterable,
            f:Callable[[Any], Any]=lambda x: x,
            reverse:bool=False
        ):
        """Sort iterable using bubble algorithm.

        Args:
            iterable (Iterable): iterable to sort.
            f (Callable[[Any], Any], optional): function to apply and extract
                the data of the iterable. Defaults to lambda x:x.
            reverse (bool, optional): if the sorting must be in reverse.
                Defaults to False.
        """
        # In reverse
        if reverse:
            for i in range(len(iterable)):
                for j in range(len(iterable)):
                    # Swaping if a > b
                    if f(iterable[i]) > f(iterable[j]):
                        temp: Any = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp
        else:
            for i in range(len(iterable)):
                for j in range(len(iterable)):
                    # Swaping if a < b
                    if f(iterable[i]) < f(iterable[j]):
                        temp: Any = iterable[i]
                        iterable[i] = iterable[j]
                        iterable[j] = temp
