import os
from datetime import datetime
import pygame


class MickeyClock:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.center = (self.width // 2, self.height // 2 - 40)

        base_path = os.path.dirname(__file__)
        images_path = os.path.join(base_path, "images")

        self.clock_image = pygame.image.load(
            os.path.join(images_path, "clock.png")
        ).convert_alpha()

        self.left_hand = pygame.image.load(
            os.path.join(images_path, "left_hand.png")
        ).convert_alpha()

        self.right_hand = pygame.image.load(
            os.path.join(images_path, "right_hand.png")
        ).convert_alpha()

        self.mickey_image = pygame.image.load(
            os.path.join(images_path, "mickey.png")
        ).convert_alpha()

        self.clock_image = pygame.transform.smoothscale(self.clock_image, (520, 520))
        self.left_hand = pygame.transform.smoothscale(self.left_hand, (110, 110))
        self.right_hand = pygame.transform.smoothscale(self.right_hand, (130, 130))
        self.mickey_image = pygame.transform.smoothscale(self.mickey_image, (180, 220))

        self.minutes = 0
        self.seconds = 0

        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def update(self) -> None:
        now = datetime.now()
        self.minutes = now.minute
        self.seconds = now.second

    def draw_rotated_hand(
        self,
        image: pygame.Surface,
        angle: float,
        offset_length: int,
    ) -> None:
        rotated_image = pygame.transform.rotate(image, angle)

        offset = pygame.math.Vector2(0, -offset_length)
        rotated_offset = offset.rotate(-angle)

        hand_center = (
            self.center[0] + rotated_offset.x,
            self.center[1] + rotated_offset.y,
        )

        rect = rotated_image.get_rect(center=hand_center)
        self.screen.blit(rotated_image, rect)

    def draw(self) -> None:
        self.screen.fill((220, 220, 220))

        clock_rect = self.clock_image.get_rect(center=self.center)
        self.screen.blit(self.clock_image, clock_rect)

        # Left hand = seconds
        second_angle = -(self.seconds * 6)
        self.draw_rotated_hand(self.left_hand, second_angle, 35)

        # Right hand = minutes
        minute_angle = -(self.minutes * 6)
        self.draw_rotated_hand(self.right_hand, minute_angle, 42)

        mickey_rect = self.mickey_image.get_rect(
            center=(self.center[0], self.center[1] + 210)
        )
        self.screen.blit(self.mickey_image, mickey_rect)

        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 7)

        time_text = f"{self.minutes:02d}:{self.seconds:02d}"
        text_surface = self.font.render(time_text, True, (20, 20, 20))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height - 45))
        self.screen.blit(text_surface, text_rect)