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
        """
        Cached dataset

        Returns:
            List[List]: The loaded dataset without header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0

        Returns:
            Dict[int, List]: Indexed dataset dictionary.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """
        Return page of dataset starting from index with page_size items,
        resilient to deletions.

        Args:
            index (int): Start index.
            page_size (int): Number of items to return.

        Returns:
            Dict[str, Any]: Dictionary with pagination data.
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and index >= 0
        assert index < len(self.dataset())

        data = []
        next_index = index
        collected = 0

        while collected < page_size and next_index < len(self.dataset()):
            item = indexed_data.get(next_index)
            if item:
                data.append(item)
                collected += 1
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
