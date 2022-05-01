import cv2
from cvzone.HandTrackingModule import HandDetector


# Buttons Class
class Buttons:
    def __init__(self, position, width, height, value):
        self.position = position
        self.width = width
        self.height = height
        self.value = value

    def draw(self, frame):
        cv2.rectangle(frame, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (220, 220, 220), cv2.FILLED)
        cv2.rectangle(frame, self.position, (self.position[0] + self.width, self.position[1] + self.height), (0, 0, 0),
                      3)
        cv2.putText(frame, self.value, (self.position[0] + 40, self.position[1] + 63), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (50, 50, 50), 2)

    def click(self, x, y):
        if self.position[0] < x < self.position[0] + self.width and self.position[1] < y < self.position[
            1] + self.height:
            cv2.rectangle(frame, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, self.value, (self.position[0] + 30, self.position[1] + 68), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (50, 50, 50), 2)

            return True
        else:
            return False


# Webcam and initialisation
cap = cv2.VideoCapture(0)
cap.set(3, 2380)  # Width
cap.set(4, 2000)  # Length
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150
        buttonList.append(Buttons((xpos, ypos), 100, 100, buttonListValues[y][x]))

# Variables
myEquation = ''
delayCounter = 0

while True:
    # Get image from webcam
    result, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Detect hand
    hands, frame = detector.findHands(frame, flipType=False)

    # Draw all buttons
    cv2.rectangle(frame, (800, 90), (800 + 400, 70 + 100), (220, 220, 220), cv2.FILLED)
    cv2.rectangle(frame, (800, 90), (800 + 400, 70 + 100), (0, 0, 0), 3)

    for button in buttonList:
        button.draw(frame)

        # Check for hand
        if hands:
            lmList = hands[0]['lmList']
            length, _, frame = detector.findDistance(lmList[8], lmList[12], frame)
            x, y = lmList[8]

            if length < 55:
                for i, button in enumerate(buttonList):
                    if button.click(x, y) and delayCounter ==0:
                        myValue = buttonListValues[int(i % 4)][int(i / 4)]
                        if myValue == '=':
                            myEquation = str(eval(myEquation))
                        else:
                            myEquation += myValue
                        delayCounter = 1

    # Remove repetition of values
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Display the equation/result
    cv2.putText(frame, myEquation, (810, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)

    cv2.imshow('Img', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
