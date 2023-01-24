import sqlite3
import csv
import re

get_res = re.compile(r'(\d+x\d+)', re.IGNORECASE)
get_cpu_vendor = re.compile(r'(intel|amd|samsung)', re.IGNORECASE)
get_gpu_vendor = re.compile(r'(intel|amd|nvidia|arm)', re.IGNORECASE)
get_storage = re.compile(r'(\d+)(g|t)b', re.IGNORECASE)

db = sqlite3.connect('database')
with open('./backend/initialise.sqlite') as sql_source:
    db.executescript(sql_source.read())

with open('./backend/laptops.csv') as f:
    reader = csv.reader(f)
    print(','.join(next(reader)))
    all_rows = []
    for line in reader:
        this_row = []

        # manufacturer
        this_row.append(line[0])

        # model_name
        this_row.append(line[1])

        # category
        this_row.append(line[2].replace(' ', '-'))

        # screen_diag
        this_row.append(float(line[3].strip('"')))

        # screen_res
        maybe_screen_res = get_res.search(line[4])
        this_row.append(maybe_screen_res.group(0) if maybe_screen_res else '')

        # screen_type
        this_row.append(get_res.sub('', line[4]).strip())

        # screen_touch
        this_row.append('touch' if 'touch' in line[4].lower() else 'non-touch')

        # cpu_vendor
        maybe_cpu_vendor = get_cpu_vendor.search(line[5])
        this_row.append(maybe_cpu_vendor.group(0) if maybe_cpu_vendor else '')

        # cpu
        this_row.append(get_cpu_vendor.sub('', line[5]).strip())

        # ram
        this_row.append(int(line[6].strip('GB')))

        # storage
        drives = ((int(i[0]), i[1].lower())
                  for i in get_storage.findall(line[7]))
        total_storage_gb = sum(
            i[0] if i[1] == 'g' else i[0]*1024 for i in drives
        )
        this_row.append(total_storage_gb)

        # storage_type
        types = ['ssd' if 'ssd' in line[7].lower() else '',
                 'hdd' if 'hdd' in line[7].lower() else '',
                 'flash' if 'flash' in line[7].lower() else '']
        this_row.append(','.join(i for i in types if i) or 'none')

        # gpu_vendor
        maybe_gpu_vendor = get_gpu_vendor.search(line[8])
        this_row.append(maybe_gpu_vendor.group(0) if maybe_gpu_vendor else '')

        # gpu
        this_row.append(get_gpu_vendor.sub('', line[8]).strip())

        # os
        this_row.append(line[9].replace(' ','').lower().replace('os', 'OS'))

        # os version
        this_row.append(line[10])

        # mass
        this_row.append(float(line[11].strip('kgs')))

        # price
        this_row.append(round(87.89 * float(line[12].replace(',', '.')), 2))

        all_rows.append(this_row)
    db.executemany(
        'insert into laptop (manufacturer,model_name,category,screen_diag,screen_res,screen_type,screen_touch,cpu_vendor,cpu,ram,storage,storage_type,gpu_vendor,gpu,os,os_version,mass,price) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        all_rows
    )
    db.commit()
