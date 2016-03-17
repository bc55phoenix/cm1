#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

import re
import time
import string
from twitter import *
import yweather
import codecs
import io
import shutil
import sys
from HTMLParser import HTMLParser # HTML unescaping via standard lib
from bs4.dammit import EntitySubstitution # HTML escaping, via BeautifulSoup4

reload(sys)
sys.setdefaultencoding('utf-8')

htmlparser = HTMLParser()
esub = EntitySubstitution()

html = """
	<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Bhagya</title>
    
    
    
    
        <style type="text/css">

              #mtabs_wrapper {
                  width: 100%%;
              }
              #mtabs_container {
                  border-bottom: 1px solid #ccc;
              }
              #mtabs {
                  list-style: none;
                  padding: 5px 0 4px 0;
                  margin: 0 0 0 0px;
                  /* font: 0.75em arial; */
              }
              #mtabs li {
                  display: inline;
              }
              #mtabs li a {
                  border: 1px solid #ccc;
                  padding: 4px 6px;
                  text-decoration: none;
                  color:#000;
                  font-family: Artifika, serif; 
                  background-color: #eeeeee;
                  font-size:14px;
                  /*border-bottom: 1px solid #ccc;
                  outline: none;*/
                  border-radius: 5px 5px 5px 5px;
                  -moz-border-radius: 5px 5px 5px 5px;
                  -webkit-border-top-left-radius: 5px;
                  -webkit-border-top-right-radius: 5px;
              }
              #mtabs li a:hover {
                  background-color: #dddddd;
                  padding: 4px 6px;
              }
              #mtabs li.active a {
                  border-bottom: 1px solid #ccc;
                  background-color: #fff;
                  padding: 4px 6px 5px 6px;
                  /*border-bottom: none;*/
              }
              #mtabs li.active a:hover {
                  background-color: #eeeeee;
                  padding: 4px 6px 5px 6px;
                  /*border-bottom: none;*/
              }
               
              #mtabs li a.icon_accept {
                  background-image: url(accept.png);
                  background-position: 5px;
                  background-repeat: no-repeat;
                  padding-left: 24px;
              }
              #mtabs li a.icon_accept:hover {
                  padding-left: 24px;
              }
               
              #mtabs_content_container {
                  border: 1px solid #ccc;
                  border-top: 1px solid #ccc;
                  padding: 25px;
                  width: 100%%;
                  height: 100%%;
              }
              .mtab_content {
                  display: none;
              }

              /* TAB CSS END */

        </style>

    
    
    
  </head>

  <body>

    <script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'></script>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type='text/javascript'>

  var $ = jQuery;

  google.charts.load('current', {'packages': ['geochart']});
     google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {
      var data = google.visualization.arrayToDataTable([
        ['City',   'Info', {role: 'tooltip', p:{html:true}}],
        %s
      ]);
      
       var data2 = google.visualization.arrayToDataTable([
        ['City',   'Info', {role: 'tooltip', p:{html:true}}],
        %s
      ]);
      
      var data3 = google.visualization.arrayToDataTable([
        ['City',   'Info', {role: 'tooltip', p:{html:true}}],
        %s
      ]);
      
      var data4 = google.visualization.arrayToDataTable([
        ['City',   'Info', {role: 'tooltip', p:{html:true}}],
        %s
      ]);
      
      var data5 = google.visualization.arrayToDataTable([
        ['City',   'Info', {role: 'tooltip', p:{html:true}}],
        %s
      ]);

      var options = {
        region: 'world',
        width: '1112',
        height: '500',
        displayMode: 'markers',
        colorAxis: {colors: ['pink', 'red']},
        tooltip: {
            isHtml: true
        }
      };
      
      var options2 = {
        region: 'world',
        width: '1112',
        height: '500',
        displayMode: 'markers',
        colorAxis: {colors: ['cyan', 'blue']},
        tooltip: {
            isHtml: true
        }
      };
      
      var options3 = {
        region: 'world',
        width: '1112',
        height: '500',
        displayMode: 'markers',
        colorAxis: {colors: ['yellow', 'green']},
        tooltip: {
            isHtml: true
        }
      };
      
      var options4 = {
        region: 'world',
        width: '1112',
        height: '500',
        displayMode: 'markers',
        colorAxis: {colors: ['yellow', 'orange']},
        tooltip: {
            isHtml: true
        }
      };
      
      var options5 = {
        region: 'world',
        width: '1112',
        height: '500',
        displayMode: 'markers',
        colorAxis: {colors: ['grey', 'black']},
        tooltip: {
            isHtml: true
        }
      };

      var chart = new google.visualization.GeoChart(document.getElementById('tab1'));
      var chart2 = new google.visualization.GeoChart(document.getElementById('tab2'));
      var chart3 = new google.visualization.GeoChart(document.getElementById('tab3'));
      var chart4 = new google.visualization.GeoChart(document.getElementById('tab4'));
      var chart5 = new google.visualization.GeoChart(document.getElementById('tab5'));
      
      chart.draw(data, options);

      chart2.draw(data2, options2);

      chart3.draw(data3, options3);
    
      chart4.draw(data4, options4);

      chart5.draw(data5, options5);
		}


    $(document).ready(function(){
    //  When user clicks on tab, this code will be executed
    $("#mtabs li").click(function() {
        //  First remove class "active" from currently active tab
        $("#mtabs li").removeClass('active');
 
        //  Now add class "active" to the selected/clicked tab
       $(this).addClass("active");
 
        //  Hide all tab content
        $(".mtab_content").hide();
 
        //  Here we get the href value of the selected tab
        var selected_tab = $(this).find("a").attr("href");
 
        //  Show the selected tab content
        $(selected_tab).fadeIn();
 
        //  At the end, we add return false so that the click on the link is not executed
        return false;
    });
  $("#simulate").click(function(){
    $('a[rel="tab2"]').trigger("click");
  });
});

</script>

<div class="mtabs_wrapper">
  <!-- Original tabs START -->

  <div id="mtabs">
    <ul>
      <li><a href="#tab1" rel="tab1">Kartik</a></li>
      <li><a href="#tab2" rel="tab2">Bhagya</a></li>
      <li><a href="#tab3" rel="tab3">Jean</a></li>
      <li class="active"><a href="#tab4" rel="tab4">Alap</a></li>
      <li><a href="#tab5" rel="tab1">Acsa</a></li>
      <li><h1>#Care4urFrnds</h1> - Click <a href="https://docs.google.com/document/d/1q3BFsJH-1Cz_91XxCL3S2DhNBggqC9ut3DsGdwqfKxA/edit?usp=sharing">here</a> for the explanation report.</li>
    </ul>
  </div>

  <div id="mtabs_content_container">
    <div id="tab1" class="mtab_content" style="width: 100%%; height: 100%%;">
    </div>
    <div id="tab2" class="mtab_content" style="width: 100%%; height: 100%%;">
    </div>
    <div id="tab3" class="mtab_content" style="width: 100%%; height: 100%%;">
    </div>
    <div id="tab4" class="mtab_content" style="width: 100%%; height: 100%%;">
    </div>
    <div id="tab5" class="mtab_content" style="width: 100%%; height: 100%%;">
    </div>

  </div>
  <!-- Original tabs END -->
</div>
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

        

    
    
    
  </body>
</html>

"""

