# test_runner.py
import unittest
import pygame
import sys
import os
from pygame import display

# Import the test cases
from tests import TestSpaceInvaders

def run_tests():
    """
    Set up the test environment and run all tests
    """
    # Initialize pygame for testing
    os.environ['SDL_VIDEODRIVER'] = 'dummy'  # Use dummy video driver for testing
    pygame.init()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases to suite
    suite.addTests(loader.loadTestsFromTestCase(TestSpaceInvaders))
    
    # Create a test runner with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run the tests
    result = runner.run(suite)
    
    # Clean up pygame
    pygame.quit()
    
    # Return the result status
    return result.wasSuccessful()

if __name__ == '__main__':
    # Set up file structure
    print("Setting up test environment...")
    
    # Ensure assets directory exists
    if not os.path.exists('assets'):
        os.makedirs('assets')
        print("Created assets directory")
    
    # Create dummy assets for testing if they don't exist
    asset_files = [
        "pixel_ship_red_small.png",
        "pixel_ship_green_small.png",
        "pixel_ship_blue_small.png",
        "pixel_ship_yellow.png",
        "pixel_laser_red.png",
        "pixel_laser_green.png",
        "pixel_laser_blue.png",
        "pixel_laser_yellow.png",
        "background-black.png"
    ]
    
    for asset in asset_files:
        asset_path = os.path.join("assets", asset)
        if not os.path.exists(asset_path):
            # Create a small dummy surface and save it
            surface = pygame.Surface((30, 30))
            pygame.image.save(surface, asset_path)
            print(f"Created dummy asset: {asset}")
    
    print("\nStarting tests...\n")
    
    # Run the tests
    success = run_tests()
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)