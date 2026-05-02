"""
YOLO Retail Inventory Tracker - Live Camera Module
Phase 1: Camera Feed Acquisition and Display

This module captures real-time video from the system's default webcam using OpenCV.
The captured frames are displayed in a window, allowing verification that the camera
hardware is working correctly and frame acquisition is functioning as expected.

Author: YOLO Retail Team
Date: May 2026
"""

import cv2
import sys


def initialize_camera(camera_index=0):
    """
    Initialize the webcam capture device.
    
    Args:
        camera_index (int): Index of the camera to use. Default is 0 (built-in camera).
    
    Returns:
        cv2.VideoCapture: The video capture object, or None if initialization fails.
    """
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print(f"Error: Could not open webcam at index {camera_index}.")
        print("Please verify that your camera is connected and not in use by another application.")
        return None
    
    # Set camera resolution for better performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    return cap


def display_camera_feed(cap):
    """
    Capture and display the live camera feed.
    
    The video feed will be displayed in a window until the user presses 'q' to quit.
    Each frame is displayed with the current frame count and FPS information.
    
    Args:
        cap (cv2.VideoCapture): The video capture object.
    
    Returns:
        bool: True if execution completed successfully, False otherwise.
    """
    frame_count = 0
    
    print("Starting live camera feed...")
    print("Press 'q' to quit the application.")
    print("-" * 50)
    
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        
        # Check if the frame was successfully captured
        if not ret:
            print("Error: Failed to grab frame from the camera.")
            print("The camera may have been disconnected or is in use by another application.")
            return False
        
        frame_count += 1
        
        # Add frame information to the display
        cv2.putText(
            frame,
            f"Frame: {frame_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
        
        # Display the current frame in a window
        cv2.imshow('YOLO Retail: Live Camera Feed Test', frame)
        
        # Check for user input (wait 1 millisecond per frame)
        # 0xFF & ord('q') ensures we capture the 'q' key press
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            print("\nUser pressed 'q'. Closing the application...")
            break
        elif key == ord('c'):
            # Allow user to capture a screenshot by pressing 'c'
            filename = f"camera_capture_{frame_count}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Screenshot saved as: {filename}")
    
    return True


def cleanup_resources(cap):
    """
    Release the camera and close all display windows.
    
    Args:
        cap (cv2.VideoCapture): The video capture object to release.
    """
    if cap is not None:
        cap.release()
    
    cv2.destroyAllWindows()
    print("Camera released and windows closed successfully.")


def main():
    """
    Main entry point for the camera test module.
    
    This function initializes the camera, displays the live feed, and handles
    cleanup of resources when the application exits.
    """
    print("=" * 50)
    print("YOLO Retail Inventory Tracker - Camera Module Test")
    print("=" * 50)
    
    # Initialize the camera
    cap = initialize_camera(camera_index=0)
    
    if cap is None:
        print("Fatal Error: Camera initialization failed.")
        sys.exit(1)
    
    try:
        # Display the camera feed
        success = display_camera_feed(cap)
        
        if not success:
            print("Error: An issue occurred while displaying the camera feed.")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nInterrupt signal received. Shutting down...")
    
    except Exception as e:
        print(f"Unexpected error occurred: {type(e).__name__}: {str(e)}")
        sys.exit(1)
    
    finally:
        # Ensure resources are cleaned up
        cleanup_resources(cap)
    
    print("=" * 50)
    print("Camera test completed successfully.")
    print("=" * 50)
    sys.exit(0)


if __name__ == "__main__":
    main()
