#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint as rand
if __name__ == '__main__':
	from twisted.web import server, resource
	from twisted.internet import reactor


class bild(object):
	def __init__(self):
		self.inter = ["Endlich", "Skandal", "Panik", "Unglaublich", "Horror", "Schrecklich",
						"Schock", "Grauenvoll", "Schon wieder"]
		self.pre = ["Ex", "Ober", "Hitler", "Ausländer", "Jugend", "Kirchen", "Bayern",
				"Fußball", "Islamisten", "Amerika", "Meister", "Politiker", "Horror", "Panik", "Todes",
				"Hass", "UFO", "Monster", "Katholiken", "Knast", "Zuknunfts", "China", "Nazi"]
		self.nomen = ["Frau", "Papst", "Bibel", "Kanzler", "Obama", "Party", "Poldi", "Hitler",
				"Sex", "Moslem", "Bauer", "Erfinder", "Minister", "Superstar", "Deutschland", 
				"Verona", "Bohlen", "Merkel", "Wurst", "Priester", "Ausland", "Europa", "Döner", "Klinsi",
				"Killer", "Verbrecher", "Nazi", "Chaot", "Guru", "Ausländer", "Politiker"]
		self.verben = ["schlägt", "rettet", "kauft", "klaut", "isst", "verlässt", "will", "hasst",
				"predigt", "befreit", "erschießt", "erfindet", "heiratet", "verbrennt", "kauft",
				"verbietet", "verkauft", "findet", "zerstört", "verkündet", "verspricht"]
		self.nomen_ende = ["Bayern", "Döner", "Bahn", "Fußball", "RTL", "Dschungel", "Krieg",
				"Sicherheit", "Bananen"]
		self.nomen_ende.extend(self.nomen)
	def gib(self):
		t = []
		while True:
			t.append("<b>" + self.inter[rand(0,len(self.inter) - 1)] + ":</b> ")
			t.append(self.pre[rand(0,len(self.pre) - 1)] + "-")
			t.append(self.nomen[rand(0,len(self.nomen) - 1)] + " ")
			t.append(self.verben[rand(0,len(self.verben) - 1)] + " ")
			t.append(self.nomen_ende[rand(0,len(self.nomen_ende) - 1)])
			if t[4] not in t[2] and t[2] not in t[1]:
				break
			else:
				t = []
		return t[0] + t[1] + t[2] + t[3] + t[4]
		
	def max(self):
		return len(self.pre) * len(self.inter) * len(self.nomen) * len(self.verben) * len(self.nomen_ende)

if __name__ == '__main__':	
	class Simple(resource.Resource):
	    isLeaf = True
	    def __init__(self):
			resource.Resource.__init__(self)
			self.bild = bild()
			self.html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>BIDL informiert</title>
</head>
<body>
<center>
<h1> Aktuell: </h1>
		{0}	
		<br>
		<br> 
		<a href="javascript:this.location.reload();">refresh</a> - 
		<a href="http://github.com/janboe/schlagzeilen/blob/master/schlagzeilen.py">source</a>
		<p>	<a href="http://www.validome.org/referer">
			<img style="border:none"
				 src="http://www.validome.org/images/set5/valid_html_4_0_1.gif"
				 alt="Valid HTML 4.01" width="80" height="15">
			</a>
		</p>
		<br>
		<span style="font-size:60%"><i> Mögliche Schlagzeilen: {1}</i>
		</span>
		<br>
		</center>
</body>
</html>
			""".format("{0}", str(self.bild.max()))
	    def render_GET(self, request):
	        return self.html.format(self.bild.gib())

if __name__ == '__main__':
	site = server.Site(Simple())
	reactor.listenTCP(8080, site)
	reactor.run()
