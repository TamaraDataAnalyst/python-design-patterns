#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import csv
import json
import xml.etree.ElementTree as etree

class CSVDataExtractor:
    def __init__(self, filepath):
        self.data = csv.DictReader (open(filepath, mode="r", newline=""))

    @property
    def parsed_data(self):
        return self.data

class JSONDataExtractor:
    def __init__(self, filepath):
        with open(filepath, mode="r") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def data_extractor(filepath):
    suffix = filepath.split('.')[-1]
    if suffix in ('csv', 'txt', 'tsv'):
        ext_extractor = CSVDataExtractor
    elif filepath.endswith('json'):
        ext_extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        ext_extractor = XMLDataExtractor
    else:
        raise ValueError(f'Cannot extract data from {filepath}')
    return ext_extractor(filepath)

def extractor_data_from(filepath, dialect='excel'):
    extractor_obj = None
    try:
        extractor_obj = data_extractor(filepath)
    except ValueError as e:
        print(e)
    return extractor_obj


if __name__ =='__main__':
    from itertools import islice
    path = '../../data/movies.json'
    csv_factory = extractor_data_from(path)
    json_data = csv_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()
    
    
    