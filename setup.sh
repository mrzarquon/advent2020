#!/bin/bash

cd ~/src/advent2020

DATE=$1

echo "Making ${DATE} Skeleton"

mkdir ~/src/advent2020/$DATE

touch ~/src/advent2020/$DATE/{1_part.py,2_part.py,test.txt,input.txt,notes_1.txt,notes_2.txt}

cat << 'EOF' > ~/src/advent2020/$DATE/1_part.py
#!/usr/bin/env python3
import os
import sys
import re
import operator
from copy import deepcopy
from pprint import pprint

file_in = open(sys.argv[1],"r").readlines()

EOF

cat << 'EOF' > ~/src/advent2020/$DATE/2_part.py
#!/usr/bin/env python3
import os
import sys
import re
import operator
from copy import deepcopy
from pprint import pprint

file_in = open(sys.argv[1],"r").readlines()

EOF

chmod +x ~/src/advent2020/$DATE/*.py