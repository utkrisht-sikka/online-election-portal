from django.urls import path, re_path
from django.conf.urls import url, include

from .views import home, login, cand_profile, register_candidate, register_party, register_voter, register_official, register, f_voter_view1
from .views import  f_voter_view2, f_voter_view3, ec_official_profile, admin_official_profile, register,party_view,election_result
urlpatterns = [
    path('', home, name='home'),
    path(r'login', login, name='login'),
    path('register', register_voter, name='register'),
    path('profile/candidate', cand_profile, name='cand_profile'),
    path('profile/ec_official', ec_official_profile, name='ec_official_profile'),
    path('profile/admin_official', admin_official_profile, name='admin_official_profile'),
    path('register/candidate/<id>/', register_candidate, name="reg_cand"),
    path('register/party', register_party, name="register_party"),
    path('register/official', register_official, name="register_official"),
    path('login/voter_view1/<id>/',f_voter_view1,name="voter_view1"),
    path('login/voter_view2/<id>/',f_voter_view2,name="voter_view2"),
    path('login/voter_view3/<id>/',f_voter_view3,name="voter_view3"),
    path('login/party',party_view,name="party_view"),
    path('register/voter',register_voter,name="reg_person"),
    path('result/',election_result,name="result"),
]
