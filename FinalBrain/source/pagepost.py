from google.appengine.ext import ndb


class CommentsData(ndb.Model):
    comment_page_id = ndb.IntegerProperty()
    comment_string = ndb.StringProperty(repeated = True)

class PagePost():
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def listString(self, page_id):
        return "<a href='brain?page_id=" + str(page_id) + "'>" + self.title + "</a>"
    def commentsAsHTML(self, page_id, new_comment):
        comments_query = CommentsData.query(CommentsData.comment_page_id == page_id)
        comments_data = comments_query.get()
        if comments_data == None:
            if new_comment == None:
                return "<p style=color:black> No comments yet </p>"
            else:
                comment_list = [ new_comment ]
                comments_data = CommentsData(comment_page_id = page_id,
                                            comment_string = comment_list)
                comments_data.put()
                return "<p style=color:black>" + new_comment + "</p>"
        else:
            if new_comment != None:
                comments_data.comment_string.append(new_comment)
            html_string = ""
            for comment in comments_data.comment_string:
                html_string += "<p style=color:black>" + comment + "</p>"
            if new_comment != None:
                comments_data.put()
            return html_string


page_list = [
    PagePost ("HOME", """<body id="homepage" ><h4 style="color:White">Whether you're studying Psychology or Medicine, this site will inform you about parts of the brain.
    Learning and remembering parts of the brain can be tricky. Enjoy this interactive digital brain map! Use it to your studying advantages!</h4>


    <img src="https://lh3.google.com/u/0/d/0B1sf9FkLScdDVVhmZkhyTFNOMG8=w2880-h1564-iv1" alt="" usemap="#Map" />
    <div class="topcorner"= 'description'>


      <p id= "explanation" >The brain is one of the largest and most complex organs in the human body. It is made up of more than 100 billion nerves that communicate in trillions of connections called synapses. The brain is made up of many specialized areas that work together: The cortex is the outermost layer of brain cells.</p>
      <p id = 'temporal' style = 'display: none;'>The Temporal Lobe mainly revolves around hearing and selective listening. It receives sensory information such as sounds and speech from the ears. It is also key to being able to comprehend, or understand meaningful speech. In fact, we would not be able to understand someone talking to us, if it wasn't for the temporal lobe. This lobe is special because it makes sense of the all the different sounds and pitches (different types of sound) being transmitted from the sensory receptors of the ears.</p>
    <p id = 'frontal' style = 'display: none;'>You use your frontal lobe nearly everyday. You use it to make decisions, such as what to eat or drink for breakfast in the morning, as well as for thinking or studying for a test. The frontal lobe is also where our personality is formed and where we can carry out higher mental processes such as planning. In addition, the frontal lobe is necessary to being able to speak fluently (without fault) and meaningfully.</p>
    <p id = 'parietal' style = 'display: none;'>The parietal lobe carries out some very specific functions. As a part of the cortex, it has a lot of responsibilities and has to be able to process sensory information within seconds. The parietal lobe is where information such as taste, temperature and touch are integrated, or processed. Humans would not be able to to feel sensations of touch, if the parietal lobe was damaged.</p>
    <p id = 'occipital' style = 'display: none;'>The occiptial lobe is important to being able to correctly understand what your eyes are seeing. These lobes have to be very fast to process the rapid information that our eyes are sending. Similar to how the temporal lobe makes sense of auditory information, the occipital lobe makes sense of visual information so that we are able to understand it. If our occipital lobe was impaired, or injured we would not be able to correctly process visual signals, thus visual confusion would result.</p>
    <p id = 'cereb' style = 'display: none;'>The cerebellum is one of the most identifiable parts of the brain due to its unique shape and location. It is extremely important for being able to perform everyday voluntary (done with purpose and intent) tasks such as walking and writing. It is also essential to being able to stay balanced and upright. Patients who have suffered from damaged cerebellums often struggle with keeping their balance and maintaining proper muscle coordination.</p>
    <p id = 'spinal' style = 'display: none;'>The spinal cord is a complex cylinder of nerves that starts at the base of your brain and runs down the vertebral canal to the backbone. It is part of the body's collection of nerves, called the central nervous system, along with the brain. In each of the spinal cord's many segments lives a pair of roots that are made up of nerve fibers. These roots are referred to as the dorsal and the ventral.</p>
    </div>
    <map name="Map" id="Map">
        <area class = 'mapping' id = 'temporal_lobe' alt="" title="" href='#' shape="poly" coords="804,347,813,399,794,420,783,443,768,467,760,470,750,483,736,492,728,495,735,502,698,521,666,535,598,541,567,540,531,557,487,576,463,604,411,614,371,623,333,605,285,563,265,540,264,512,268,493,280,477,297,456,309,435,317,413,326,400,341,388,361,378,385,368,415,361,429,350,448,340,475,336,486,332,507,317,528,310,552,305" />
        <area class = 'mapping' id = 'frontal_lobe' alt="" title="" href='#' shape="poly" coords="256,530,180,538,137,534,112,523,104,515,77,493,66,474,56,449,52,426,48,414,43,405,39,388,43,371,41,363,40,334,39,319,45,304,48,285,53,273,64,263,69,250,72,236,80,225,100,213,122,178,149,156,179,137,212,121,243,102,287,90,332,75,381,57,420,55,443,50,463,49,477,47,499,50,520,51,551,55,544,83,498,97,482,111,483,130,489,146,490,158,477,172,472,196,464,221,452,239,448,270,424,310,441,339,422,353,405,362,370,370,347,379,323,396,312,423,305,442,284,462,273,477,266,492,261,523"/>
        <area class = 'mapping' id = 'parietal_lobe' alt="" title="" href="#" shape="poly" coords="557,56,555,63,548,82,516,94,484,108,481,130,493,148,493,161,476,176,468,206,454,230,443,286,424,314,444,338,471,334,508,314,539,304,552,302,807,345,813,318,840,291,853,276,867,264,881,249,870,219,850,206,841,184,825,164,802,152,780,133,745,106,710,86,691,77,669,78,652,64,618,56,589,59,573,54"/>
        <area class = 'mapping' id = 'occipital_lobe' alt="" title="" href="#" shape="poly" coords="881,252,903,265,907,283,921,300,933,331,947,351,957,368,953,381,958,409,952,427,948,444,941,458,931,471,921,483,903,494,878,503,847,504,817,501,794,512,761,510,740,504,733,495,747,487,757,477,773,466,788,431,800,412,815,399,816,389,814,363,811,352,809,335,818,312" />
        <area class = 'mapping' id = 'cerebellum' alt="" title="" href="#" shape="poly" coords="540,559,541,567,545,575,549,596,565,615,576,618,593,631,608,638,624,644,646,653,674,660,701,663,730,658,744,650,763,642,784,632,802,620,808,613,840,592,866,566,871,540,870,518,867,509,838,505,815,506,798,510,775,514,754,509,741,507,721,515,692,525,677,534,622,542,584,547,567,545" />
        <area class = 'mapping' id = 'spinal_cord' alt="" title="" href="#" shape="poly" coords="509,573,528,610,552,622,566,633,581,648,602,672,620,695,656,677,658,673,644,658,641,653,619,643,602,635,585,624,574,617,561,614,551,604,545,583,542,572,538,564,536,562,535,560" />
    </map></body>"""),
    PagePost ("INFO", """
<!DOCTYPE html>
<html>
<head>
<link rel = 'stylesheet' href = 'resources/Brain.css'>
<meta charset="UTF-8">
<title>Information</title>
</head>
<body <!--style= "background-color:DarkMagenta;background-image:none;"-->


<h1>Information About the brain</h1>
<center><h2 style= "background: linear-gradient(to bottom, #ccff33 0%, #ff99cc 100%);">Whats To Know?</h2></center>
<div style="background-color:CornflowerBlue; overflow:auto;">
<center><h2 style="color:DeepPink">Cerebellum</h2></center>
    <img src="http://www.daviddarling.info/images/cerebellum.jpg" alt="Mountain View"
    style="width:250px;height:270px;">
    <p class="center_in_page" style="color:yellow;">The Cerebellum: The cerebellum, or "little brain",</p><br>
    <p class="center_in_page" style="color:yellow;">is similar to the cerebrum in that it has two hemispheres.</p><br>

    <p class="center_in_page" style="color:yellow;">Obtaining a general understanding of the brain and its functions is important </p><br>
    <p class="center_in_page" style="color:yellow;">to understanding the rehabilitation process. It is very important, however, </p><br>
    <p class="center_in_page" style="color:yellow;">to understand that the rehabilitation professional is concerned with the whole person.</p><br>
     <p class="center_in_page" style="color:yellow;">The identification of individual problems gives the rehabilitation team areas in </p><br>
     <p class="center_in_page" style="color:yellow;">which to focus treatment plans, all of these plans are designed to work toward the </p><br>
     <p class="center_in_page" style="color:yellow;">rehabilitation of the whole person. Each problem area affects other areas and many </p><br>
     <p class="center_in_page" style="color:yellow;">times resolving one problem has a major impact on other problems. For example, reestablishing </p><br>
     <p class="center_in_page" style="color:yellow;">postural balance and eliminating dizziness greatly enhances concentration and attention which </p><br>
     <p class="center_in_page" style="color:yellow;">allows for improved cognition and problem solving.</p>
</div>
<div style="background-color:DeepPink;overflow:auto;">
<center><h2 style="color:White">Frontal Lobe</h2></center>
<img src="https://www.neuroskills.com/images/frontlobe11.jpg" alt="Mountain View"
style="width:250px;height:270px;">
    <p class="center_in_page"style="color:yellow;">The frontal lobe links and integrates all components of behavior at the highest</p><br>
    <p class="center_in_page" style="color:yellow;">level. Emotion and social adjustment and impulse control are also localized here.</p><br>
    <p class="center_in_page" style="color:yellow;">Injury to parts of the frontal lobe may cause an inability to move part of the</p><br>
    <p class="center_in_page"style="color:yellow;">body or the whole side of the body. Speech may become halting, disorganized or</p><br>
    <p class="center_in_page" style="color:yellow;"> be stopped except for single explosive words. Personality may change. Social</p><br>
    <p class="center_in_page" style="color:yellow;"> rules of behavior may be disregarded.</p>
</div>
<div style="background-color:orange;overflow:auto;">
    <center><h2 style="color:SeaGreen">Occipital Lobe</h2></center>
    <img src="http://brainmadesimple.com/uploads/7/8/8/5/7885523/_5203909.jpg" alt="Mountain View"
    style="width:270px;height:150px;">


    <p class="center_in_page" style="color:purple;">Injury to this area usually results in "blindness" to part or all of the visual field. </p><br>
    <p class="center_in_page" style="color:purple;">Usually people experience "holes" or "blind spots"in what they see.</p><br>
    <p class="center_in_page" style="color:purple;">There may be problems picking things out of space or they may misperceive pictures or objects.</p><br>
    <p class="center_in_page" style="color:purple;">Recognition of colors may also be disturbed.</p>

     </div>
<div style="background-color:DarkRed;overflow:auto;">
    <center><h2 style="color:White">Temporal Lobe</h2></center>
    <img src="http://www.neuroskills.com/images/templobe11.jpg" alt="Mountain View"
    style="width:250px;height:270px;">

        <p class="center_in_page"style="color:silver;">The temporal lobe perceives and recognizes verbal material. </p><br>
        <p class="center_in_page" style="color:silver;">It is among the most frequently injured parts of the brain during head injury. </p><br>
        <p class="center_in_page" style="color:silver;">A person may have difficulty screening out distractions.</p><br>
        <p class="center_in_page" style="color:silver;">Injury to the upper temporal area can cause someone to misunderstand what is said. </p><br>
        <p class="center_in_page" style="color:silver;">They may make sounds like words but which are not recognizable as words at all. </p><br>
        <p class="center_in_page" style="color:silver;">They may also misunderstand body language. Emotional changes such as unexplained panic </p><br>
        <p class="center_in_page" style="color:silver;">or unexpected tearfulness may be noted. Left temporal area includes production of speech, </p><br>
        <p class="center_in_page" style="color:silver;">naming and verbal memory. The right temporal area includes musical abilities, foreign </p><br>
        <p class="center_in_page" style="color:silver;">languages, visual memory, and comprehension of the environment.</p>

     </div>
<div style="background-color:LightBlue;overflow:auto;">
         <center><h2 style="color:OrangeRed">BrainStem</h2></center>
         <img src="http://www.neuroskills.com/images/brainstem11.jpg" alt="Mountain View"
         style="width:250px;height:270px;">

         <p class="center_in_page"  style="color:Navy;">The brain stem plays a vital role in basic attention, arousal, and consciousness.</p><br>
         <p class="center_in_page"  style="color:Navy;">All information to and from our body passes through the brain</p><br>
         <p class="center_in_page"  style="color:Navy;">stem on the way to or from our brain.</p><br>
          <p class="center_in_page"  style="color:Navy;">Like the frontal and temporal lobes, the brain stem is </p><br>
          <p class="center_in_page"  style="color:Navy;">located in an area near bony protrusions making</p><br>
          <p class="center_in_page"  style="color:Navy;">it vulnerable to damage during trauma.</p>
          </div

</body>
</html>
"""),
    PagePost ("NEWS", ""),
    PagePost ("ABOUT THE CREATORS", "This is about us."),
    PagePost ("REFERENCES", """
<!DOCTYPE html>
<html>
<head>
<body>
<link rel = 'stylesheet' href = 'resources/Brain.css'>
<meta charset="UTF-8">
<title>Information</title>
</head>
<div id="intro">
   <div class="story">
      <div class="float-left">
      <h1 style=text-align:center >References</h1>
       <h1 class= "reference_text" > BrainStem Images." Google Search. Google, n.d. Web. 24 July 2017.
       Cognitive <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Skills of the Brain." Brain Injury Alliance of Utah. N.p., n.d. Web. 24 July 2017.
       <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Temporal Lob Images. Center For NeuroSkills, n.d. Web. 24 July 2017.
</h1>
      </div>
   </div>
   <!--.story-->
</div>
<!--#intro-->
<div id="second">
   <div class="story">
      <div class="bg"></div>
      <div class="float-right">
         <h2 class= "reference_text" >References</h2>
         <p id="help" class= "reference_text" >BrainStem Images." Google Search. Google, n.d. Web. 24 July 2017.
         Cognitive Skills of the Brain." Brain Injury Alliance of Utah. N.p., n.d. Web. 24 July 2017.
         Temporal Lob Images. Center For NeuroSkills, n.d. Web. 24 July 2017.
</p>

      </div>
   </div>
   <!--.story-->
</div>
<!--#second-->
<div id="third">
   <div class="story">
      <div class="float-left">
         <h2 class="reference_text">Why is The Brain So Amazing?</h2>
         <p class= 'reference_text'>Your brain contains about 100</p><br>
         <p class='reference_text'>billion microscopic cells </p>
      </div>
   </div>
   <!--.story-->
</div>
<!--#third-->
<script>
<link href="parallax.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://www.solodev.com/assets/parallax/jquery.localscroll-1.2.7-min.js"></script>
<script src="https://www.solodev.com/assets/parallax/jquery.parallax-1.1.3.js"></script>
<script src="https://www.solodev.com/assets/parallax/jquery.scrollTo-1.4.2-min.js"></script>
<script src="scrolling.js"></script>


</body>
</html>
 """)
]
