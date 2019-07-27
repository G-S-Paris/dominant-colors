from   logging import Logger
import mock 
import unittest
from   src.demo import outputName

class TestDominantColors(unittest.TestCase):

    def test_example( self ):
        x = 2
        self.assertEqual( x+2, 4 )

    def test_outputName( self ):
        with mock.patch( "os.listdir", return_value = ['nut.png'] ):
            path = "nut.png"
            expected = "nut-output-0.png"
            observed = outputName(path)
            self.assertEqual(expected, observed)

        with mock.patch( "os.listdir", return_value = ['nut.png', 'nut-output-0.png'] ):
            expected1 = "nut-output-1.png"
            observed = outputName(expected)
            self.assertEqual( expected1, observed )
