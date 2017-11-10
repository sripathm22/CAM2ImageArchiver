'''
Copyright 2017 Purdue University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from camera import Camera, IPCamera, NonIPCamera, StreamFormat
from error import ClosedStreamError

class TestCamera(unittest.TestCase):
    def setUp(self):

        #Instantiate camera test fixtures
        self.cam = Camera(1, 1, 1)
        self.ip_cam = IPCamera(1, 1, 1, "127.1.1.1", "/test_image_path", "/test_mjpeg_path", "3000")

    def test_get_frame_no_parser(self):
        #Assert camera raises error when no parser is present
        self.assertRaises(ClosedStreamError, self.cam.get_frame)

    def test_open_stream_invalid_enum(self):
        #Assert exception raised with invalid enum
        self.assertRaises(ValueError, self.ip_cam.open_stream, "INVALID_ENUM_VAL")

    def test_get_url_invalid_enum(self):
        #Assert exception raised with invalid enum
        self.assertRaises(ValueError, self.ip_cam.get_url, "INVALID_ENUM_VAL")

    def test_get_url_mjpeg(self):
        #Assert url correctly created for mjpeg case
        result = self.ip_cam.get_url(StreamFormat.MJPEG)
        self.assertEquals(result, "http://127.1.1.1:3000/test_mjpeg_path")

    def test_get_url_image(self):
        #Assert url correctly created for image case
        result = self.ip_cam.get_url(StreamFormat.IMAGE)
        self.assertEquals(result, "http://127.1.1.1:3000/test_image_path")



if __name__ == '__main__':
    unittest.main()