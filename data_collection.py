import cv2
import mediapipe as mp
from datetime import datetime
import os

# Initialize MediaPipe modules
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Set the class name
class_name = "need"

# Define the output directory
output_directory = f"D:\sign to speak\Dataset\Data2\{class_name}"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# cap = cv2.VideoCapture(0)
# mobile cam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Initialize MediaPipe Face Mesh
with mp_face_mesh.FaceMesh() as face_mesh:
    # Initialize MediaPipe Hands
    with mp_hands.Hands() as hands:
        # Initialize MediaPipe Pose
        with mp_pose.Pose() as pose:
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            fps = 30  # Adjust as needed
            codec = cv2.VideoWriter_fourcc(*'XVID')

            out = None
            recording = False  # Flag to control recording

            while True:
                current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
                video_output_path = f"{output_directory}\{class_name}_asl_video_{current_time}.mp4"

                ret, frame = cap.read()
                if not ret:
                    break

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Process hand poses
                hand_results = hands.process(rgb_frame)
                if hand_results.multi_hand_landmarks:
                    for hand_landmarks in hand_results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Process body pose
                pose_results = pose.process(rgb_frame)
                if pose_results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                key = cv2.waitKey(1) & 0xFF

                # Start/Stop recording on 's' key
                if key == ord('s'):
                    if not recording:
                        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        video_output_path = f"{output_directory}/{class_name}_asl_video_{current_time}.mp4"
                        out = cv2.VideoWriter(video_output_path, codec, fps, (frame_width, frame_height))
                        recording = True
                        print("Recording started.")
                    else:
                        out.release()
                        recording = False
                        print(f"Recording stopped. Video saved as {video_output_path}")

                if recording:
                    # Write the frame to the video
                    out.write(frame)

                cv2.imshow('Output', frame)

                # Start a new recording on 'q' key
                if key == ord('q'):
                    if recording:
                        out.release()
                        recording = False
                        print(f"Recording stopped. Video saved as {video_output_path}")
                    break  # Break out of the while loop

            # Release VideoWriter resources after the loop
            if out is not None:
                out.release()
                
####check no of files----------------------------------------------------------###########
def count_files(directory_path):
    try:
        # Get the list of files in the directory
        files = os.listdir(directory_path)

        # Filter only files (not directories) and count them
        file_count = len([f for f in files if os.path.isfile(os.path.join(directory_path, f))])
        print("-----------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------")
        print(f"Total number of files in '{directory_path}': {file_count}")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_files(output_directory)
# Release resources after exiting the main loop
cap.release()
cv2.destroyAllWindows()





