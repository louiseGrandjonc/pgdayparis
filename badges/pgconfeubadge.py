from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

import os


class PgdayParisBadge(object):
	def getsize(self):
		return (103*mm, 138*mm)

	def draw(self, base):
		reg = base.reg
		regtype = reg.regtype
		canvas = base.canv

		# Border
		canvas.rect(0,0,base.width,base.height)

		# Blue box with elephant
		base.setFill(33, 139, 181)
		canvas.rect(4*mm, base.ycoord(10, 28), base.width-(2*4*mm), 28*mm, stroke=0, fill=1)
		canvas.drawImage(base.pglogo_white_name,
						 8*mm, base.ycoord(12, 25),
						 25*mm, 25*mm,
						 mask='auto')

		# Conf info
		base.drawDynamicParagraph("PG day 2014\nParis, France",
								  35*mm, base.ycoord(12, 25),
								  base.width-(40*mm), 25*mm,
								  colors.white,
								  alignment=TA_CENTER)

		# Let's get the name info on there
		base.drawDynamicParagraph("%s %s" % (reg.firstname, reg.lastname),
								  8*mm, base.ycoord(50, 10),
								  base.width-(2*8*mm), 10*mm,
								  colors.black,
								  bold=True)
		# Company
		base.drawDynamicParagraph(reg.company,
								  8*mm, base.ycoord(60, 8),
								  base.width-(2*8*mm), 8*mm,
								  colors.black,
								  maxsize=14)

		# Type of attendee
		base.setFillTuple(regtype.regclass.colortuple())
		canvas.rect(4*mm, base.ycoord(90, 10), base.width - (2*4*mm), 10*mm, stroke=0, fill=1)

		base.drawDynamicParagraph(regtype.regclass.regclass,
								  4*mm, base.ycoord(90, 10),
								  base.width - (2*4*mm), 10*mm,
								  regtype.regclass.foregroundcolortuple() and regtype.regclass.foregroundcolortuple() or colors.black,
								  alignment=TA_CENTER)

		# Madrid logo
		canvas.drawImage("%s/../files/img/madrid_logo_simple.png" % os.path.dirname(__file__),
						 8*mm, base.ycoord(110, 20),
						 60,60,
						 mask='auto')

		# Set of boxes for lunch options
		boxsize = 40
		boxleft = (base.width-4*boxsize)-4*mm

		# Which days for lunch?
		options = reg.additionaloptions.all()

		days = ["Tue", "Wed", "Thu", "Fri"]
		# Access to general days?
		for n in range(4):
			access = False
			if n == 0:
				# Training day
				if len(options):
					# Has some training, but how much?
					if len(options) == 2 or options[0].id in (29, 34, 35):
						canvas.setFillColor(colors.green)
					else:
						# Has one option and it's not a full-day one
						canvas.setFillColor(colors.yellow)
					access = True
				else:
					canvas.setFillColor(colors.white)
			else:
				# General conference day access (we don't have any
				# single day entrances, so don't bother trying)
				if regtype.id in (88, 89, 90, 91, 96, 97, 98, 101):
					canvas.setFillColor(colors.green)
					access = True
				else:
					canvas.setFillColor(colors.white)

			canvas.rect(boxleft+n*boxsize, base.ycoord(90, boxsize),
						boxsize, boxsize, fill=1, stroke=1)
			base.drawDynamicParagraph(days[n],
									  boxleft+n*boxsize, base.ycoord(120, 6),
									  boxsize, 6*mm,
									  colors.black,
									  alignment=TA_CENTER)
			if not access:
				canvas.line(boxleft+n*boxsize, base.ycoord(90, boxsize),
							boxleft+n*boxsize+boxsize, base.ycoord(90, boxsize)+boxsize)
