# overcast-uploader
Command line tool to upload mp3 / m4a files to [Overcast Podcast App](https://overcast.fm).

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
#### Upload mp3 /m4a file
```
python overcast-uploader.py -f /path/to/file.mp3
python overcast-uploader.py -f /path/to/file.m4a
```

#### Upload all mp3 / m4a files from directory
```
python overcast-uploader.py -d /path/to/path/to/directory-with-audio-files
```

#### Upload mp3 / m4a file and delete it afterwards
```
python overcast-uploader.py -f /path/to/file.mp3 -c
python overcast-uploader.py -f /path/to/file.m4a -c
```

#### Upload all mp3 / m4a files from directory and delete them afterwards
```
python overcast-uploader.py -d /path/to/directory-with-audio-files -c
```

#### Upload mp3 / m4a file and provide Overcast credentials in program arguments
```
python overcast-uploader.py -f /path/to/file.mp3 -e abc@xyz.com -p password
python overcast-uploader.py -f /path/to/file.m4a -e abc@xyz.com -p password
```