csvAll = io.open( "Kartik.csv", "r", encoding="utf-8" ).read( )
csvAll2 = io.open( "Bhagya.csv", "r", encoding="utf-8" ).read( )
csvAll3 = io.open( "Jean.csv", "r", encoding="utf-8" ).read( )
csvAll4 = io.open( "Alap.csv", "r", encoding="utf-8" ).read( )
csvAll5 = io.open( "Acsa.csv", "r", encoding="utf-8" ).read( )

# print csvAll

recs = csvAll.split('\n')
recs2 = csvAll2.split('\n')
recs3 = csvAll3.split('\n')
recs4 = csvAll4.split('\n')
recs5 = csvAll5.split('\n')


# print recs

# print len(recs)

eachRec = []
eachRec2 = []
eachRec3 = []
eachRec4 = []
eachRec5 = []

for rec in recs:
	each = rec.split(',')
	eachRec.append(each)

for rec in recs2:
	each2 = rec.split(',')
	eachRec2.append(each2)

for rec in recs3:
	each3 = rec.split(',')
	eachRec3.append(each3)

for rec in recs4:
	each4 = rec.split(',')
	eachRec4.append(each4)

for rec in recs5:
	each5 = rec.split(',')
	eachRec5.append(each5)

# for every in eachRec:
# 	print every

