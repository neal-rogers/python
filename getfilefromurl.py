#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program does stuff."""


import urllib2
import argparse


def downloadData(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data


def saveData(file_data):
    input_file = file_data.split()
    output_file = open("data.txt", "w")

    for line in input_file:
        output_file.write(line)
        output_file.write("\n")

    output_file.close()
    print 'Data saved to file. Exiting program...'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter a valid url.')
    args = parser.parse_args()

    if args.url:
        #url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
        data = downloadData(args.url)
        result = saveData(data)
    else:
        print 'Missing or invalid url.'


if __name__ == '__main__':
    main()