from google.appengine.ext import ndb

class PagePost():
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def listString(self, page_id):
        return "<a href='brain?page_id=" + str(page_id) + "'>" + self.title + "</a>"

page_list = [
    PagePost ("HOME", """<body id = 'homepage'><h1>Click on sections of the brain to watch it closer:</h1>


    <img src="https://lh3.google.com/u/0/d/0B1sf9FkLScdDVVhmZkhyTFNOMG8=w2880-h1564-iv1" alt="" usemap="#Map" />
    <div  class = 'description'>
      <h2>BIG BRAIN!!</h2>
      <p>This is a Brain.</p>
      <p id = 'explanation'>The brain is one of the largest and most complex organs in the human body. It is made up of more than 100 billion nerves that communicate in trillions of connections called synapses. The brain is made up of many specialized areas that work together: The cortex is the outermost layer of brain cells.</p>
    </div>

    <map name="Map" id="Map">
        <area class = 'mapping' id = 'temporal_lobe'alt="" title="" href='#' shape="poly" coords="804,347,813,399,794,420,783,443,768,467,760,470,750,483,736,492,728,495,735,502,698,521,666,535,598,541,567,540,531,557,487,576,463,604,411,614,371,623,333,605,285,563,265,540,264,512,268,493,280,477,297,456,309,435,317,413,326,400,341,388,361,378,385,368,415,361,429,350,448,340,475,336,486,332,507,317,528,310,552,305" />
        <area class = 'mapping' id = 'frontal_lobe'alt="" title="" href='#' shape="poly" coords="256,530,180,538,137,534,112,523,104,515,77,493,66,474,56,449,52,426,48,414,43,405,39,388,43,371,41,363,40,334,39,319,45,304,48,285,53,273,64,263,69,250,72,236,80,225,100,213,122,178,149,156,179,137,212,121,243,102,287,90,332,75,381,57,420,55,443,50,463,49,477,47,499,50,520,51,551,55,544,83,498,97,482,111,483,130,489,146,490,158,477,172,472,196,464,221,452,239,448,270,424,310,441,339,422,353,405,362,370,370,347,379,323,396,312,423,305,442,284,462,273,477,266,492,261,523"/>
        <area class = 'mapping' id = 'parietal_lobe'alt="" title="" href="#" shape="poly" coords="557,56,555,63,548,82,516,94,484,108,481,130,493,148,493,161,476,176,468,206,454,230,443,286,424,314,444,338,471,334,508,314,539,304,552,302,807,345,813,318,840,291,853,276,867,264,881,249,870,219,850,206,841,184,825,164,802,152,780,133,745,106,710,86,691,77,669,78,652,64,618,56,589,59,573,54"/>
        <area class = 'mapping' id = 'occipital_lobe'alt="" title="" href="#" shape="poly" coords="881,252,903,265,907,283,921,300,933,331,947,351,957,368,953,381,958,409,952,427,948,444,941,458,931,471,921,483,903,494,878,503,847,504,817,501,794,512,761,510,740,504,733,495,747,487,757,477,773,466,788,431,800,412,815,399,816,389,814,363,811,352,809,335,818,312" />
        <area class = 'mapping' id = 'cerebellum'alt="" title="" href="#" shape="poly" coords="540,559,541,567,545,575,549,596,565,615,576,618,593,631,608,638,624,644,646,653,674,660,701,663,730,658,744,650,763,642,784,632,802,620,808,613,840,592,866,566,871,540,870,518,867,509,838,505,815,506,798,510,775,514,754,509,741,507,721,515,692,525,677,534,622,542,584,547,567,545" />
        <area class = 'mapping' id = 'spinal_cord'alt="" title="" href="#" shape="poly" coords="509,573,528,610,552,622,566,633,581,648,602,672,620,695,656,677,658,673,644,658,641,653,619,643,602,635,585,624,574,617,561,614,551,604,545,583,542,572,538,564,536,562,535,560" />

       <!-- [...]-->
    </map></body"""),
    PagePost ("INFO", "This is all the brain info. "),
    PagePost ("NEWS", """<div class = 'content'>
      <a class = 'news' href = 'http://www.huffingtonpost.com/entry/what-exactly-is-brain-freeze-and-how-do-i-make-it-stop_us_596d0ff6e4b07f87578e6b10?utm_hp_ref=brain'><h2>What Exactly Is Brain Freeze And How Do I Make It Stop?</h2></a>
      <hr>
      <a class = 'news'href = 'https://www.forbes.com/sites/daviddisalvo/2016/01/30/study-your-brains-capacity-is-10-times-greater-than-previously-thought/#3e880341528e'><h2>Your Brain's Capacity Is 10 Times Greater Than Previously Thought</h2></a>
      <hr>
    </div>"""),
    PagePost ("ABOUT THE CREATORS", "This is about us."),
    PagePost ("REFERENCES", "This is our citations. ")
]
