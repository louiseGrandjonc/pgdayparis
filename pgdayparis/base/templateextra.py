# This needs to go in it's own file so we can easily import
# it into a completely different django app (such as the
# main pgeu website one)

import random

"""
sponsor_platinum = [
		{'name': '2ndQuadrant', 'url': 'http://www.2ndquadrant.com/', 'img': '2ndquadrant.png'},
		{'name': 'EDB', 'url': 'http://www.enterprisedb.com/', 'img': 'enterprisedb.png'},
		{'name': 'Trustly', 'url': 'http://www.trustly.com/en/', 'img': 'trustly.png'},
	]
sponsor_gold = [
		{'name': 'Cybertec', 'url': 'http://www.cybertec.at/', 'img': 'cybertec.png'},
		{'name': 'Credativ', 'url': 'http://www.credativ.com/', 'img': 'credativ.png'},
		{'name': '8kdata', 'url': 'http://www.8kdata.com/', 'img': '8kdata.png'},

	]
sponsor_silver = [
		{'name': 'Zalando', 'url': 'http://tech.zalando.com/', 'img': 'zalando.png'},
		{'name': 'Dalibo', 'url': 'http://www.dalibo.com/', 'img': 'dalibo.png'},
		{'name': 'CitusData', 'url': 'http://www.citusdata.com/', 'img': 'citusdata.png'},
		{'name': 'GetClouder', 'url': 'http://www.getclouder.com/', 'img': 'getclouder.png'},
		{'name': 'Bayer', 'url': 'http://business-services.bayer.com/', 'img': 'bayer.png'},
		{'name': 'Schibsted Classified Media', 'url': 'http://www.schibsted.com/en/Online-Classified/', 'img': 'scm.png'},
	]
sponsor_bronze = [
		{'name': 'Roclasi', 'url': 'http://roclasi.com/', 'img': 'roclasi.png'},
		{'name': 'Bitnami', 'url': 'https://bitnami.com/', 'img': 'bitnami.png'},
		{'name': 'CartoDB', 'url': 'http://cartodb.com/', 'img': 'cartodb.png'},
		{'name': 'PuppetLabs', 'url': 'http://www.puppetlabs.com/', 'img': 'puppetlabs.png'},
		{'name': 'Redpill Linpro', 'url': 'http://www.redpill-linpro.com/', 'img': 'redpill.png'},
		{'name': 'OpenSCG', 'url': 'http://www.openscg.com/', 'img': 'openscg.png'},
		{'name': 'Adjust', 'url': 'http://www.adjust.com/', 'img': 'adjust.png'},
		{'name': 'GoodData', 'url': 'http://www.gooddata.com/', 'img': 'gooddata.png'},
		{'name': 'EngineYard', 'url': 'http://www.engineyard.com/', 'img': 'engineyard.png'},
	]
"""


def context_template_additions():
		# Shuffle sponsors (we do all of them, even though in theory we wouldn't
		# need the bronze ones everywhere, because it's easier)
		random.shuffle(sponsor_platinum)
		random.shuffle(sponsor_gold)
		random.shuffle(sponsor_silver)
		random.shuffle(sponsor_bronze)

		return {
			'sp_plat': sponsor_platinum,
			'sp_gold': sponsor_gold,
			'sp_silver': sponsor_silver,
			'sp_bronze': sponsor_bronze,
			}
