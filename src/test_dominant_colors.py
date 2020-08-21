#!/usr/local/bin/python3
""" No docs on how to run tests?  """

from   logging import Logger
import mock 
import unittest
from   src.dominant_colors import outputPath

class TestDominantColors(unittest.TestCase):

    def test_example( self ):
        x = 2
        print("rent is too damn high")
        self.assertEqual( x+2, 4 )
    
    def test_example3( self ):
        x = 4
        print("rent is too damn high")
        self.assertEqual( x+2, 6 )



    ## don't wanna do this rn (I mean I should tho ;) )
    # def test_outputPath( self ):
    #     now = 
    #     path = "/an/example/path.png"
        

    # def test_outputName( self ):
    #     with mock.patch( "os.listdir", return_value = ['nut.png'] ):
    #         path = "nut.png"
    #         expected = "nut-output-0.png"
    #         observed = outputName(path)
    #         self.assertEqual(expected, observed)

    #     with mock.patch( "ols.listdir", return_value = ['nut.png', 'nut-output-0.png'] ):
    #         expected1 = "nut-output-1.png"
    #         observed = outputName(expected)
    #         self.assertEqual( expected1, observed )
