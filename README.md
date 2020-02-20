# overcast-uploader
Command line tool to upload mp3 files to [Overcast Podcast App](https://overcast.fm).

## Requirements
* Python 3
* Overcast Premium Account

## Installing dependencies
```
pip install -r requirements.txt
```

## Usage

```
usage: overcast-uploader.py [-h] [-e EMAIL] [-p PASSWORD] [-c]
                            (-d DIR | -f FILE)

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        E-mail used to login to Overcast.
  -p PASSWORD, --password PASSWORD
                        Password to Overcast account.
  -c, --clean           Remove file after upload.
  -d DIR, --dir DIR     Directory with files to upload.
  -f FILE, --file FILE  File to upload.
```

### Examples of usage
#### Upload mp3 file
```
python overcast-uploader.py -f /path/to/file.mp3
```

#### Upload all mp3 files from directory
```
python overcast-uploader.py -d /path/to/path/to/directory-with-mp3-files
```

#### Upload mp3 file and delete it afterwards
```
python overcast-uploader.py -f /path/to/file.mp3 -c
```

#### Upload all mp3 files from directory and delete them afterwards
```
python overcast-uploader.py -d /path/to/directory-with-mp3-files -c
```

#### Upload mp3 file and provide Overcast credentials in program arguments
```
python overcast-uploader.py -f /path/to/file.mp3 -e abc@xyz.com -p password
```