# print eachRec[0]
# print eachRec[0][0]
# print eachRec[0][1]

# for per in eachRec:
# 	for elm in per:
# 		print elm

# for per in eachRec:
# 	print per[0]

# for per in eachRec:
# 	print per[1]

client = yweather.Client()

config = {}
execfile("config.py", config)

twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


htmlStr = ""
htmlStr2 = ""
htmlStr3 = ""
htmlStr4 = ""
htmlStr5 = ""

for per in eachRec:

		htmlStr += "["

		locStr = str(per[0])
		instStr = str(per[2])
		frnds_list = str(per[1])
		# print frnds_list

		htmlStr += "\'" + locStr + "\',"
		htmlStr += instStr + ","
		htmlStr += "\'#Friends: " + instStr + "</br>"
		htmlStr += "Friends: " + frnds_list + "</br>"
		

		loc_id = client.fetch_woeid(locStr)
		if loc_id is not None:
			loc_id_int = int(loc_id)
		else:
			loc_id_int = 0

		loc_weather = client.fetch_weather(str(loc_id_int))

		if (loc_weather is not None) and (loc_id_int != 0):
			atmPr = str(loc_weather["atmosphere"]["pressure"])
			cond = str(loc_weather["condition"]["text"])

		else:
			atmPr = "NA"
			cond = "NA"

		htmlStr += "AtmPr: " + atmPr + "</br>"
		htmlStr += "Weather: " + cond + "</br>"
		# print htmlStr
		# time = ""
		user = ""
		tweet = ""

		# try:
		# 	query = twitter.search.tweets(q = locStr, count = 1)

		# 	for result in query["statuses"]:
		# 		time = result["created_at"]
		# 		user = result["user"]["screen_name"]
		# 		tweet = result["text"]
		# 		tweet = tweet.replace("'", "\\'")
		# 		tweet = tweet.replace("\n", "")				
		# 		# emoji_pattern = re.compile("["
		# 		# 		u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+", flags=re.UNICODE)
		# 		# tweet = (emoji_pattern.sub(r'', tweet)) # no emoji
		# 		printable = set(string.printable)
		# 		tweet = filter(lambda x: x in printable, tweet)
		# 		tweet = esub.substitute_html(tweet)
		# except:
		# 	print "404 "
		# 	htmlStr += "\'],"
		# 	continue


		# htmlStr += "Latest: " + user + " " + tweet + "</br>"

		trndNo = 0
		trend_list = "NA"

		if loc_id_int == 0:
			trndNo = 0
			trend_list = "NA"
		else:
			try:
				results = twitter.trends.place(_id = loc_id_int)
				trend_list = ""
				for location in results:
						for trend in location["trends"]:
			 				trndNo += 1
			 				print trend["name"]
			 				trend_list +=  trend["name"]
			 				trend_list += ", "
		 		trend_list = trend_list[:-2]
		 		printable = set(string.printable)
				trend_list = filter(lambda x: x in printable, trend_list)
				trend_list = esub.substitute_html(trend_list)
			except:
				trndNo = 0
				trend_list = "NA"
				print "404 "
				htmlStr += "\'],"
				continue

		htmlStr += "</br>Trends#: " + str(trndNo) + "</br>"
		htmlStr += "Trending: " + trend_list + "</br>"

		img1 = per[3]
		img2 = per[4]
		img3 = per[5]
		img4 = per[6]
		img5 = per[7]

		htmlStr += "</br> <img src=\"" + img1 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr += "</br> <img src=\"" + img2 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr += "</br> <img src=\"" + img3 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr += "</br> <img src=\"" + img4 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr += "</br> <img src=\"" + img5 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr += "\'],"

		# print htmlStr
		# print "\n"

