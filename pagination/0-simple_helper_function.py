#!/usr/bin/env python3
"""Helper function for pagination"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return a tuple of start and end index based on page and page_size"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
