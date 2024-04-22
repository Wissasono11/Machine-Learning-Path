import unittest

class TestStringMethods(unittest.TestCase):
    # test case-1
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # test case-2
    def test_isalnum(self):
        self.assertTrue('c0ding'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    # test case-3
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')

if __name__ == '__main__':
    #Test Runner
    unittest.main()

print("=== test case yang lebih sederhana ===")

import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username): # using db sample
        self.username = username
    
    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    # Test Case-1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "Dicoding")
        self.assertFalse(dicoding.aktif) # tidak aktif secara default
        putus_koneksi_db(db)
    
    # Test Case-2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "Dicoding")
        dicoding.set_aktif()
        self.assertTrue(dicoding.aktif) # tidak aktif secara default
        putus_koneksi_db(db)

if __name__ =="__main__":
    # Test Runner
    unittest.main()

print("=== menggunakan metode setUp() dan tearDown() ===")
"""
setUp -> mempersiapkan pengujian. dipanggil untuk menyiapkan tes sehingga pemanggilannya
         akan dilakukan tiap sebelum metode tes dilaksanakan
tearDown -> dipanggil setiap metode tes selesai dilaksanakan dan bertindak untuk membersihkan
            meskipun terjadi kesalahan (exception) pada proses tes
"""
# Test Fixture
def setUp(self):
    self.db = koneksi_ke_db()
    self.coding = User(self.db, "dicoding")

def tearDown(self):
    putus_koneksi_db(self.db)
 
# Test Case-1
def test_user_default_not_active(self):
    self.assertFalse(self.dicoding.aktif) #tidak aktif secara default

#Test Case-2
def test_user_is_active(self):
    self.dicoding.set_aktif() #aktifkan user baru
    self.assertTrue(self.dicoding.aktif)