from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_material2_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

# Create your views here.

# Dashboard
def analytics(request):
  context = {
    'parent': 'dashboard',
    'segment': 'analytics'
  }
  return render(request, 'pages/dashboards/analytics.html', context)

def automotive(request):
  context = {
    'parent': 'dashboard',
    'segment': 'automotive'
  }
  return render(request, 'pages/dashboards/automotive.html', context)

def smart_home(request):
  context = {
    'parent': 'dashboard',
    'segment': 'smart_home'
  }
  return render(request, 'pages/dashboards/smart-home.html', context)

def billing(request):
  context = {
    'parent': 'dashboards',    
    'segment': 'billing'
  }
  return render(request, 'pages/dashboards/billing.html', context)

def invoice(request):
  context = {
    'parent': 'dashboards',    
    'segment': 'invoice'
  }
  return render(request, 'pages/dashboards/invoice.html', context)

def sales(request):
  context = {
    'parent': 'dashboards',        
    'segment': 'sales'
  }
  return render(request, 'pages/dashboards/sales.html', context)

def datatables(request):
  context = {
    'parent': 'dashboards',
    'segment': 'datatables'
  }
  return render(request, 'pages/dashboards/datatables.html', context)

# Blockchain

def nft(request):
  context = {
    'parent': 'blockchain',
    'segment': 'nft'
  }
  return render(request, 'pages/blockchain/nft.html', context)

def registration(request):
  context = {
    'parent': 'blockchain',
    'segment': 'registration'
  }
  return render(request, 'pages/blockchain/registration.html', context)

def token(request):
  context = {
    'parent': 'blockchaiin',
    'segment': 'token'
  }
  return render(request, 'pages/blockchain/token.html', context)

# Profile

def profile_overview(request):
  context = {
    'parent': 'profile',    
    'segment': 'profile_overview'
  }
  return render(request, 'pages/profile/overview.html', context)

def settings(request):
  context = {
    'parent': 'profile',    
    'segment': 'settings'
  }
  return render(request, 'pages/profile/settings.html', context)

def security(request):
  context = {
    'parent': 'profile',    
    'segment': 'security'
  }
  return render(request, 'pages/profile/security.html', context)

def wizard(request):
  context = {
    'parent': 'profile',    
    'segment': 'wizard'
  }
  return render(request, 'pages/profile/wizard.html', context)

def reports(request):
  context = {
    'parent': 'profile',    
    'segment': 'reports'
  }
  return render(request, 'pages/profile/reports.html', context)

def new_user(request):
  context = {
    'parent': 'profile',    
    'segment': 'new_user'
  }
  return render(request, 'pages/profile/new-user.html', context)


# Pages -> VR
def vr_default(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'vr',
    'segment': 'vr_default'
  }
  return render(request, 'pages/pages/vr/vr-default.html', context)

def vr_info(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'vr',
    'segment': 'vr_info'
  }
  return render(request, 'pages/pages/vr/vr-info.html', context)

# Pages
def rtl(request):
  context = {
    'parent': 'pages',
    'segment': 'rtl'
  }
  return render(request, 'pages/pages/rtl-page.html', context)

def pricing(request):
  context = {
    'parent': 'pages',
    'segment': 'pricing'
  }
  return render(request, 'pages/pages/pricing-page.html', context)

def blog(request):
  context = {
    'parent': 'pages',
    'segment': 'blog'
  }
  return render(request, 'pages/pages/blog.html', context)

def post(request):
  context = {
    'parent': 'pages',
    'segment': 'post'
  }
  return render(request, 'pages/pages/post.html', context)

def emporium(request):
  context = {
    'parent': 'pages',
    'segment': 'emporium'
  }
  return render(request, 'pages/pages/emporium.html', context)

def contact(request):
  context = {
    'parent': 'pages',
    'segment': 'contact'
  }
  return render(request, 'pages/pages/contact.html', context)

def projects(request):
  context = {
    'parent': 'pages',
    'segment': 'projects'
  }
  return render(request, 'pages/pages/projects.html', context)

