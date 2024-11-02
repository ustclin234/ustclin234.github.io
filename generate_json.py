# coding = utf-8
import json,os

def generate_json(file_folder, item='qsshouban', save_folder='./json_files/'):
    files = sorted([s for s in os.listdir(file_folder) if s.endswith('png')])
    contents = {
        "images": files
    }
    js = json.dumps(contents, sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    with open(f'{save_folder}{item}.json','w',newline='\n',encoding='utf-8') as file:
        file.write(js)

file_folders1 = './qsshouban/'
file_folders2 = './qsgupu/'
generate_json(file_folders1, 'qsshouban')
generate_json(file_folders2, 'qsgupu')