htmlStr = htmlStr[:-1]
print htmlStr
time.sleep(1200)

for per in eachRec2:

		htmlStr2 += "["

		locStr2 = str(per[0])
		# print locStr2
		instStr2 = str(per[2])
		frnds_list2 = str(per[1])

		htmlStr2 += "\'" + locStr2 + "\',"
		htmlStr2 += instStr2 + ","
		htmlStr2 += "\'#Friends: " + instStr2 + "</br>"
		htmlStr2 += "Friends: " + frnds_list2 + "</br>"
		

		loc_id2 = client.fetch_woeid(locStr2)
		if loc_id2 is not None:
			loc_id_int2 = int(loc_id2)
		else:
			loc_id_int2 = 0

		loc_weather2 = client.fetch_weather(str(loc_id_int2))

		if (loc_weather2 is not None) and (loc_id_int2 != 0):
			atmPr2 = str(loc_weather2["atmosphere"]["pressure"])
			cond2 = str(loc_weather2["condition"]["text"])

		else:
			atmPr2 = "NA"
			cond2 = "NA"

		htmlStr2 += "AtmPr: " + atmPr2 + "</br>"
		htmlStr2 += "Weather: " + cond2 + "</br>"
		time2 = ""
		user2 = ""
		tweet2 = ""

		# try:
		# 	query2 = twitter.search.tweets(q = locStr2, count = 1)

		# 	for result2 in query2["statuses"]:
		# 		time2 = result2["created_at"]
		# 		user2 = result2["user"]["screen_name"]
		# 		tweet2 = result2["text"]
		# 		tweet2 = tweet2.replace("'", "\\'")
		# 		tweet2 = tweet2.replace("\n", "")				
		# 		# emoji_pattern = re.compile("["
		# 		# 		u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+", flags=re.UNICODE)
		# 		# tweet = (emoji_pattern.sub(r'', tweet)) # no emoji
		# 		printable2 = set(string.printable)
		# 		tweet2 = filter(lambda x: x in printable2, tweet2)
		# 		tweet2 = esub.substitute_html(tweet2)
		# except:
		# 	print "404 "
		# 	htmlStr2 += "\'],"
		# 	continue


		#htmlStr2 += "Latest: " + user2 + " " + tweet2 + "</br>"

		trndNo2 = 0
		trend_list2 = "NA"

		if loc_id_int2 == 0:
			trndNo2 = 0
			trend_list2 = "NA"
		else:
			try:
				results2 = twitter.trends.place(_id = loc_id_int)
				trend_list2 = ""
				for location2 in results2:
					for trend2 in location2["trends"]:
		 				trndNo2 += 1
		 				print trend2["name"]
		 				trend_list2 +=  trend2["name"]
		 				trend_list2 += ", "
		 		trend_list2 = trend_list2[:-2]
		 		printable2 = set(string.printable)
				trend_list2 = filter(lambda x: x in printable2, trend_list2)
				trend_list2 = esub.substitute_html(trend_list2)
			except:
				trndNo2 = 0
				trend_list2 = "NA"
				print "404 "
				htmlStr2 += "\'],"
				continue

		htmlStr2 += "</br>Trends#: " + str(trndNo2) + "</br>"
		htmlStr2 += "Trending: " + trend_list2 + "</br>"

		img1 = per[3]
		img2 = per[4]
		img3 = per[5]
		img4 = per[6]
		img5 = per[7]

		htmlStr2 += "</br> <img src=\"" + img1 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr2 += "</br> <img src=\"" + img2 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr2 += "</br> <img src=\"" + img3 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr2 += "</br> <img src=\"" + img4 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr2 += "</br> <img src=\"" + img5 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"


		htmlStr2 += "\'],"

		# print htmlStr2
		# print "\n"

