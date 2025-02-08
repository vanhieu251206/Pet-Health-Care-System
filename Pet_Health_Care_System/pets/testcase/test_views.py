from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from pets.models import Product

CustomUser = get_user_model()

class ViewsTest(TestCase):
    def setUp(self):
        """Thiết lập môi trường test"""
        self.client = Client()

        # Tạo user test với role là customer
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpassword",
            role="customer"
        )

        # Tạo sản phẩm test cho shop
        self.product = Product.objects.create(
            name="Dog Food",
            price=200000.00,
            image="media/dog_food.jpg"
        )

    ## ---- 1. TEST HIỂN THỊ CÁC TRANG ---- ##
    def test_guest_dashboard_view(self):
        """Kiểm tra trang guest_dashboard"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/guest_dashboard.html')

    def test_login_page_view(self):
        """Kiểm tra trang login"""
        response = self.client.get(reverse('pets:login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/login_page.html')

    def test_register_page_view(self):
        """Kiểm tra trang đăng ký"""
        response = self.client.get(reverse('pets:register_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/register_page.html')

    def test_select_role_page_view(self):
        """Kiểm tra trang chọn vai trò"""
        response = self.client.get(reverse('pets:select_role'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/select_role.html')

    def test_cart_page_view(self):
        """Kiểm tra trang giỏ hàng"""
        response = self.client.get(reverse('pets:cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/cart.html')

    def test_checkout_page_view(self):
        """Kiểm tra trang checkout"""
        response = self.client.get(reverse('pets:checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/checkout.html')

    def test_shop_page_view(self):
        """Kiểm tra trang shop hiển thị sản phẩm"""
        response = self.client.get(reverse('pets:shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/shop.html')
        self.assertContains(response, self.product.name)

    ## ---- 2. TEST CHỨC NĂNG LOGIN ---- ##
    def test_login_success(self):
        """Kiểm tra đăng nhập thành công"""
        response = self.client.post(reverse('pets:login_view'), {
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)  # Kiểm tra redirect thành công
        self.assertRedirects(response, reverse('staff:tong_quan'))

    def test_login_fail_wrong_password(self):
        """Kiểm tra đăng nhập thất bại khi nhập sai mật khẩu"""
        response = self.client.post(reverse('pets:login_view'), {
            'username': 'testuser',
            'password': 'wrongpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)  # Kiểm tra redirect lại trang login
        self.assertRedirects(response, reverse('pets:login_page'))

    def test_login_fail_wrong_role(self):
        """Kiểm tra đăng nhập thất bại khi nhập sai role"""
        response = self.client.post(reverse('pets:login_view'), {
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'staff'  # Sai role
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pets:login_page'))

    def test_login_fail_missing_role(self):
        """Kiểm tra đăng nhập thất bại khi thiếu role"""
        response = self.client.post(reverse('pets:login_view'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pets:login_page'))

    ## ---- 3. TEST CHỨC NĂNG REGISTER ---- ##
    def test_register_success(self):
        """Kiểm tra đăng ký thành công"""
        response = self.client.post(reverse('pets:register_view'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password_confirm': 'newpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)  # Kiểm tra redirect thành công
        self.assertTrue(CustomUser.objects.filter(username="newuser").exists())

    def test_register_fail_password_mismatch(self):
        """Kiểm tra đăng ký thất bại do mật khẩu không khớp"""
        response = self.client.post(reverse('pets:register_view'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password_confirm': 'wrongpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CustomUser.objects.filter(username="newuser").exists())

    def test_register_fail_existing_username(self):
        """Kiểm tra đăng ký thất bại do username đã tồn tại"""
        response = self.client.post(reverse('pets:register_view'), {
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password_confirm': 'newpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.filter(username="testuser").count(), 1)

    def test_register_fail_existing_email(self):
        """Kiểm tra đăng ký thất bại do email đã được sử dụng"""
        response = self.client.post(reverse('pets:register_view'), {
            'username': 'newuser',
            'email': 'testuser@example.com',
            'password': 'newpassword',
            'password_confirm': 'newpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CustomUser.objects.filter(username="newuser").exists())
