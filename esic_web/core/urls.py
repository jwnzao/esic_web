from django.urls import path
from .views import home_page, articles_page, actualites_page, presentation_page, formations, dates, temoignages, evenements, formationDevelopper, businessEngineering, dataScience, cybersecurity, certifications

urlpatterns = [
    # path('home/', include('home.urls')),
    path("", home_page, name="home"),
    path("articles", articles_page, name="articles"),
    path("actualites", actualites_page, name="actualites"),
    path("presentation", presentation_page, name="presentation"),
    path("formations", formations, name="formations"),
    path("formations/formation-developper", formationDevelopper, name="formationDevelopper"),
    path("formations/business-engineering", businessEngineering, name="businessEngineering"),
    path("formations/dat-science", dataScience, name="dataScience"),
    path("formations/cybersecurity", cybersecurity, name="cybersecurity"),
    path("formations/certifications", certifications, name="certifications"),
    path("dates", dates, name="dates"),
    path("temoignages", temoignages, name="temoignages"),
    path("evenements", evenements, name="evenements"),
]