htmlStr2 = htmlStr2[:-1]
print htmlStr2
time.sleep(1200)

for per in eachRec3:

		htmlStr3 += "["

		locStr3 = str(per[0])
		# print locStr3
		instStr3 = str(per[2])
		frnds_list3 = str(per[1])

		htmlStr3 += "\'" + locStr3 + "\',"
		htmlStr3 += instStr3 + ","
		htmlStr3 += "\'#Friends: " + instStr3 + "</br>"
		htmlStr3 += "Friends: " + frnds_list3 + "</br>"
		

		loc_id3 = client.fetch_woeid(locStr3)
		if loc_id3 is not None:
			loc_id_int3 = int(loc_id3)
		else:
			loc_id_int3 = 0

		loc_weather3 = client.fetch_weather(str(loc_id_int3))

		if (loc_weather3 is not None) and (loc_id_int3 != 0):
			atmPr3 = str(loc_weather3["atmosphere"]["pressure"])
			cond3 = str(loc_weather3["condition"]["text"])

		else:
			atmPr3 = "NA"
			cond3 = "NA"

		htmlStr3 += "AtmPr: " + atmPr3 + "</br>"
		htmlStr3 += "Weather: " + cond3 + "</br>"
		time3 = ""
		user3 = ""
		tweet3 = ""

		# try:
		# 	query3 = twitter.search.tweets(q = locStr3, count = 1)

		# 	for result3 in query3["statuses"]:
		# 		time3 = result3["created_at"]
		# 		user3 = result3["user"]["screen_name"]
		# 		tweet3 = result3["text"]
		# 		tweet3 = tweet3.replace("'", "\\'")
		# 		tweet3 = tweet3.replace("\n", "")				
		# 		# emoji_pattern = re.compile("["
		# 		# 		u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+", flags=re.UNICODE)
		# 		# tweet = (emoji_pattern.sub(r'', tweet)) # no emoji
		# 		printable3 = set(string.printable)
		# 		tweet3 = filter(lambda x: x in printable3, tweet3)
		# 		tweet3 = esub.substitute_html(tweet3)
		# except:
		# 	print "404 "
		# 	htmlStr3 += "\'],"
		# 	continue


		# htmlStr3 += "Latest: " + user3 + " " + tweet3 + "</br>"

		trndNo3 = 0
		trend_list3 = "NA"

		if loc_id_int3 == 0:
			trndNo3 = 0
			trend_list3 = "NA"
		else:
			try:
				results3 = twitter.trends.place(_id = loc_id_int)
				trend_list3 = ""
				for location3 in results3:
					for trend3 in location3["trends"]:
		 				trndNo3 += 1
		 				print trend3["name"]
	 					trend_list3 +=  trend3["name"]
	 					trend_list3 += ", "
		 		trend_list3 = trend_list3[:-2]
		 		printable3 = set(string.printable)
				trend_list3 = filter(lambda x: x in printable5, trend_list3)
				trend_list3 = esub.substitute_html(trend_list3)
			except:
				trndNo3 = 0
				trend_list3 = "NA"
				print "404 "
				htmlStr3 += "\'],"
				continue

		htmlStr3 += "</br>Trends#: " + str(trndNo3) + "</br>"
		htmlStr3 += "Trending: " + trend_list3 + "</br>"

		img1 = per[3]
		img2 = per[4]
		img3 = per[5]
		img4 = per[6]
		img5 = per[7]

		htmlStr3 += "</br> <img src=\"" + img1 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr3 += "</br> <img src=\"" + img2 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr3 += "</br> <img src=\"" + img3 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr3 += "</br> <img src=\"" + img4 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr3 += "</br> <img src=\"" + img5 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"


		htmlStr3 += "\'],"

		# print htmlStr3
		# print "\n"

