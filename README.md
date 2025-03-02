# ytmusic-downloader
 you can download videos or playlist from youtube
### step1: open the termianal
```bash
C:\Users\user>git clone https://github.com/silavucan33/ytmusic-downloader
```
### step2: create a virtual environment (optional)
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
### step3: install dependencies
```bash
pip install django yt-dlp
```
### step4:
```bash
cd ytmusic_downloader/youtube_downloader
```

### step5:
```bash
python manage.py migrate
```
### step6: start your app
```bash
python manage.py runserver
```
### step 7: open your browser and go to
```bash
http://127.0.0.1:8000/
```
