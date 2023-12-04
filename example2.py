import os
source_dir = 'E:\ezeba\Descargas'

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)