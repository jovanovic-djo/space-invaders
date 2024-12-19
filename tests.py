import unittest
import pygame
from main import Ship, Player, Enemy, Laser, collide

class TestSpaceInvaders(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((750, 750))
        
    def tearDown(self):
        pygame.quit()
        
    def test_ship_initialization(self):
        """Test basic ship initialization"""
        ship = Ship(100, 100)
        self.assertEqual(ship.x, 100)
        self.assertEqual(ship.y, 100)
        self.assertEqual(ship.health, 100)
        self.assertEqual(len(ship.lasers), 0)
        
    def test_player_initialization(self):
        """Test player specific initialization"""
        player = Player(100, 100, 150)
        self.assertEqual(player.health, 150)
        self.assertEqual(player.max_health, 150)
        self.assertIsNotNone(player.ship_img)
        self.assertIsNotNone(player.laser_img)
        
    def test_enemy_initialization(self):
        """Test enemy initialization with different colors"""
        colors = ["red", "green", "blue"]
        for color in colors:
            enemy = Enemy(100, 100, color)
            self.assertIsNotNone(enemy.ship_img)
            self.assertIsNotNone(enemy.laser_img)
            
    def test_laser_movement(self):
        """Test laser movement mechanics"""
        laser = Laser(100, 100, pygame.Surface((10, 10)))
        initial_y = laser.y
        laser.move(5)
        self.assertEqual(laser.y, initial_y + 5)
        
    def test_ship_cooldown(self):
        """Test ship shooting cooldown mechanism"""
        ship = Ship(100, 100)
        ship.cool_down_counter = 0
        ship.shoot()
        self.assertGreater(ship.cool_down_counter, 0)
        
    def test_player_health_reduction(self):
        """Test player health reduction mechanics"""
        player = Player(100, 100, 100)
        initial_health = player.health
        player.health -= 10
        self.assertEqual(player.health, initial_health - 10)
        
    def test_enemy_movement(self):
        """Test enemy movement mechanics"""
        enemy = Enemy(100, 100, "red")
        initial_y = enemy.y
        enemy.move(5)
        self.assertEqual(enemy.y, initial_y + 5)
        
    def test_collision_detection(self):
        """Test collision detection between objects"""
        player = Player(100, 100)
        enemy = Enemy(100, 100, "red")
        self.assertTrue(collide(player, enemy))
        enemy = Enemy(500, 500, "red")  # Far away position
        self.assertFalse(collide(player, enemy))
        
    def test_laser_off_screen(self):
        """Test laser off screen detection"""
        laser = Laser(100, -10, pygame.Surface((10, 10)))
        self.assertTrue(laser.off_screen(750))
        laser = Laser(100, 100, pygame.Surface((10, 10)))
        self.assertFalse(laser.off_screen(750))
        
    def test_player_boundaries(self):
        """Test player movement boundaries"""
        player = Player(0, 0)
        initial_x = player.x
        # Simulate moving left at boundary
        player.x -= 5
        self.assertEqual(player.x, initial_x)
        
if __name__ == '__main__':
    unittest.main()