def project(request):
  context = {
    'parent': 'pages',
    'segment': 'project'
  }
  return render(request, 'pages/pages/project.html', context)  

def about_us(request):
  context = {
    'parent': 'pages',
    'segment': 'about_us'
  }
  return render(request, 'pages/pages/about_us.html', context)

def widgets(request):
  context = {
    'parent': 'pages',
    'segment': 'widgets'
  }
  return render(request, 'pages/pages/widgets.html', context)

def charts(request):
  context = {
    'parent': 'pages',
    'segment': 'charts'
  }
  return render(request, 'pages/pages/charts.html', context)

def sweet_alerts(request):
  context = {
    'parent': 'pages',
    'segment': 'sweet_alerts'
  }
  return render(request, 'pages/pages/sweet-alerts.html', context)

def notifications(request):
  context = {
    'parent': 'pages',
    'segment': 'notifications'
  }
  return render(request, 'pages/pages/notifications.html', context)


# Applications

def discover(request):
  context = {
    'parent': 'applications',
    'segment': 'discover'
  }
  return render(request, 'pages/applications/discover.html', context)

def messages(request):
  context = {
    'parent': 'applications',    
    'segment': 'messages'
  }
  return render(request, 'pages/applications/messages.html', context)

def crm(request):
  context = {
    'parent': 'applications',
    'segment': 'crm'
  }
  return render(request, 'pages/applications/crm.html', context)
  


# Applications -> Projects
def general(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'general'
  }
  return render(request, 'pages/applications/projects/general.html', context)

def timeline(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'timeline'
  }
  return render(request, 'pages/applications/projects/timeline.html', context)

def new_project(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'new_project'
  }
  return render(request, 'pages/applications/projects/new-project.html', context)

def all_projects(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'all-projects'
  }
  return render(request, 'pages/applications/projects/all-projects.html', context)

def stats(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'stats'
  }
  return render(request, 'pages/applications/projects/stats.html', context)

def calendar(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'calendar'
  }
  return render(request, 'pages/applications/projects/calendar.html', context)

def kanban(request):
  context = {
    'parent': 'applications',
    'sub_parent': 'projects',
    'segment': 'kanban'
  }
  return render(request, 'pages/applications/projects/kanban.html', context)

# Ecommerce -> Products
def new_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'new_product'
  }
  return render(request, 'pages/ecommerce/products/new-product.html', context)

def edit_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'edit_product'
  }
  return render(request, 'pages/ecommerce/products/edit-product.html', context)

def product_page(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'product_page'
  }
  return render(request, 'pages/ecommerce/products/product-page.html', context)

def products_list(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'products_list'
  }
  return render(request, 'pages/ecommerce/products/products-list.html', context)

# Ecommerce -> Orders
def order_list(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_list'
  }
  return render(request, 'pages/ecommerce/orders/list.html', context)

def order_details(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_details'
  }
  return render(request, 'pages/ecommerce/orders/details.html', context)

# Ecommerce -> Referral
def referral(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'referral'
  }
  return render(request, 'pages/ecommerce/referral.html', context)

def outlet(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'outlet'
  }
  return render(request, 'pages/ecommerce/outlet.html', context)


# Authentication -> Login
class BasicLoginView(LoginView):
  template_name = 'accounts/signin/basic.html'
  form_class = LoginForm


# Authentication -> Register
def basic_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/basic-login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/signup/basic.html', context)

# Authentication -> Lock
def basic_lock(request):
  return render(request, 'accounts/lock/basic.html')


# Authentication -> Reset
class BasicPasswordResetView(PasswordResetView):
  template_name = 'accounts/reset/basic.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/reset-confirm/basic.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/change/basic.html'
  form_class = UserPasswordChangeForm

# Authentication -> Verification
def basic_verification(request):
  return render(request, 'accounts/verification/basic.html')


# Error
def error_404(request):
  return render(request, 'accounts/error/404.html')

def error_500(request):
  return render(request, 'accounts/error/500.html')

def logout_view(request):
  logout(request)
  return redirect('/accounts/basic-login/')