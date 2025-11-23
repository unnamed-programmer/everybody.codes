#!/usr/bin/env fish

for day in (seq -w 1 20)
mkdir $PWD/$day

for cf in 1code 2code 3code
echo "#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()" >> $PWD/$day/$cf.py
end

for nf in 1notes 2notes 3notes
touch $PWD/$day/$nf
end
end
