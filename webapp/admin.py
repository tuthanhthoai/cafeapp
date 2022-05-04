from flask_admin.contrib.sqla import ModelView
from webapp import db, app
from webapp.models import Category, Product, Tag, User, UserRole
from flask_admin import BaseView, expose, Admin, AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect

import utils


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class ProductView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_exclude_list = ["image"]
    column_filters = ["name", "price"]


class ReportView(BaseView):
    @expose("/")
    def report(self):
        return "Report Page"

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render("admin/index.html")


class LogoutView(AuthenticatedBaseView):
    @expose("/")
    def logout(self):
        logout_user()
        return redirect("/")


class UserView(AuthenticatedModelView):
    column_exclude_list = ["password", "avatar"]


admin = Admin(
    app=app,
    name="Admin Page",
    template_mode="bootstrap4",
    index_view=MyAdminIndexView()
)
admin.add_view(AuthenticatedModelView(Category, db.session, name="Category"))
admin.add_view(ProductView(Product, db.session, name="Product"))
admin.add_view(AuthenticatedModelView(Tag, db.session, name="Tag"))
admin.add_view(UserView(User, db.session, name="User"))
admin.add_view(ReportView(name="Report"))
admin.add_view(LogoutView(name="Logout"))
