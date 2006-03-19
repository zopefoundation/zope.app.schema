##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Implementation of ZCML action to register vocabulary factories.

$Id$
"""
from zope.app import zapi
from zope.interface import Interface, implements
from zope.schema.interfaces import IVocabularyRegistry
from zope.schema import vocabulary
from zope.testing import cleanup
from zope.app.schema.interfaces import IVocabularyFactory

class ZopeVocabularyRegistry(object):
    """IVocabularyRegistry that supports global and local utilities."""

    implements(IVocabularyRegistry)
    __slots__ = ()

    def get(self, context, name):
        """See zope.schema.interfaces.IVocabularyRegistry"""
        factory = zapi.getUtility(IVocabularyFactory, name)
        return factory(context)

def _clear():
    """Re-initialize the vocabulary registry."""
    # This should normally only be needed by the testing framework,
    # but is also used for module initialization.
    global vocabularyRegistry
    vocabulary._clear()
    vocabularyRegistry = vocabulary.getVocabularyRegistry()
    vocabulary._clear()
    vocabulary.setVocabularyRegistry(ZopeVocabularyRegistry())


_clear()
cleanup.addCleanUp(_clear)
