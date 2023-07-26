#!/usr/bin/env python3
"""

"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         takes two integer arguments page with default value 1 and page_size
         with default value 10.
         Use assert to verify that both arguments are integers greater than 0.
         Use index_range to find the correct indexes to paginate the
         dataset correctly
         and return the appropriate page of the dataset
         (i.e. the correct list of rows).
         If the input arguments are out of range for the dataset,
         an empty list should be returned.
        """

        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start index: StartIndex =
    (PageNumber - 1) * PageSize
    Calculate the end index: EndIndex = StartIndex + PageSize
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
