#zope stuff
from zope.interface import Interface
from zope.container.constraints import contains
from zope import schema
from zope.size import ISized

#grok stuff
import grok

#dolmen stuff
from dolmen import menu
from dolmen.app.site import Dolmen
from dolmen.file import ImageField
from dolmen.blob import BlobProperty
from dolmen import content
from dolmen.app.security.content import CanAddContent, CanViewContent, CanListContent
from dolmen.app.layout import models
from dolmen.app.container import listing
from dolmen.app import layout

#menhir imports
from menhir.contenttype.image import IImage, Image, ImagePopup

#cinezune stuff
from cinezune.locaciones import LocacionesMessageFactory as _

class Locaciones(Dolmen):
    content.nofactory()
    title= _(u"Cinezune")

class LocacionesIndex(models.Index):
    grok.context(Locaciones)
    content.require(CanViewContent)

class IPicture(IImage):
    """A Picture of a location
    """
    description = schema.Text(
        title=_(u"Private description"),
        description=_(u"This is a private description of a location. This information will not be public.")
        )


class Picture(Image):
    """A simple image storing its data in a blob.
    """
    content.name(u'A photo of the location')
    content.schema(IPicture)


class ILocation (Interface):
    contains(IPicture)
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

class LocationIndex(models.Index):
    grok.context(Location)
    content.require(CanViewContent)
    @property
    def values(self):
        return dict(self.context.values())

@menu.menuentry(layout.ContextualMenu, order=15)
class LocationExtraInfo(models.Page):
    grok.title(_(u"Info privada"))
    grok.context(Location)
    content.require(CanListContent)

    def content(self):
        ImagePopup.need()
        url = self.url(self.context)
        self.sketch_size = ISized(self.context.sketch).sizeForDisplay()
        self.sketch_preview = "%s/++thumbnail++sketch.preview" % url
        self.sketch_popup_url = "%s/++thumbnail++sketch.large" % url
        self.sketch_download_url = "%s/++download++sketch" % url
        return super(models.Page,self).content()
