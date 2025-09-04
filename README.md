# LiveManga

A comprehensive manga processing and live translation system that combines OCR, colorization, text detection, and translation capabilities for manga images.

## Features

- **Text Detection**: Advanced OCR and text detection using deep learning models
- **Colorization**: Automatic manga colorization with pre-trained models
- **Image Processing**: Denoising, upscaling, and enhancement utilities
- **Web Interface**: Django-based backend for processing and serving manga content
- **Mobile App**: Flutter frontend for mobile manga reading and processing
- **Database Integration**: SQLite database for storing manga data and metadata
- **API Endpoints**: RESTful API for manga processing operations

## Project Structure

- `livemanga/`: Django backend application
- `manga/`: Manga processing scripts and utilities
- `models/`: Pre-trained neural network models
- `networks/`: Network architectures and weights
- `utils/`: Utility functions for image processing, OCR, and more
- `denoising/`: Image denoising models and functions
- `html/`: Generated documentation
- `media/`: Processed manga images and assets

## Installation

### Prerequisites

- Python 3.8+
- Flutter SDK (for mobile app)
- Git

### Backend Setup

1. Clone the repository
2. Navigate to the project directory
3. Install Python dependencies:
   ```bash
   pip install django djangorestframework pillow opencv-python torch torchvision numpy
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Mobile App Setup

1. Ensure Flutter is installed
2. Navigate to the project directory
3. Install Flutter dependencies:
   ```bash
   flutter pub get
   ```
4. Run the app:
   ```bash
   flutter run
   ```

## Usage

1. Place manga images in the `inp/` directory
2. Run the processing pipeline:
   ```bash
   python launch.py
   ```
3. Access the web interface at `http://localhost:8000`
4. Use the mobile app for on-the-go processing

## Models and Networks

The project includes several pre-trained models:

- Text detection models in `models/yolov5/`
- Colorization models in `networks/`
- Denoising models in `denoising/models/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
