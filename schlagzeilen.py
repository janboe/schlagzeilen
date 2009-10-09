#!/usr/bin/python
# *--coding: utf-8 --*
from random import randint as rand
from twisted.web import server, resource
from twisted.internet import reactor


class bild(object):
	def __init__(self):
		self.inter = ["Endlich", "Skandal", "Panik", "Unglaublich", "Horror", "Schrecklich"]
		self.pre = ["Ex", "Ober", "Hitler", "Ausländer", "Jugend", "Kirchen", "Bayern",
				"Fußball", "Islamisten", "Amerika", "Meister", "Politiker", "Horror", "Panik", "Todes"]
		self.nomen = ["Frau", "Papst", "Bibel", "Kanzler", "Obama", "Party", "Poldi", "Hitler",
				"Sex", "Moslem", "Bauer", "Erfinder", "Minister", "Superstar", "Deutschland", 
				"Verona", "Bohlen", "Merkel", "Wurst", "Priester", "Ausland", "Europa", "Döner", "Klinsi"]
		self.verben = ["schlägt", "rettet", "kauft", "klaut", "isst", "verlässt", "will", "hasst",
				"predigt", "befreit", "erschießt", "erfindet", "heiratet", "verbrennt", "kaut"]
		self.nomen_ende = ["Bayern", "Döner", "Bahn", "Fußball", "RTL", "Dschungel"]
		self.nomen_ende.extend(self.nomen)
	def gib(self):
		t = []
		t.append("<b>" + self.inter[rand(0,len(self.inter) - 1)] + ":</b> ")
		t.append(self.pre[rand(0,len(self.pre) - 1)] + "-")
		t.append(self.nomen[rand(0,len(self.nomen) - 1)] + " ")
		t.append(self.verben[rand(0,len(self.verben) - 1)] + " ")
		t.append(self.nomen_ende[rand(0,len(self.nomen_ende) - 1)])
		return t[0] + t[1] + t[2] + t[3] + t[4]
		
class Simple(resource.Resource):
    isLeaf = True
    def __init__(self):
		resource.Resource.__init__(self)
		self.bild = bild()
		self.header = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>
<title>BILD informiert</title>
</head>
<body>
<center>
		"""
		self.footer = """
		
		
		
		<a href="javascript:this.location.reload();">refresh</a>
		</center>
</body>
</html>
		"""
    def render_GET(self, request):
        return self.header + "<h1>" + self.bild.gib() + "</h1>" + self.footer

if __name__ == '__main__':
	site = server.Site(Simple())
	reactor.listenTCP(8080, site)
	reactor.run()
