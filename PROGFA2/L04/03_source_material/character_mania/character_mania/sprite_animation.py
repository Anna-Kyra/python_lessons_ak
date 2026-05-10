from dae_progfa_lib.progfa_image import ProgfaImage

class SpriteAnimation:
    """
    This can be used to create a walking animation using a sprite sheet.
    Each row in the sprite sheet is considered to be a different direction (for example left, right, up, down).
    Each row should consist of 4 columns to build the animation. This can be changed by setting max_cols attribute value.
    """

    def __init__(self, sprite_sheet: ProgfaImage, col: int = 1, row: int = 0, frame_time = 8):
        """
        Creates an instance of Sprite4x4
        :param sprite_sheet: the image / sprite sheet, must be a 4 x 4, each row is a different direction
        :param col: optional, start column in the sprite sheet
        :param row: optional, start row in the sprite sheet
        :param frame_time: how many frames must one part of the sprite sheet be displayed before going to the next?
        """
        self.sprite_sheet = sprite_sheet
        self.row = row
        self.col = col
        self.max_cols = 4   # number of frames (columns) in one row to build the animation
        self.frame_time = frame_time
        self.accu_frames = 0

    def walk(self):
        """Animates by changing to the next frame (col) in the current row."""
        self.accu_frames += 1
        if self.accu_frames % self.frame_time == 0:
            self.col += 1
            if self.col >= self.max_cols:
                self.col = 0

    def display(self, x: float, y: float):
        """
        Displays the corrent frame (based on row and col) in the requested position.
        Position is depending on the current shape mode of your engine.
        :param x: left or center x position, based on your current shape mode
        :param y: bottom or center y position, based on your current shape mode
        """
        frame_w = self.get_width()
        frame_h = self.get_height()
        frame_rect = (self.col * frame_w,
                      self.row * frame_h,
                      frame_w,
                      frame_h)
        self.sprite_sheet.draw_partial(x, y, frame_rect)

    def get_width(self) -> float:
        """returns the width of one frame in the sprite sheet."""
        return self.sprite_sheet.width / self.max_cols

    def get_height(self) -> float:
        """Returns the height of one frame in the sprite sheet."""
        return self.sprite_sheet.height / self.max_cols