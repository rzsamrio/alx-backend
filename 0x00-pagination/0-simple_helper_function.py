#!/usr/bin/env python3
"""Helper functions."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range of items on a particular page."""
    return ((page - 1) * page_size, page * page_size)
