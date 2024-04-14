import os
from update_video_db import update_video_status


actual_dir = os.path.dirname(os.path.abspath(__file__))[0: len(os.path.dirname(os.path.abspath(__file__))) - 7]
base_dir = os.path.join(actual_dir, "VideosFpv")
editing_dir = os.path.join(actual_dir, "VideosFpv", "Editing")
processed_dir = os.path.join(actual_dir, "VideosFpv", "Processed")

def process_video(video_id, url_video):
    try:
        create_dirs()
        parts = url_video.split("/")
        video_filename = parts[-1]
        parts = video_filename.split(".mp4")
        name = parts[0]
        download_video(url_video, video_filename)
        # file_concat_path = create_file_conc(name, video_filename)
        # edit_video(video_filename, file_concat_path)
        # remove_file("Editing", name + ".txt")
        # remove_file("Editing", video_filename)
        # remove_file("Editing", "c_" + video_filename)
        # remove_file("Editing", "l_" + video_filename)
        # update_video_status(video_id, "processed")
    except OSError as e:
        print(f"Error: {e.strerror}")

def edit_video(video_filename, file_concat_path):
    file_path = os.path.join(editing_dir, video_filename)
    file_c = os.path.join(editing_dir, "c_" + video_filename)
    file_l = os.path.join(editing_dir, "l_" + video_filename)
    file_p = os.path.join(processed_dir, video_filename)    
    os.system('ffmpeg -f concat -safe 0 -i "' + file_concat_path + '" -c copy "' + file_c + '"')
    os.system('ffmpeg -ss 0 -t 20  -i "' + file_path + '" -c copy "' + file_l + '"')
    os.system('ffmpeg -i "' + file_l + '" -c copy -aspect 16/9 "' + file_p + '"')

def download_video(url_video, video_name):
    video_editing = os.path.join(editing_dir, video_name) 
    print(video_editing)
    os.system(f"curl -o {video_editing} {url_video}")
    
def create_file_conc(video_name, file_name):
    file_path = os.path.join(editing_dir, video_name + ".txt")
    content = "file logo.mp4\n" + "file " + file_name + "\n" + "file logo.mp4"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(content)
            file.close()
    return file_path

def remove_file(folder_name, filename):
    file = os.path.join(base_dir, folder_name, filename)
    if  os.path.exists(file):
        os.remove(file)

def create_dirs():
    if not os.path.exists(editing_dir):
        os.mkdir(editing_dir)
    if not os.path.exists(processed_dir):
        os.mkdir(processed_dir)