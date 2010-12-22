#zope stuff
from zope.interface import Interface
from zope.container.constraints import contains
from zope import schema

#grok stuff
import grok

#dolmen stuff
from dolmen.app.site import Dolmen
from dolmen.file import ImageField
from dolmen.blob import BlobProperty
from dolmen import content
from dolmen.app.security.content import CanAddContent

from cinezune.locaciones import LocacionesMessageFactory as _

class Locaciones(Dolmen):
    content.nofactory()
    title= _(u"Cinezune Locations site")

class ILocation (Interface):
    contains('.IPicture')
    title = schema.TextLine( title=_(u"Location title"),
                             description = _(u"Give a title of the site")
                             )
    private_description = schema.Text(
        title=_(u"Private description"),
        description=_(u"This is a private description of a location. This information will not be public.")
        )

    address = schema.Text(
            title=_(u"Location address"),
            description=_(u"Please write the address of this location. This information will not be public."),
        )

    map_url = schema.URI (
            title=_(u"Google Map URL"),
            description=_(u"This is the URL of a google map with information about this location. This information will not be public."),
            required=False,
        )

    sketch = ImageField(
            title=_(u"Sketch Map"),
            description=_(u"Please upload an image for the sketch map. This information will not be public."),
            required=False,
        )

class Location (content.Container):
    grok.implements(ILocation)
    content.schema(ILocation)
    content.name(u'A Location with photos')
    content.require(CanAddContent)
    sketch = BlobProperty(ILocation['sketch'])

class IPicture(content.IBaseContent):
    """A Picture of a location
    """
    description = schema.Text(
        title=_(u"Private description"),
        description=_(u"This is a private description of a location. This information will not be public.")
        )

    image = ImageField(
            title=_(u"Picture"),
            description=_(u"Please upload an image"),
            required=True,
        )

class Picture(content.Content):
    content.schema(IPicture)
    content.name(u'A photo of the location')
    content.require(CanAddContent)
    image = BlobProperty(IPicture['image'])
