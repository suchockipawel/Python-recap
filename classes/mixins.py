class ProductManagemntMixin:
    def add_product(self, product_name):
        print(f'Product {product_name} added sucessfully')
    def remove_product(self, product_name):
        print(f'Product {product_name} removed sucessfully')

class UserPreferenceMixin:
    def set_preferred_theme(self, theme):
        print(f'User preferred theme set to {theme}')
    def set_notification_preferrences (self, email=True, sms=False):
        print(f'Notification preferences updated: Email={email}, SMS={sms}')

class WebApplication:
    def display_homepage(self):
        print('Displaying homepage of the web application')

class UserDashboard(WebApplication, ProductManagemntMixin, UserPreferenceMixin):
    def display_dashboard(self):
        self.display_homepage()
        print('Display user dashboard')
user_dashboard = UserDashboard()
user_dashboard.add_product('Smart Phone')
user_dashboard.set_preferred_theme('Dark Mode')
user_dashboard.set_notification_preferrences()
user_dashboard.display_dashboard()
