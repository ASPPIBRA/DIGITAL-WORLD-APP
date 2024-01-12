from django.urls import path
from admin_material2_pro import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Dashboard
    path('analytics/', views.analytics, name="analytics"),
    path('automotive/', views.automotive, name="automotive"),
    path('smart-home/', views.smart_home, name="smart_home"),
    path('billing/', views.billing, name="billing"),
    path('invoice/', views.invoice, name="invoice"),    
    path('sales/', views.sales, name="sales"),
    path('datatables/', views.datatables, name="datatables"),

    # Blockchain
    path('nft/', views.nft, name="nft"),
    path('registration/', views.registration, name="registration"),
    path('token/', views.token, name="token"),
    

    # Profile
    path('profile/profile-overview/', views.profile_overview, name="profile_overview"),
    path('profile/settings/', views.settings, name="settings"),
    path('profile/security/', views.security, name="security"),
    path('profile/wizard/', views.wizard, name="wizard"),   
    path('profile/reports/', views.reports, name="reports"),
    path('profile/new-user/', views.new_user, name="new_user"),    

    # Pages -> VR
    path('pages/vr/vr-default/', views.vr_default, name="vr_default"),
    path('pages/vr/vr-info/', views.vr_info, name="vr_info"),

    # Pages
    path('pages/rtl/', views.rtl, name="rtl"),
    path('pages/pricing/', views.pricing, name="pricing"),
    path('pages/blog/', views.blog, name="blog"),
    path('pages/post/', views.post, name="post"),
    path('pages/emporium/', views.emporium, name="emporium"),
    path('pages/contact/', views.contact, name="contact"),
    path('pages/projects/', views.projects, name="projects"),
    path('pages/project/', views.project, name="project"),
    path('pages/about_us/', views.about_us, name="about_us"),
    path('pages/widgets/', views.widgets, name="widgets"),
    path('pages/charts/', views.charts, name="charts"),
    path('pages/sweet-alerts/', views.sweet_alerts, name="sweet_alerts"),
    path('pages/notifications/', views.notifications, name="notifications"),
    
    # Applications
    path('applications/discover/', views.discover, name="discover"),
    path('applications/messages/', views.messages, name="messages"),
    path('applications/crm/', views.crm, name="crm"),       
     

    # Applications -> Projects
    path('applications/projects/general/', views.general, name="general"),
    path('applications/projects/timeline/', views.timeline, name="timeline"),
    path('applications/projects/new-project/', views.new_project, name="new_project"),
    path('applications/projects/all-projects/', views.all_projects, name="all_projects"),
    path('applications/projects/stats/', views.stats, name="stats"),
    path('applications/projects/calendar/', views.calendar, name="calendar"),
    path('applications/projects/kanban/', views.kanban, name="kanban"), 

    # Ecommerce -> Products
    path('ecommerce/products/new-product/', views.new_product, name="new_product"),  
    path('ecommerce/products/edit-product/', views.edit_product, name="edit_product"),  
    path('ecommerce/products/product-page/', views.product_page, name="product_page"),  
    path('ecommerce/products/products-list/', views.products_list, name="products_list"),

    # Ecommerce -> Orders
    path('ecommerce/orders/list/', views.order_list, name="order_list"),  
    path('ecommerce/orders/details/', views.order_details, name="order_details"),

    # Ecommerce -> Referral
    path('ecommerce/referral/', views.referral, name="referral"),
    path('ecommerce/outlet/', views.outlet, name="outlet"),  

    # Authentication -> Login
    path('accounts/basic-login/', views.BasicLoginView.as_view(), name="basic_login"),
    

    # Authentication -> Register
    path('accounts/basic-register/', views.basic_register, name="basic_register"),
    

    # Authentication -> Reset
    path('accounts/basic-reset/', views.BasicPasswordResetView.as_view(), name="basic_reset"),
    

    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/done/change-done.html'
    ), name="password_change_done"),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/done/basic.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/complete/basic.html'
    ), name='password_reset_complete'),

    # Authentication -> Verification
    path('accounts/basic-verification/', views.basic_verification, name="basic_verification"),
    

    # Authentication -> Lock
    path('accounts/basic-lock/', views.basic_lock, name="basic_lock"),
    

    # Error
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Logout
    path('accounts/logout/', views.logout_view, name='logout'),
]

