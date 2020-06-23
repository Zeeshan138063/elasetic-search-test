# create a connection from your Django application to ElasticSearch.

from elasticsearch_dsl.connections import connections

connections.create_connection()

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

from elasticsearch_dsl import DocType, Text, Date


class BlogPostIndex(DocType):
    # The DocType works as a wrapper to enable you to write an index like a model
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'blogpost-index'


def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
