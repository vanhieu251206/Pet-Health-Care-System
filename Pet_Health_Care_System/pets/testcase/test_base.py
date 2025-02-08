from django.test import TestCase, Client
from django.urls import reverse

class BaseTemplateTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_base_template_loads_successfully(self):
        """Kiểm tra `base.html` có load không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/base.html')

    def test_navbar_exists(self):
        """Kiểm tra Navbar có hiển thị không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertContains(response, '<nav', html=False)
        self.assertContains(response, 'Trang chủ')
        self.assertContains(response, 'Cửa hàng')

    def test_footer_exists(self):
        """Kiểm tra Footer có hiển thị không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertContains(response, '<footer', html=False)
        self.assertContains(response, 'Về Chúng Tôi')

    def test_search_bar_exists(self):
        """Kiểm tra ô tìm kiếm có hiển thị không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertContains(response, 'Tìm kiếm sản phẩm')

    def test_login_and_register_links(self):
        """Kiểm tra link Đăng nhập và Đăng ký có tồn tại không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertContains(response, reverse('pets:login_page'))
        self.assertContains(response, reverse('pets:register_page'))

    def test_all_blocks_render_content(self):
        """Kiểm tra các block có render ra nội dung không"""
        response = self.client.get(reverse('pets:guest_dashboard'))
        self.assertContains(response, 'carousel', html=False)  # kiểm tra slider
        self.assertContains(response, 'footer-container', html=False)  # kiểm tra footer
