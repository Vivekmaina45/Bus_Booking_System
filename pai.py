import cv2
import numpy as np
import mediapipe as mp

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Canvas to draw on
canvas = np.ones((600, 1000, 3), np.uint8) * 255

# Default color
draw_color = (0, 0, 255)

# Buttons (Color + Clear)
buttons = {
    'CLEAR': ((10, 10), (110, 60), (0, 0, 0)),
    'BLUE': ((120, 10), (220, 60), (255, 0, 0)),
    'GREEN': ((230, 10), (330, 60), (0, 255, 0)),
    'RED': ((340, 10), (440, 60), (0, 0, 255)),
    'YELLOW': ((450, 10), (550, 60), (0, 255, 255))
}

# Draw buttons
def draw_buttons(frame):
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        cv2.putText(frame, label, (x1 + 10, y1 + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

# Initialize webcam
cap = cv2.VideoCapture(0)
prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    draw_buttons(frame)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)
            h, w, _ = frame.shape
            lm_list = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmark.landmark]
            x1, y1 = lm_list[8]  # Index finger tip

            # Check for button interaction
            for label, ((x1b, y1b), (x2b, y2b), color) in buttons.items():
                if x1b < x1 < x2b and y1b < y1 < y2b:
                    if label == 'CLEAR':
                        canvas[:, :] = 255
                    else:
                        draw_color = color
                    prev_x, prev_y = 0, 0

            # Drawing area
            if y1 > 80:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x1, y1
                cv2.line(canvas, (prev_x, prev_y), (x1, y1), draw_color, 5)
                prev_x, prev_y = x1, y1
    else:
        prev_x, prev_y = 0, 0

    # Merge canvas with webcam
    frame[80:680, 0:1000] = cv2.addWeighted(frame[80:680, 0:1000], 0.5, canvas[80:680, 0:1000], 0.5, 0)
    cv2.imshow("AI Virtual Painter", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
