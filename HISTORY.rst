0.4.2 (2014-10-16)
------------------

- Fix a problem with SKOS matches.
- BC compatibilty break with 0.4.0 and 0.4.1: renamed the matchtypes broader to
  broad and narrower to narrow to be more inline with the SKOS standard.

0.4.1 (2014-10-15)
------------------

- Made the :class:`~skosprovider.providers.DictionaryProvider` return 
  :class:`~skosprovider.skos.Collection` objects with 
  :class:`~skosprovider.skos.Note` objects attached if available.
- Fix a problem in find operations when a concept or collection had no label
  attached to it. (#6) [dieuska]

0.4.0 (2014-10-02)
------------------

- Dropped support for Python 2.6 and 3.2.
- Added ability to add :class:`~skosprovider.skos.Note` to 
  :class:`~skosprovider.skos.Collection` and 
  :class:`~skosprovider.skos.ConceptScheme`.
- Added a :class:`~skosprovider.skos.ConceptScheme` to every provider. This
  ConceptScheme can then be passed on to Concepts and Collections. This allows
  Concepts and Collections that have left the context of their provider, to
  still refer back to the :class:`~skosprovider.skos.ConceptScheme` and thus 
  the :class:`skosprovider.providers.VocabularyProvider` where they originated.
- When querying the :class:`~skosprovider.registry.Registry` for providers,
  a :term:`URI` of an accompanying ConceptScheme can now also be used.
- Added :attr:`~skosprovider.skos.Concept.subordinate_arrays` attribute to
  :class:`~skosprovider.skos.Concept` and 
  :attr:`~skosprovider.skos.Collection.superordinates` to 
  :class:`~skosprovider.skos.Collection`. These attributes are based on the
  :term:`SKOS-THES` specification. They allow linking Concepts and Collections
  for the purpose of displaying a hierarchy.
- Expanded support for languages with 
  `language-tags <http://pypi.python.org/pypi/language-tags>`_ library. When
  generating a label, the language specification handles inexact language matches
  better. Eg. when asking for a label with language `nl` for a concept that only
  has `nl-BE` labels, these will now be returned while in the past this was not
  guaranteed. 
- Added `subject` to the metadata of a providers. This is a list of subjects
  or tags that help describe or type the provider. The 
  :class:`~skosprovider.registry.Registry` can now be searched for
  providers with a certain subject through the 
  :meth:`~skosprovider.registry.Registry.get_providers` method.

0.3.0 (2014-05-14)
------------------

- Added support for :term:`URI`. A :class:`skosprovider.skos.Concept`, 
  :class:`skosprovider.skos.Collection` or 
  :class:`skosprovider.skos.ConceptScheme` can now have a :term:`URI`.
- Query a :class:`skosprovider.providers.VocabularyProvider` or the 
  :class:`skosprovider.registry.Registry` by :term:`URI`.
- Added :mod:`skosprovider.uri` module to handle generating of :term:`URIS <URI>`.
- Added a :meth:`~skosprovider.providers.VocabularyProvider.get_top_concepts`
  method to :class:`skosprovider.providers.VocabularyProvider`. This method
  returns the Top Concepts in a ConceptScheme (the concepts that don't have
  a broader concept).
- Added the :meth:`~skosprovider.providers.VocabularyProvider.get_top_display` 
  and :meth:`~skosprovider.providers.VocabularyProvider.get_children_display`
  methods to handle generating a display hierarchy for a certain provider.
- A method that used to return a list of dicts containing an id and a label, 
  now also returns a uri and a type (concept/collection) for each dict. (#2)
- Provide list of valid noteTypes and labelTypes as attributes of Note and 
  Label so they can be used externally. (#4)
- Reworking tests. Now using pytest in stead of nose.
- Adding code coverage based on `Coveralls <https://coveralls.io>`_.

0.2.1 (2013-12-06)
------------------

- Make the :class:`skosprovider.providers.MemoryProvider` forward compatible
  by constructing :class:`skosprovider.skos.Concept` and 
  :class:`skosprovider.skos.Collection` objects with keywords.
- Soms minor fixes in documentation.
- Added an extra unit test.

0.2.0 (2013-05-16)
------------------

- Major rewrite and refactoring. Tried to keep BC in place as much as possible,
  but did change some stuff.
- Added a read only SKOS domain model in the :mod:`skosprovider.skos` module.
- Providers no longer return dicts as concepts, but instances of 
  :class:`skosprovider.skos.Concept`.
- Added support for skos collections with a 
  :class:`skosprovider.skos.Collection` object.
- Expanded concept query syntax. Now allows for querying on type 
  (concept or collection) and on collection membership. See 
  :meth:`skosprovider.providers.VocabularyProvider.find`.
- Added :func:`skosprovider.utils.dict_dumper`.

0.1.3 (2013-03-22)
------------------

- Find empty label now returns no results
- Find without a label now calls get_all

0.1.2 (2013-02-07)
------------------

- Providers can be removed from the registry
- Added the ability to get a single provider from the registry
- No longer possible to register the same provider twice

0.1.1 (2012-12-11)
------------------

- Some pep8 fixes
- Add support for tox
- Now tested for python 3.2
- Added skos:notes as an example to the unit tests.

0.1.0
-----

- Initial version
