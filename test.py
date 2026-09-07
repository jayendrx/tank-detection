from ultralytics import YOLO
import cv2


def main():
    # Load your trained model
    model = YOLO(r"runs\detect\train5\weights\best.pt")

    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Run YOLO on the webcam frame
        results = model(frame, conf=0.80)

        # Draw bounding boxes
        annotated_frame = results[0].plot()

        # Show the result
        cv2.imshow("Tank Detection", annotated_frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()