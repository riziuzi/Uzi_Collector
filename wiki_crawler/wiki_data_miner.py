from collections import deque
import json
import os
import requests
import urllib.parse
import validators
from bs4 import BeautifulSoup
import time as time_lib
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pickle
import atexit
import signal


# Function to load the data (list and queue) from a file
def load_data(file_path = "queue_list.pickle"):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        my_queue = deque(data['queue'])
        my_list = data['list']
        my_checked = data['checked']
        batch_count = data['batch_count']
        time_max = data['time_max']
        print("Data loaded successfully.")
        return my_queue, my_list, my_checked, batch_count, time_max
    except FileNotFoundError:
        print("No saved data found.")
        return deque(), [], [], 0, 0

def get_directory_size(directory):
    total_size = 0
    for entry in os.scandir(directory):
        if entry.is_file():
            total_size += entry.stat().st_size
        elif entry.is_dir():
            total_size += get_directory_size(entry.path)
    return total_size



directory = r"D:\deep_data\wiki_technicalTermLabeledData"
if not os.path.exists(directory):         # Ensures to make directory
    os.makedirs(directory)


queue_file_path = "queue_list.pickle"
q, data, checked, batch_count, time_max = load_data(queue_file_path)
if(len(q) == 0):
  parent_url = "https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences"
  q.append((parent_url,0))

def save_data():
    data = {
        'queue': list(q),
        'list': data,
        'checked': checked,
        'batch_count': batch_count,
        'time_max': time_max
    }
    with open(queue_file_path, 'wb') as file:
        pickle.dump(data, file)
    print("Data saved successfully.")

disk_space = 400
batch_size = 200
empty_dict=0
set_depth = 3
base_url="https://en.wikipedia.org"
# parent_url = "https://geoltime.github.io/?Ma=470"
cite_note = "#"
repeated=[]
excpt = []
cooling_time = 30
compression = "snappy"
time=0

count1 = count2 = count3 = count4 = 0
total_directory_size = 0

atexit.register(save_data)

def interrupt_handler(signal, frame):
    save_data()
    exit(0)

signal.signal(signal.SIGINT, interrupt_handler)

while(len(q) and total_directory_size < disk_space * 1024 * 1024 * 1024):
    front = q.popleft()                     # Basic BFS settings
    url = front[0]
    time = front[1]
    time_max = max(time_max, time)
    
    if(time_max>set_depth):
      q.appendleft((front,time))
      break
    
    try:
      response = requests.get(url)
    except:
      try:
        response = requests.get("https://www.google.com/")
        continue
      except:
        q.appendleft((url,time))
        print("sleeping for :",cooling_time,"url:",url)
        time_lib.sleep(cooling_time)
        continue
      
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    print(url,len(paragraphs),time)
    count1+=1
    for j in range(len(paragraphs)):              # Inserting new links (according to given depth) to queue (BFS fashion)
      count2+=1
      if len(paragraphs[j].find_all("a"))!=0:
        list2=[]
        for i in paragraphs[j].find_all("a"):
          try:
            count3+=1
            if i.get("href") not in checked and validators.url(i.get("href")) and cite_note not in i.get("href"):
              checked.append(i.get("href"))
              count4+=1
              q.append((i.get("href"),time+1))
            elif base_url+i.get("href") not in checked and validators.url(base_url+i.get("href")) and cite_note not in i.get("href"):
              checked.append(base_url+i.get("href"))
              count4+=1
              q.append((base_url+i.get("href"),time+1))
            else:
              repeated.append(url)
              count4+=0
          except Exception:
            excpt.append([url])
            print("cought exception for ",url,i)

    texts = []
    labels = []
    count = 0
    for paragraph in paragraphs:          # Extrcating labeled and unlabeled data
      text = paragraph.get_text()
      texts.append(text)
      links = paragraph.find_all("a")
      label = [link.get_text() for link in links]
      labels.append(label)
      count+=1

    dict1 = {}                            
    for i in range(count):
      dict1[texts[i]] = labels[i]
    if(len(dict1)>0):
      data.append({url:dict1})
    else:
      print(url, ": dictionary found empty")
      empty_dict+=1
      continue
    print(f"url:{len(data)}  batch:{batch_count+1}")
    
    if len(data) >= batch_size:
        df = pd.DataFrame(data)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, os.path.join(directory, f"{batch_count}.parquet"),compression=compression)
        data = []
        batch_count += 1
    
    total_directory_size = get_directory_size(directory)

# Remaining data in last
if data:
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, os.path.join(directory, f"{batch_count}.parquet"),compression=compression)


deque_list = list(q)      # Save the list to a JSON file
if(os.path.isfile(os.path.join(directory,"deque_data.json"))):                    # Saving
  with open(os.path.join(directory,"deque_data.json"),"r") as file:
    dataD = json.load(file)
  dataD.append(deque_list)
  with open(os.path.join(directory,"deque_data.json"),"w") as file:
    json.dump(dataD, file)
        
else:
  with open(os.path.join(directory,str(time)+".json"),"w") as file:
    json.dump(deque_list, file)