from django.conf.urls.defaults import *

from djfacet.constants import *

#faceted browsing application
urlpatterns = patterns('djfacet.views',
    # main handler: eg .../djfacet/?filter=religionname_Christian&resulttype=country
    url(r'^$', 'home', name='djfacet_home'),

    # eg .../djfacet/allfacets/?resulttype=religions
    url(r'^allfacets/$', 'allfacets', name='allfacets'),

    # eg .../djfacet/facet/regionname/?resulttype=religions&totitems=
    url(r'^facet/(?P<facet_name>\w+)/$', 'singlefacet', name='singlefacet'),

    # ajax calls :
    # eg ..../djfacet/update_facet?filter=regionname_ArcticRegion&resulttype=religions&activefacet=regionname
    url(r'^update_facet$', 'update_facet', name='update_facet'),
)