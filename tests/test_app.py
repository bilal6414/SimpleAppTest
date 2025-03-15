import unittest
import cv2
from app import get_version

class TestApp(unittest.TestCase):
    def test_get_version(self):
        # Ensure the version read from version.txt is '1.0.0' (initially)
        version = get_version()
        self.assertEqual(version, "1.0.0", "Initial version should be 1.0.0")

    def test_opencv_import(self):
        # Check that cv2 returns a version string
        cv_version = cv2.__version__
        self.assertTrue(isinstance(cv_version, str))
        self.assertNotEqual(cv_version, "")

if __name__ == "__main__":
    unittest.main()
