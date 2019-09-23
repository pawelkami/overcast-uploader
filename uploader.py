import requests
import bs4 as bs
import argparse
import glob, os
import threading
import datetime

def send_file_to_overcast(filename, login, password):
    with open(filename, 'rb') as f:
        file_body = f.read()

    print("Sending: " + filename + " Size: " + str(len(file_body)) + " bytes")
    r = requests.Session()

    payload = {'email': login, 'password': password}
    r.post('https://overcast.fm/login', data=payload)
    data = r.get('https://overcast.fm/uploads').text

    soup = bs.BeautifulSoup(data, "html.parser")
    supa = soup.find('form', attrs={'id': 'upload_form'})

    action = supa.get('action')
    data_key_prefix = supa.get('data-key-prefix')

    bucket = supa.find('input', attrs={'name': 'bucket'}).get('value')
    key = supa.find('input', attrs={'name': 'key'}).get('value')
    aws_access_key_id = supa.find('input', attrs={'name': 'AWSAccessKeyId'}).get('value')
    acl = supa.find('input', attrs={'name': 'acl'}).get('value')
    upload_policy = supa.find('input', attrs={'name': 'policy'}).get('value')
    upload_signature = supa.find('input', attrs={'name': 'signature'}).get('value')
    upload_ctype = supa.find('input', attrs={'name': 'Content-Type'}).get('value')

    data_key_prefix += filename


    form_params = {
        "bucket": (None, bucket),
        "key": (None, key),
        "AWSAccessKeyId": (None, aws_access_key_id),
        "acl": (None, acl),
        "policy": (None, upload_policy),
        "signature": (None, upload_signature),
        "Content-Type": (None, upload_ctype),
        "file": (filename, file_body)
    }

    r.post(action, files=form_params)

    r.post('https://overcast.fm/podcasts/upload_succeeded', data={"key": data_key_prefix})

    print(filename + " has been sent")


def send_directory_to_overcast(dirpath, login, password):
    os.chdir(dirpath)
    threads = []
    for filename in glob.glob("*"):
        if not filename.endswith("mp3"):
            continue

        t = threading.Thread(target=send_file_to_overcast, args=(filename, login, password))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help="Directory with files to upload.", required=True)
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(args.dir + " is not a valid path")
        exit(1)

    login = input("Email:")
    password = input("Password:")

    begin_time = datetime.datetime.now()
    send_directory_to_overcast(args.dir, login, password)
    end_time = datetime.datetime.now()

    print("Begin time: " + str(begin_time))
    print("End time: " + str(end_time))
