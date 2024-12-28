# Facial Recognition Attendance System

This project is a facial recognition-based attendance system built using Flask, OpenCV, and the `face_recognition` library.

## Project Structure

- `app.py`: The main Flask application file.
- `attendance/attendance.py`: Contains the function to mark attendance.
- `recognition/recognition.py`: Contains the function to recognize faces using the webcam.
- `requirements.txt`: Lists the dependencies required for the project.
- `templates/index.html`: The HTML template for the home page.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd facial_recognition_attendance
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

- The home page (`/`) provides a welcome message and instructions.
- The `/mark_attendance` endpoint is used to mark attendance using facial recognition.

## Dependencies

- Flask
- OpenCV (`opencv-python`)
- `face_recognition`

## License

This project is licensed under the MIT License.