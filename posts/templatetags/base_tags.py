from django import template
from .. import models



register = template.Library()

@register.simple_tag
def title():
    return "YT Team"


@register.inclusion_tag("posts/partials/home_navbar.html")
def home_navbar():
    pass


@register.inclusion_tag("posts/partials/navbar_Category.html")
def Category_navbar():
    Category = {
        "cats": models.Category.objects.actived(),
    }
    return Category





# @register.inclusion_tag("posts/partials/Songers_navbar_home.html")
# def Songer_navbar():
#     Songer = {
#         "Sonr": models.Songer.objects.published(),
#     }
#     return Songer
#
#
# @register.inclusion_tag("posts/partials/Songer_navbar_home.html")
# def Songer2_navbar(slug):
#     Songer = {
#         "Son": models.Songer.objects.get(slug = slug),
#     }
#     return Songer
#
# @register.inclusion_tag("posts/partials/panel.html")
# def panel_navbar():
#     pass




# @register.inclusion_tag("registration/partials/link.html")
# def link(request,link_name,content,classes):
#     context = {
#         "request": request,
#         "link_name": link_name,
#         "link" : "account:{}".format(link_name),
#         "content": content,
#         "classes":classes,
#     }
#     return context
