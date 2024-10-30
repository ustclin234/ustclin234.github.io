# coding = utf-8
import json,os

def generate_json(file_folder, save_folder='./json_files/'):
    files = sorted([s for s in os.listdir(file_folder) if s.endswith('png')])
    contents = {
        "images": files
    }
    js = json.dumps(contents, sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    with open(f'{save_folder}qsshouban.json','w',newline='\n',encoding='utf-8') as file:
        file.write(js)

file_folders = './qsshouban/'
generate_json(file_folders)