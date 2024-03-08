import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
dirs = {}
cur_path = '/'
dirs.setdefault(cur_path, {})
for line in lines[1:]:
  if '$ cd' == line[:4] and line[5:7] != '..':
    cur_path += line[5:].rstrip('\n')+'/'
    dirs.setdefault(cur_path, {})
  elif line[0].isnumeric():
    size, name = line.rstrip('\n').split(' ')
    dirs[cur_path][name] = int(size)
  elif line == '$ cd ..\n':
    cur_path = '/'.join(cur_path.split('/')[:-2]) + '/'
  # print(line, end="")
  # print(cur_path, "\n")
        
dir_sums = {key: sum(value.values()) for key, value in dirs.items()}

dir_sums_nested = {}
for path, dir_sum in dir_sums.items():
  child_dirs = {key: value for key, value in dir_sums.items() if key.startswith(path)}
  dir_sums_nested[path] = sum(child_dirs.values())
print(json.dumps(dir_sums_nested, indent=4, sort_keys=True))

dir_sums_at_most_100_000 = {key: value for key, value in dir_sums_nested.items() if value <= 100_000}

# part 2
total_avail_space = 70_000_000
available_space = total_avail_space - dir_sums_nested['/']
needed_space = 30_000_000 - available_space
print(needed_space)

sums_at_least_needed_space = [tuple((key, value)) for key, value in dir_sums_nested.items() if value >= needed_space]
sums_at_least_needed_space_sorted = sorted(sums_at_least_needed_space, key=lambda x: x[1])
print(sums_at_least_needed_space_sorted[0])
  