htmlStr3 = htmlStr3[:-1]
print htmlStr3
time.sleep(1200)

for per in eachRec4:

		htmlStr4 += "["

		locStr4 = str(per[0])
		# print locStr4
		instStr4 = str(per[2])
		frnds_list4 = str(per[1])


		htmlStr4 += "\'" + locStr4 + "\',"
		htmlStr4 += instStr4 + ","
		htmlStr4 += "\'#Friends: " + instStr4 + "</br>"
		htmlStr4 += "Friends: " + frnds_list4 + "</br>"
		

		loc_id4 = client.fetch_woeid(locStr4)
		if loc_id4 is not None:
			loc_id_int4 = int(loc_id4)
		else:
			loc_id_int4 = 0

		loc_weather4 = client.fetch_weather(str(loc_id_int4))

		if (loc_weather4 is not None) and (loc_id_int4 != 0):
			atmPr4 = str(loc_weather4["atmosphere"]["pressure"])
			cond4 = str(loc_weather4["condition"]["text"])

		else:
			atmPr4 = "NA"
			cond4 = "NA"

		htmlStr4 += "AtmPr: " + atmPr4 + "</br>"
		htmlStr4 += "Weather: " + cond4 + "</br>"
		time4 = ""
		user4 = ""
		tweet4 = ""

		# try:
		# 	query4 = twitter.search.tweets(q = locStr4, count = 1)

		# 	for result4 in query4["statuses"]:
		# 		time4 = result4["created_at"]
		# 		user4 = result4["user"]["screen_name"]
		# 		tweet4 = result4["text"]
		# 		tweet4 = tweet4.replace("'", "\\'")
		# 		tweet4 = tweet4.replace("\n", "")				
		# 		# emoji_pattern = re.compile("["
		# 		# 		u"\U0001F600-\U0001F64F" u"\U0001F400-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+", flags=re.UNICODE)
		# 		# tweet = (emoji_pattern.sub(r'', tweet)) # no emoji
		# 		printable4 = set(string.printable)
		# 		tweet4 = filter(lambda x: x in printable4, tweet4)
		# 		tweet4 = esub.substitute_html(tweet4)
		# except:
		# 	print "404 "
		# 	htmlStr4 += "\'],"
		# 	continue


		# htmlStr4 += "Latest: " + user4 + " " + tweet4 + "</br>"

		trndNo4 = 0
		trend_list4 = "NA"

		if loc_id_int4 == 0:
			trndNo4 = 0
			trend_list4 = "NA"
		else:
			try:
				results4 = twitter.trends.place(_id = loc_id_int4)
				trend_list4 = ""
				for location4 in results4:
					for trend4 in location4["trends"]:
		 				trndNo4 += 1
		 				print trend4["name"]
						trend_list4 +=  trend4["name"]
	 					trend_list4 += ", "
		 		trend_list4 = trend_list4[:-2]
		 		printable4 = set(string.printable)
				trend_list4 = filter(lambda x: x in printable4, trend_list4)
				trend_list4 = esub.substitute_html(trend_list4)
			except:
				trndNo4 = 0
				trend_list4 = "NA"
				print "404 "
				htmlStr4 += "\'],"
				continue

		htmlStr4 += "</br>Trends#: " + str(trndNo4) + "</br>"
		htmlStr4 += "Trending: " + trend_list4 + "</br>"

		img1 = per[3]
		img2 = per[4]
		img3 = per[5]
		img4 = per[6]
		img5 = per[7]

		htmlStr4 += "</br> <img src=\"" + img1 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr4 += "</br> <img src=\"" + img2 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr4 += "</br> <img src=\"" + img3 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr4 += "</br> <img src=\"" + img4 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr4 += "</br> <img src=\"" + img5 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"


		htmlStr4 += "\'],"

		# print htmlStr4
		# print "\n"

htmlStr4 = htmlStr4[:-1]
print htmlStr4
time.sleep(1200)

