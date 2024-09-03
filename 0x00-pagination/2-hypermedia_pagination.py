#!/usr/bin/env python3
"""Baby name list."""
from typing import Tuple, List, Dict
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a Server."""
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
        """Return a page of baby names."""
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = None, page_size: int = 10) -> Dict:
        """Return a traversable list of baby names."""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None if page >= total_pages else page + 1
        res = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": total_pages,
        }
        return res


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range of items on a particular page."""
    return ((page - 1) * page_size, page * page_size)
