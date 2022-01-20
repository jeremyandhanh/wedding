import hashlib

lines = []
with open('rsvp_codes.txt') as f:
    lines = f.readlines()

for line in lines:
    if len(line) >= 6:
        line = line.strip()
    line = hashlib.md5(line.encode('utf-8')).hexdigest()
    print(f'{line}')

print(hashlib.md5("O3BNXO".encode('utf-8')).hexdigest())