import unittest
from instock import checkStock

class TestParse( unittest.TestCase ):
    def testItemsNotInStock( self ):
        f = open( 'Rogue US-MIL Spec Bumper _ Rogue Fitness.htm', 'r' )
        page = f.read()
        f.close()

        itemsToCheck = { '25LB Rogue US-MIL Spec Bumper Pair' : False }
        checkStock( page, itemsToCheck )
        self.assertTrue( not any( itemsToCheck.values() ) )

    def testItemsInStock( self ):
        f = open( 'Rogue US-MIL Spec Bumper _ Rogue Fitness.htm', 'r' )
        page = f.read()
        f.close()

        itemsToCheck = { '45LB Rogue US-MIL Spec Bumper Pair' : False }
        checkStock( page, itemsToCheck )

        self.assertTrue( all( itemsToCheck.values() ) )

if __name__ == '__main__':
    unittest.main()