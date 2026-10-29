# LiveManga

A manga processing pipeline with a Django REST backend and a Flutter client. It takes raw manga pages and produces enhanced, colorized, readable-aloud versions.

## What it does

- **Panel splitting** of manga pages
- **Text detection and OCR** (YOLOv5-based detection, PaddleOCR)
- **Grammar correction** of recognised text (Gramformer)
- **Text-to-speech** with multiple voices (XTTS)
- **Colorization** of black-and-white pages
- **Upscaling** (BSRGAN) and denoising
- **REST API** (Django REST Framework) consumed by the Flutter app at the repository root

Translation is not implemented.

## Project structure

- `livemanga/` Django project and API
- `manga/` page-processing scripts
- `models/`, `networks/`, `denoising/` model code and weights locations
- `utils/` image and OCR helpers
- `launch.py` runs the processing pipeline
- `lib/` (and platform folders) Flutter app

## Setup

Prerequisites: Python 3.8+, a CUDA-capable GPU recommended, Flutter SDK for the app.

```bash
git clone https://github.com/a-3isa/livemanga
cd livemanga
pip install django djangorestframework pillow opencv-python torch torchvision numpy
# plus the OCR/TTS stack: paddleocr, TTS (XTTS), gramformer
python manage.py migrate
python manage.py runserver
```

Pre-trained model weights are required for detection, colorization, upscaling and TTS; place them in the directories above (they are not all included in the repository).

Run the pipeline: put pages in `inp/`, then

```bash
python launch.py
```

Flutter app:

```bash
flutter pub get
flutter run
```

Point the app at your backend URL. Do not rely on `public_url.txt`; it holds a stale tunnel address from development.

## License

MIT. See the LICENSE file.