for per in eachRec5:

		htmlStr5 += "["

		locStr5 = str(per[0])
		# print locStr5
		instStr5 = str(per[2])
		frnds_list5 = str(per[1])

		htmlStr5 += "\'" + locStr5 + "\',"
		htmlStr5 += instStr5 + ","
		htmlStr5 += "\'#Friends: " + instStr5 + "</br>"
		htmlStr5 += "Friends: " + frnds_list5 + "</br>"

		loc_id5 = client.fetch_woeid(locStr5)
		if loc_id5 is not None:
			loc_id_int5 = int(loc_id5)
		else:
			loc_id_int5 = 0

		loc_weather5 = client.fetch_weather(str(loc_id_int5))

		if (loc_weather5 is not None) and (loc_id_int5 != 0):
			atmPr5 = str(loc_weather5["atmosphere"]["pressure"])
			cond5 = str(loc_weather5["condition"]["text"])

		else:
			atmPr5 = "NA"
			cond5 = "NA"

		htmlStr5 += "AtmPr: " + atmPr5 + "</br>"
		htmlStr5 += "Weather: " + cond5 + "</br>"
		time5 = ""
		user5 = ""
		tweet5 = ""

		# try:
		# 	query5 = twitter.search.tweets(q = locStr5, count = 1)

		# 	for result5 in query5["statuses"]:
		# 		time5 = result5["created_at"]
		# 		user5 = result5["user"]["screen_name"]
		# 		tweet5 = result5["text"]
		# 		tweet5 = tweet5.replace("'", "\\'")
		# 		tweet5 = tweet5.replace("\n", "")				
		# 		# emoji_pattern = re.compile("["
		# 		# 		u"\U0001F600-\U0001F65F" u"\U0001F500-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+", flags=re.UNICODE)
		# 		# tweet = (emoji_pattern.sub(r'', tweet)) # no emoji
		# 		printable5 = set(string.printable)
		# 		tweet5 = filter(lambda x: x in printable5, tweet5)
		# 		tweet5 = esub.substitute_html(tweet5)
		# except:
		# 	print "404 "
		# 	htmlStr5 += "\'],"
		# 	continue


		# htmlStr5 += "Latest: " + user5 + " " + tweet5 + "</br>"

		trndNo5 = 0
		trend_list5 = "NA"

		if loc_id_int5 == 0:
			trndNo5 = 0
			trend_list5 = "NA"
		else:
			try:
				results5 = twitter.trends.place(_id = loc_id_int5)
				trend_list = ""
				for location5 in results5:
					for trend5 in location5["trends"]:
		 				trndNo5 += 1
		 				print trend5["name"]
	 					trend_list5 +=  trend5["name"]
	 					trend_list5 += ", "
		 		trend_list5 = trend_list5[:-2]
		 		printable5 = set(string.printable)
				trend_list5 = filter(lambda x: x in printable5, trend_list5)
				trend_list5 = esub.substitute_html(trend_list5)
			except:
				trndNo5 = 0
				trend_list5 = "NA"
				print "404 "
				htmlStr5 += "\'],"
				continue

		htmlStr5 += "</br>Trends#: " + str(trndNo5) + "</br>"
		htmlStr5 += "Trending: " + trend_list5 + "</br>"

		img1 = per[3]
		img2 = per[4]
		img3 = per[5]
		img4 = per[6]
		img5 = per[7]

		htmlStr5 += "</br> <img src=\"" + img1 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr5 += "</br> <img src=\"" + img2 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr5 += "</br> <img src=\"" + img3 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr5 += "</br> <img src=\"" + img4 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"
		htmlStr5 += "</br> <img src=\"" + img5 + " alt=\"FlickrImg\" height=\"42\" width=\"100\" border=2em> </br>"


		htmlStr5 += "\'],"

		# print htmlStr5
		# print "\n"

htmlStr5 = htmlStr5[:-1]
print htmlStr5


open( "cm.html", "w" ).write( html % (htmlStr, htmlStr2, htmlStr3, htmlStr4, htmlStr5) )







