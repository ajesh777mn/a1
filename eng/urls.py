"""eng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp.views import *
from btech.views import *
from mca.views import *
from mba.views import *
from basicscience.views import *
from django.urls import path  #repath
from django.conf.urls.static import static 
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$',index,name='index'),
          path(r'^information_corner/$',information_corner,name='information_corner'),
         path(r'^info_corner/(?P<id>[0-9]+)',info_corner,name='info_corner'),

          
        path(r'^team/(?P<id>[0-9]+)',team,name='team'),

  
        path(r'^profile/$',profile,name='profile'),
        path(r'^kvmtrust/$',kvmtrust,name='kvmtrust'),
            path(r'^libintroduction1/$',libintroduction1,name='libintroduction1'),
            path(r'^libfaculty/$',libfaculty,name='libfaculty'),
            path(r'^course_intro/(?P<id>[0-9]+)',course_intro,name='course_intro'),
                path(r'^btechgovt/$',btechgovt,name='btechgovt'),
                path(r'^btechmgt/$',btechmgt,name='btechmgt'),
                path(r'^btechnri/$',btechnri,name='btechnri'),
                path(r'^faculty/$',faculty,name='faculty'),
                    path(r'^btech_faculties/(?P<id>[0-9]+)',btech_faculties,name='btech_faculties'),
                path(r'^engintroduction/$',engintroduction,name='engintroduction'),

                path(r'^manjula_devanada/$',manjula_devanada,name='manjula_devanada'),
                path(r'^minnukbenny/$',minnukbenny,name='minnukbenny'),
                path(r'^enquiry_form/$',enquiry_form,name='enquiry_form'),
                path(r'^brochures',brochures,name='brochures'),
                


                path(r'^mcaintro/$',mcaintro,name='mcaintro'),
                path(r'^mcaadmission/$',mcaadmission,name='mcaadmission'),
                path(r'^mcasyllabus/$',mcasyllabus,name='mcasyllabus'),
                path(r'^mcaprequestions/$',mcaprequestions,name='mcaprequestions'),
                path(r'^mcaextra/$',mcaextra,name='mcaextra'),
                path(r'^mcafaculty/$',mcafaculty,name='mcafaculty'),


                    path(r'^mbaintro/$',mbaintro,name='mbaintro'),
                    path(r'^mbaadmission/$',mbaadmission,name='mbaadmission'),
                    path(r'^mbabrochure/$',mbabrochure,name='mbabrochure'),
                    path(r'^mbaambassodors/$',mbaambassodors,name='mbaambassodors'),
                    path(r'^mbafaculty/$',mbafaculty,name='mbafaculty'),
                    path(r'^drannkavithamathew/$',drannkavithamathew,name='drannkavithamathew'),
                    path(r'^drvanoopkumar/$',drvanoopkumar,name='drvanoopkumar'),
                    path(r'^drdeepakashokkumar/$',drdeepakashokkumar,name='drdeepakashokkumar'),
                    path(r'^mba_faculties/(?P<id>[0-9]+)',mba_faculties,name='mba_faculties'),
                    path(r'^akhils/$',akhils,name='akhils'),



                    path(r'^basicintro/$',basicintro,name='basicintro'),
                    path(r'^basicfaculty/$',basicfaculty,name='basicfaculty'),

                    path(r'^courses/$',courses,name='courses'),
                    path(r'^eligibility_criteria/$',eligibility_criteria,name='eligibility_criteria'),
                    path(r'^mba_eligibility/$',mba_eligibility,name='mba_eligibility'),  
                    path(r'^mca_eligibility/$',mca_eligibility,name='mca_eligibility'),  
                    path(r'^scholarships/$',scholarships,name='scholarships'),  
                    path(r'^curricular/$',curricular,name='curricular'),  
                    path(r'^co_curricular/$',co_curricular,name='co_curricular'),
                    path(r'^transportation/$',transportation,name='transportation'),
                    path(r'^hostel/$',hostel,name='hostel'),
                    path(r'^iedc/$',iedc,name='iedc'),
                    path(r'^nature_club/$',nature_club,name='nature_club'),
                    path(r'^placement/$',placement,name='placement'),
                    path(r'^contact_us/$',contact_us,name='contact_us'),
                    path(r'^approval_recognition/$',approval_recognition,name='approval_recognition'),
                    path(r'^principal/$',principal,name='principal'),
                    path(r'^Vision_Mission/$',Vision_Mission,name='Vision_Mission'),
                    path(r'^route_map/$',route_map,name='route_map'),
                    
                    
                    path(r'^main_gallery/(?P<id>[0-9]+)',main_gallery,name='main_gallery'),
                    path(r'^photogallery/$',photogallery,name='photogallery'),
                    path(r'^photos_pseudocast/$',photos_pseudocast,name='photos_pseudocast'),
                    path(r'^photos_placement_training/$',photos_placement_training,name='photos_placement_training'),
                    path(r'^photos_iedc/$',photos_iedc,name='photos_iedc'),
                    path(r'^photos_arts_2017/$',photos_arts_2017,name='photos_arts_2017'),
                    path(r'^photos_engclg/$',photos_engclg,name='photos_engclg'),
                    path(r'^photos_sports/$',photos_sports,name='photos_sports'),
                    path(r'^photos_international_workshop/$',photos_international_workshop,name='photos_international_workshop'),
                    path(r'^photos_teloz_2k15/$',photos_teloz_2k15,name='photos_teloz_2k15'),
                    path(r'^photos_lagori_rocks/$',photos_lagori_rocks,name='photos_lagori_rocks'),
                    path(r'^photos_laboratories/$',photos_laboratories,name='photos_laboratories'),
                    path(r'^photos_infrastructure/$',photos_infrastructure,name='photos_infrastructure'),
                    path(r'^photos_campus/$',photos_campus,name='photos_campus'),
                    path(r'^photos_mba/$',photos_mba,name='photos_mba'),
                    path(r'^photos_intelli/$',photos_intelli,name='photos_intelli'),
                    path(r'^photos_IVmca/$',photos_IVmca,name='photos_IVmca'),

                    



                    path(r'^events/$',events,name='events'),
                    path(r'^keam-2021-online-preparation/$',keam2021onlinepreparation,name='keam-2021-online-preparation'),
                    path(r'^event_list/(?P<id>[0-9]+)',event_list,name='event_list'),

                    path(r'^notice_board/$',notice_board,name='notice_board'),
                    path(r'^useful_links/$',useful_links,name='useful_links'),
                    path(r'^alumni/$',alumni,name='alumni'),
                    path(r'^media_update/$',media_update,name='media_update'),
                    path(r'^University_Guidelines/$',University_Guidelines,name='University_Guidelines'),

        path(r'^all_events/$',all_events,name='all_events'),    
                    path(r'^news_events/(?P<id>[0-9]+)',news_events,name='news_events'),

        path(r'^seminar1/$',seminar1,name='seminar1'),

                    path(r'^university_update/$',university_update,name='university_update'),
                    path(r'^notification/(?P<id>[0-9]+)',notification,name='notification'),


                    

                    path(r'^darsanaramachandran/$',darsanaramachandran,name='darsanaramachandran'),
                    path(r'^mca_faculties/(?P<id>[0-9]+)',mca_faculties,name='mca_faculties'),
                    path(r'^basicscience_faculties/(?P<id>[0-9]+)',basicscience_faculties,name='basicscience_faculties'),
                    path(r'^testa/$',testa,name='testa'),
                            path(r'^online_appl/$',online_appl,name='online_appl'),
                            path(r'^mandatory_discl/$',mandatory_discl,name='mandatory_discl'),

 path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
