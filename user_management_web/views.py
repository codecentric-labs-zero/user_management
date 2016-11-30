from distutils.command.register import register

from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from rolepermissions.shortcuts import assign_role
from rolepermissions.verifications import has_permission, has_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.shortcuts import available_perm_status, get_user_role
from models import ProductAndPartsForm, sparePartsFormSet,Product


@login_required
def main_control(request):
    if request.user.is_superuser:
        return redirect("super_user_page")
    else:
        page = ''
        if has_role(request.user, 'lead_recruiter'):
            page = 'recruiter_page'
        elif has_role(request.user, 'recruiter'):
            page = 'recruiter_page'
    return redirect(page)


@login_required
def lead_page(request):
    return HttpResponse("welcome lead recruiter")


@login_required
def super_user_page(request):
    return HttpResponse("welcome SUPER USER")


@login_required
def recruiter_page(request):
    return render(request, 'recruitment_page.html')


@login_required
@has_permission_decorator('view_recruitment_page')
def users(request):
    result = []
    for user in User.objects.all():
        if get_user_role(user) is None:
            result.append((user, None, None))
        else:
            result.append((user, get_user_role(user), available_perm_status(user)))
    return render(request, 'users.html', {'result': result})


@login_required
def add_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST.get('username', None),
            password=request.POST.get('username', None),
            email=None
        )
        if request.user.is_superuser:
            assign_role(user, 'lead_recruiter')
        else:
            assign_role(user, 'recruiter')
        user.save()
        return redirect('/web/users')
    return render(request, 'add_user.html')


@login_required()
def add_products(request):
    if request.method == 'POST':
        productForm = ProductAndPartsForm(request.POST)
        if productForm.is_valid():
            product = productForm.save(commit=False)
            product_parts_form_set = sparePartsFormSet(request.POST, instance=product)
            if product_parts_form_set.is_valid():
                product.save()
                product_parts_form_set.save()
                return redirect('/web/products')
    else:

        productForm = ProductAndPartsForm()
        product_parts = sparePartsFormSet(instance=Product())

    return render(request, 'add_products.html',
                  {'productForm': productForm, 'product_parts_form_set': product_parts})

@login_required()
def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'all_products': all_products})
