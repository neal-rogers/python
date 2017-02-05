#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program creates a class, instantiates two objects, and outputs text."""


class Book(object):
    """
    Attributes:
        author (str): Book author.
        title (str): Book title.
    """

    author = ''
    title = ''

    def __init__(self, author, title):
        """
        Constructor for Book class.

        Args:
            author (str): Author name.
            title (str): Book title.

        Returns:
            None
        """

        self.author = author
        self.title = title

    def display(self):
        """
        Args: 
            None

        Returns:
            Formatted text.

        Example:
            >>> book_1.display()
            >>> Of Mice and Men, written by John Steinbeck
        """
        print '{}, written by {}'.format(self.title, self.author)

book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill A Mockingbird')

book1.display()
book2.display()
