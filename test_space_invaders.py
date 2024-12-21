import pytest
import pygame
from unittest.mock import MagicMock
from main import Laser, Ship, Player, Enemy, collide, HEIGHT

pygame.init()

@pytest.fixture
def dummy_laser_image():
    return pygame.Surface((5, 10))

@pytest.fixture
def dummy_ship_image():
    return pygame.Surface((50, 50))

@pytest.fixture
def player(dummy_ship_image, dummy_laser_image):
    player = Player(300, 630)
    player.ship_img = dummy_ship_image
    player.laser_img = dummy_laser_image
    return player

@pytest.fixture
def enemy(dummy_ship_image, dummy_laser_image):
    enemy = Enemy(100, 100, "red")
    enemy.ship_img = dummy_ship_image
    enemy.laser_img = dummy_laser_image
    return enemy

@pytest.fixture
def laser(dummy_laser_image):
    return Laser(100, 100, dummy_laser_image)

def test_laser_off_screen(laser):
    assert not laser.off_screen(HEIGHT)
    laser.y = -10
    assert laser.off_screen(HEIGHT)

def test_laser_collision(dummy_ship_image, laser):
    ship = Ship(100, 100)
    ship.ship_img = dummy_ship_image
    ship.mask = pygame.mask.from_surface(dummy_ship_image)
    assert laser.collision(ship)
    laser.x = 200
    assert not laser.collision(ship)

def test_ship_cooldown(player):
    player.cool_down_counter = 0 
    player.COOLDOWN = 10 
    player.cooldown()
    assert player.cool_down_counter == 1
    player.cooldown()
    assert player.cool_down_counter == 2

def test_ship_shoot(player):
    assert len(player.lasers) == 0
    player.shoot()
    assert len(player.lasers) == 1

def test_player_healthbar(player):
    mock_window = pygame.Surface((800, 600))  # Use a real surface
    player.healthbar(mock_window)

def test_enemy_move(enemy):
    initial_y = enemy.y
    enemy.move(5)
    assert enemy.y == initial_y + 5

def test_enemy_shoot(enemy):
    assert len(enemy.lasers) == 0
    enemy.shoot()
    assert len(enemy.lasers) == 1

def test_collide(dummy_ship_image):
    obj1 = Ship(100, 100)
    obj2 = Ship(120, 120)
    obj1.ship_img = dummy_ship_image
    obj2.ship_img = dummy_ship_image
    obj1.mask = pygame.mask.from_surface(dummy_ship_image)
    obj2.mask = pygame.mask.from_surface(dummy_ship_image)
    assert collide(obj1, obj2)
    obj2.x = 200
    assert not collide(obj1, obj2)

def test_laser_edge_case(dummy_laser_image):
    laser = Laser(0, HEIGHT, dummy_laser_image)
    assert not laser.off_screen(HEIGHT)
    laser.y = HEIGHT + 1
    assert laser.off_screen(HEIGHT)

@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    pygame.quit()