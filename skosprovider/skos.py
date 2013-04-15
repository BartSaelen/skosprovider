# -*- coding: utf-8 -*-

'''
This module contains a read-only model of the :term:`SKOS` specification.
'''

import collections


class Label:
    '''
    A :term:`SKOS` Label.
    '''

    label = None
    '''
    The label itself (eg. `churches`, `trees`, `Spitfires`, ...)
    '''

    type = "prefLabel"
    '''
    The type of this label ( `prefLabel`, `altLabel`, `hiddenLabel`).
    '''

    language = None
    '''
    The language the label is in (eg. `en`, `en-US`, `nl`, `nl-BE`).
    '''

    def __init__(self, label, type="prefLabel", language=None):
        self.label = label
        self.type = type
        self.language = language

    def __eq__(self, other):
        return self.__dict__ == (other if type(other) == dict else other.__dict__)

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, item):
        if item in self.__dict__.keys():
            return self.__dict__[item]

    @staticmethod
    def is_valid_type(type):
        '''
        Check if the argument is a valid SKOS label type.
        '''
        return type in ['prefLabel', 'altLabel', 'hiddenLabel']


class Note:
    '''
    A :term:`SKOS` Note.
    '''

    def __init__(self, note, type="note", language=None):
        self.note = note
        self.type = type
        self.language = language

    def __eq__(self, other):
        return self.__dict__ == (other if type(other) == dict else other.__dict__)

    def __ne__(self, other):
        return not self == other

    @staticmethod
    def is_valid_type(type):
        '''
        Check if the argument is a valid SKOS note type.
        '''
        return type in [
            'note',
            'changeNote',
            'definition',
            'editorialNote',
            'example',
            'historyNote',
            'scopeNote'
        ]


class ConceptScheme:
    '''
    A :term:`SKOS` ConceptScheme.
    '''

    def __init__(self, id, labels=[]):
        self.id = id
        self.labels = labels

    def label(self, language='any'):
        return label(self.labels, language)


class Concept(collections.Mapping):
    '''
    A :term:`SKOS` Concept.
    '''
   
    def __init__(self, id,
                 labels=[], notes=[],
                 broader=[], narrower=[], related=[]):
        self.id = id
        self.labels = [dict_to_label(l) for l in labels]
        self.notes = notes
        self.broader = broader
        self.narrower = narrower
        self.related = related

    def __getitem__(self, item):
        if item in self.__dict__.keys():
            return self.__dict__[item]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def label(self, language='any'):
        return label(self.labels, language)


class Collection:
    '''
    A :term:`SKOS` Collection.
    '''
    
    def __init__(self, id, labels=[]):
        self.id = id
        self.labels = labels

    def label(self, language='any'):
        return label(self.labels, language)


def label(labels=[], language='any'):
    '''
    Provide a label for a list of labels.

    The items in the list of labels are assumed to be either instances of 
    :class:`Label`, or dicts with at least the key `label` in them. These will 
    be passed to the :func:`dict_to_label` function.

    This method tries to find a label by looking if there's
    a pref label for the specified language. If there's no pref label, 
    it looks for an alt label. It disregards hidden labels.

    If language 'any' was specified, all labels will be considered, 
    regardless of language.

    To find a label without a specified language, pass `None` as language.

    If a language or None was specified, and no label could be found, this
    method will automatically try to find a label in some other language.

    Finally, if no label could be found, None is returned.
    '''
    alt = None
    for l in labels:
        l = dict_to_label(l)
        if language == 'any' or l.language == language:
            if l.type == 'prefLabel':
                return l
            if alt is None and l.type == 'altLabel':
                alt = l
    if alt is not None:
        return alt
    elif language != 'any':
        return label(labels, 'any')
    else:
        return None


def dict_to_label(dict):
    '''
    Transform a dict with keys `label`, `type` and `language` into a 
    :class:`Label`.

    If the argument passed is already a :class:`label`, this method just returns 
    the argument.
    '''
    if isinstance(dict, Label):
        return dict
    else:
        return Label(
            dict['label'], 
            dict['type'] if 'type' in dict else 'prefLabel', 
            dict['language'] if 'language' in dict else None
        )
