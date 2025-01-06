class DrawBoxes:
    def __init__(self, image):
        self.image = image
        self.drawing = False
        self.start_point = None
        self.end_point = None
        self.rectangles = []

    def start_drawing(self, event):
        self.drawing = True
        self.start_point = (event.x, event.y)

    def stop_drawing(self, event):
        self.drawing = False
        self.end_point = (event.x, event.y)
        self.rectangles.append((self.start_point, self.end_point))
        self.draw_rectangle()

    def draw_rectangle(self):
        # Logic to draw rectangle on the image
        pass

    def reset(self):
        self.rectangles = []
        self.start_point = None
        self.end_point = None

    def get_rectangles(self):
        return self.rectangles

    def update_image(self):
        # Logic to update the image with drawn rectangles
        pass
