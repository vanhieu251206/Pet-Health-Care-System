from django.test import TestCase
from django.contrib.auth import get_user_model
from pets.models import Product

class CustomUserModelTest(TestCase):
    def setUp(self):
        """Tạo user test"""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            phone="0123456789",
            role="customer"
        )

    def test_create_user(self):
        """Kiểm tra user được tạo đúng không"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.phone, "0123456789")
        self.assertEqual(self.user.role, "customer")
        self.assertTrue(self.user.check_password("testpassword"))

    def test_user_role_choices(self):
        """Kiểm tra role của user có hợp lệ không"""
        valid_roles = dict(self.user.ROLE_CHOICES)
        self.assertIn(self.user.role, valid_roles)

    def test_user_str_method(self):
        """Kiểm tra phương thức __str__ trả về username"""
        self.assertEqual(str(self.user), "testuser")


class ProductModelTest(TestCase):
    def setUp(self):
        """Tạo sản phẩm test"""
        self.product = Product.objects.create(
            name="Dog Food",
            price=200000.00,
            image="media/dog_food.jpg"
        )

    def test_create_product(self):
        """Kiểm tra sản phẩm có được tạo thành công không"""
        self.assertEqual(self.product.name, "Dog Food")
        self.assertEqual(self.product.price, 200000.00)
        self.assertEqual(self.product.image, "media/dog_food.jpg")

    def test_product_str_method(self):
        """Kiểm tra phương thức __str__ của Product"""
        self.assertEqual(str(self.product), "Dog Food")
