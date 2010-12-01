===============
INTRODUCTION
===============

This is an experiment. This will be a custom CMS that will manage a catalog of
images and information from locations for movie locations and local tv shows.

The interesting/geeky part of this 'custom CMS' is that I'm using the grok and
Dolmen project to build this stuff. I don't know if I'll succeed.

We'll se.

Note to self: Add the following line to configure.zcml in menhir.skin.lightblue
in order to workaround reduced dependencies on grok 1.2 release:

  <include package="zope.browserresource" file="meta.zcml" />
  <include package="zope.browserresource" />
