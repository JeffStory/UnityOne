import commands
import os
z = 1
while z == 1:
	os.chdir("Ubuntu One")
	x = commands.getoutput("ls -c|head -n1")
	y = "u1sdtool --publish-file %s" % x
	os.popen(y)
	b = commands.getoutput("u1sdtool --publish-file %s" % x)
	print b
	z = 0
