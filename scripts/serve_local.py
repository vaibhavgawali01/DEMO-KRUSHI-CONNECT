# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import urllib.request
import urllib.error

PORT = 8080
DIRECTORY = "dist"
BACKEND_URL = "http://localhost:8082"

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def proxy_to_backend(self):
        target_url = BACKEND_URL + self.path
        headers = {k: v for k, v in self.headers.items() if k.lower() not in ('host', 'connection')}
        body = None
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length)

        req = urllib.request.Request(target_url, data=body, headers=headers, method=self.command)
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                resp_body = resp.read()
                self.send_response(resp.status)
                for k, v in resp.getheaders():
                    if k.lower() not in ('transfer-encoding', 'connection', 'content-length'):
                        self.send_header(k, v)
                self.send_header('Content-Length', str(len(resp_body)))
                self.end_headers()
                self.wfile.write(resp_body)
        except urllib.error.HTTPError as e:
            err_body = e.read()
            self.send_response(e.code)
            for k, v in e.headers.items():
                if k.lower() not in ('transfer-encoding', 'connection', 'content-length'):
                    self.send_header(k, v)
            self.send_header('Content-Length', str(len(err_body)))
            self.end_headers()
            self.wfile.write(err_body)
        except Exception as e:
            err_json = f'{{"error": "Backend offline or unreachable: {str(e)}"}}'.encode('utf-8')
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(err_json)))
            self.end_headers()
            self.wfile.write(err_json)

    def do_POST(self):
        if self.path.startswith('/api/'):
            self.proxy_to_backend()
        else:
            self.send_error(405, "Method Not Allowed")

    def do_PUT(self):
        if self.path.startswith('/api/'):
            self.proxy_to_backend()
        else:
            self.send_error(405, "Method Not Allowed")

    def do_DELETE(self):
        if self.path.startswith('/api/'):
            self.proxy_to_backend()
        else:
            self.send_error(405, "Method Not Allowed")

    def do_GET(self):
        if self.path.startswith('/api/'):
            self.proxy_to_backend()
            return

        parts = self.path.split('?')
        clean_path = parts[0].split('#')[0].rstrip('/')
        query = '?' + parts[1] if len(parts) > 1 else ''

        # Map common clean routes
        route_map = {
            '/about': '/about.html',
            '/contact': '/contact.html',
            '/products': '/products.html',
            '/weather': '/weather.html',
            '/farming-tips': '/farming-tips.html',
            '/fertilizer-calculator': '/fertilizer-calc.html',
            '/fertilizer-calc': '/fertilizer-calc.html',
            '/faq': '/faq.html',
            '/offers': '/offers.html',
            '/login': '/login.html',
            '/register': '/register.html',
            '/forgot-password': '/forgot-password.html',
            '/admin': '/admin-dashboard.html',
            '/admin/dashboard': '/admin-dashboard.html',
            '/admin-dashboard': '/admin-dashboard.html',
            '/admin/products': '/admin-products.html',
            '/admin-products': '/admin-products.html',
            '/admin/product-form': '/admin-product-form.html',
            '/admin-product-form': '/admin-product-form.html',
            '/admin/categories': '/admin-categories.html',
            '/admin-categories': '/admin-categories.html',
            '/admin/udhari': '/admin-udhari.html',
            '/admin-udhari': '/admin-udhari.html',
            '/admin/inventory': '/admin-inventory.html',
            '/admin-inventory': '/admin-inventory.html',
            '/admin/customers': '/admin-customers.html',
            '/admin-customers': '/admin-customers.html',
            '/admin/reviews': '/admin-reviews.html',
            '/admin-reviews': '/admin-reviews.html',
            '/admin/reports': '/admin-reports.html',
            '/admin-reports': '/admin-reports.html',
            '/admin/backup': '/admin-backup.html',
            '/admin-backup': '/admin-backup.html',
            '/admin/settings': '/admin-settings.html',
            '/admin-settings': '/admin-settings.html',
            '/farmer/dashboard': '/farmer-dashboard.html',
            '/farmer-dashboard': '/farmer-dashboard.html',
            '/customer/dashboard': '/farmer-dashboard.html',
            '/profile': '/farmer-profile.html',
            '/farmer/profile': '/farmer-profile.html',
            '/customer/profile': '/farmer-profile.html',
            '/farmer-profile': '/farmer-profile.html',
            '/orders': '/farmer-orders.html',
            '/farmer/orders': '/farmer-orders.html',
            '/customer/orders': '/farmer-orders.html',
            '/farmer-orders': '/farmer-orders.html',
            '/farmer/udhari': '/farmer-udhari.html',
            '/customer/udhari': '/farmer-udhari.html',
            '/farmer-udhari': '/farmer-udhari.html',
            '/farmer/pay': '/farmer-pay.html',
            '/customer/pay': '/farmer-pay.html',
            '/farmer-pay': '/farmer-pay.html',
            '/farmer/payments': '/farmer-payments.html',
            '/customer/payments': '/farmer-payments.html',
            '/farmer-payments': '/farmer-payments.html',
            '/farmer/notifications': '/farmer-notifications.html',
            '/customer/notifications': '/farmer-notifications.html',
            '/farmer-notifications': '/farmer-notifications.html'
        }

        if clean_path in route_map:
            self.path = route_map[clean_path] + query
        elif clean_path and not os.path.splitext(clean_path)[1]:
            rel_candidate = clean_path.lstrip('/') + '.html'
            if os.path.isfile(os.path.join(DIRECTORY, rel_candidate)):
                self.path = '/' + rel_candidate + query

        super().do_GET()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), CleanUrlHandler) as httpd:
        print(f"Local Server running at http://localhost:{PORT} (Proxying /api/ to {BACKEND_URL})")
        httpd.serve_forever()
