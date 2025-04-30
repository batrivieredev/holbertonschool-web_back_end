#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Return page info with deletion-resilient pagination.

        Args:
            index: Start index of the current page
            page_size: Size of the page

        Returns:
            Dict containing:
                index: Current start index
                next_index: Next index to query
                page_size: Current page size
                data: Current page data
        """
        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and index >= 0
        assert index <= max(indexed_data.keys())

        data = []
        next_index = index

        while len(data) < page_size and next_index <= max(indexed_data.keys()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
