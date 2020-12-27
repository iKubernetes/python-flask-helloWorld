#!/usr/bin/env python
import unittest
import server

class TestHello(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\nWebSite: http://www.magedu.com\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\nWebSite: http://www.magedu.com\n')

    def test_hello_name(self):
        name = 'magedu'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

    def test_hello_agent(self):
        rv = self.app.get(f'/user-agent')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
