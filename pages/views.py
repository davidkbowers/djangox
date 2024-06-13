from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class BlogPageView(TemplateView):
    template_name = "pages/blog.html" 


class ClassesPageView(TemplateView):
    template_name = "pages/classes.html"  


class CommunityPageView(TemplateView):
    template_name = "pages/community.html"  


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"   


class ShopPageView(TemplateView):
    template_name = "pages/shop.html"  