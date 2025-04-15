import cv2
import numpy as np

# Create a blank canvas
canvas = np.ones((600, 1000, 3), dtype=np.uint8) * 255

# Button positions and colors
buttons = {
    'CLEAR': ((10, 10), (110, 60), (0, 0, 0)),
    'BLUE': ((120, 10), (220, 60), (255, 0, 0)),
    'GREEN': ((230, 10), (330, 60), (0, 255, 0)),
    'RED': ((340, 10), (440, 60), (0, 0, 255)),
    'YELLOW': ((450, 10), (550, 60), (0, 255, 255))
}

shapes = {
    'RECT': ((20, 80), (80, 140)),
    'CIRCLE': ((20, 150), (80, 210)),
    'LINE': ((20, 220), (80, 280)),
    'TRIANGLE': ((20, 290), (80, 350))
}

def draw_ui():
    # Draw color buttons
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        cv2.rectangle(canvas, (x1, y1), (x2, y2), color, 3)
        cv2.putText(canvas, label, (x1 + 10, y1 + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Draw tool shapes
    for i, (label, ((x1, y1), (x2, y2))) in enumerate(shapes.items()):
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (150, 150, 150), 1)
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        if label == 'RECT':
            cv2.rectangle(canvas, (x1 + 10, y1 + 10), (x2 - 10, y2 - 10), (100, 100, 100), 1)
        elif label == 'CIRCLE':
            cv2.circle(canvas, (center_x, center_y), 20, (0, 200, 0), 1)
        elif label == 'LINE':
            cv2.line(canvas, (x1 + 10, y2 - 10), (x2 - 10, y1 + 10), (200, 100, 100), 1)
        elif label == 'TRIANGLE':
            pts = np.array([[center_x, y1 + 10], [x1 + 10, y2 - 10], [x2 - 10, y2 - 10]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(canvas, [pts], True, (150, 0, 150), 1)

    # Draw drawing area
    cv2.rectangle(canvas, (150, 80), (980, 580), (180, 180, 180), 2)

draw_ui()

while True:
    cv2.imshow("AI Virtual Painter", canvas)
    key = cv2.waitKey(1)
    if key == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
