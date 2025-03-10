import os
import requests
#import stat

VIDEOS_FOLDER = 'videos'

#Functions for handling content additions and removals.

def handle_add_message(link: str, title: str):
    try:
        filename = os.path.basename(link)
        filepath = os.path.join(VIDEOS_FOLDER, filename)
        if not os.path.exists(filepath):
            response = requests.get(link, stream=True)
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        file.flush()
                #file.write(response.content)
            #os.chmod(filepath, stat.S_IRWXO)
            print(f"Downloaded {filename} from {link}")
        else:
            print(f"{filename} already exists locally.")
    except:
        print("Exception.")

def handle_remove_message(filename: str):
    try:
        filepath = os.path.join(VIDEOS_FOLDER, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Removed {filename}")
        else:
            print(f"{filename} not found locally.")
    except:
        print("Exception.")
