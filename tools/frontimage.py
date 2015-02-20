#!/usr/bin/env python
#
# Output a template for "frontimages" for all files listed on the
# commandline (use with shell expansion, of course)


import os
import sys
from PIL import Image
import StringIO


if __name__=="__main__":
	s = StringIO.StringIO()
	
	for f in sys.argv[1:]:
		i = Image.open(f)
		(width, height) = i.size
		s.write("\t{'image': 'frontrotate/%s', 'width': %s, 'height': %s, 'title': ''},\n" % (os.path.basename(f), width, height))
		
	print s.getvalue()
