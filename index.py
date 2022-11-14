import cv2

#open webcam
cap = cv2.VideoCapture(0)

def visionTargetCoord(image):
    coordinates = []  # red square coordinates
    red_color = [0, 0, 255]
    last_x_red, last_y_red = 0, 0  # store the last x and y red positions
    rows, cols, _ = image.shape
    print(rows,cols)
    for x in range(rows):
        for y in range(cols):
            px = list(image[x, y])
            if px == red_color:
                # find the first coordinate of the red square (top left corner)
                if len(coordinates) == 0:
                    coordinates.append((y, x))  # top left corner of the red square
                    print("true")

                last_x_red, last_y_red = x, y # continuously update untill bottom right of the red square

    coordinates.append((last_y_red, last_x_red)) # add the bottom right coordinates to array

    # identify four point pixel coordinates
    top_left = coordinates[0]  # (x1, y1)
    bottom_left = (coordinates[0][0], coordinates[1][1])  # (x1, y2)
    top_right = (coordinates[1][0], coordinates[0][1])  # (x2, y1)
    bottom_right = coordinates[1]

    # Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
    # Draw a 10 px red rectangle around the green rectangle and save the image.
    # We only need the top left and bottom right corner to draw it
    cv2.rectangle(image, coordinates[0], coordinates[len(coordinates) - 1], (0, 255, 0), 10)
    cv2.imwrite('square_detected.jpg', image)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    # reduce webcam size by 2
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # display webcam
    #cv2.imshow('Input', frame)
    visionTargetCoord(frame)

    # end stream when esc is pressed
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

