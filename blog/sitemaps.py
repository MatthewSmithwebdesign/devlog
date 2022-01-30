from django.contrib.sitemaps import Sitemap
from feed.models import BlogPost


class BlogPostSitemap(Sitemap):
    changefreq ='monthly'
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_on