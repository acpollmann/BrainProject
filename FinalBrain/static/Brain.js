/*$('.mapping').mouseover(function() {
    alert($(this).attr('id'));
}
$('.mapping').click(function() {
    alert($(this).attr('id'));
});

var map = document.getElementById("Map");
map.addEventListener("click", function(e) {
    callAction(e.target);
});

function callAction(area) {
    alert(area.title);
}
*/
// pill.js: Methods for handling pill requests
counter = function() {
    var value = $('#text').val();

    if (value.length == 0) {
        $('#wordCount').html(0);
        return;
    }

    var regex = /\s+/gi;
    var wordCount = value.trim().replace(regex, ' ').split(' ').length;

    $('#wordCount').html(wordCount);
};

$(document).ready(function() {
    $('#count').click(counter);
    $('#text').change(counter);
    $('#text').keydown(counter);
    $('#text').keypress(counter);
    $('#text').keyup(counter);
    $('#text').blur(counter);
    $('#text').focus(counter);
});
function setupHandlers(){
  $('#temporal_lobe').click(sendTemp);
  $('#img__description').click(sendTemp);
  $('#frontal_lobe').click(sendFront);
  $('#img__description1').click(sendFront);
  $('#parietal_lobe').click(sendPar);
  $('#img__description2').click(sendPar);
  $('#occipital_lobe').click(sendOcc);
  $('#img__description3').click(sendOcc);
  $('#cerebellum').click(sendCere);
  $('#img__description4').click(sendCere);
  $('#spinal_cord').click(sendSpin);
  $('#img__description5').click(sendSpin);
}

function sendTemp(){
/*$(this).attr('id')*/
$('#explanation').css('display', 'none')
$('#temporal').css('display', 'block')
$('#frontal').css('display', 'none')
$('#parietal').css('display', 'none')
$('#occipital').css('display', 'none')
$('#cereb').css('display', 'none')
$('#spinal').css('display', 'none')

}
function sendFront(){
  $('#explanation').css('display', 'none')
  $('#temporal').css('display', 'none')
  $('#frontal').css('display', 'block')
  $('#parietal').css('display', 'none')
  $('#occipital').css('display', 'none')
  $('#cereb').css('display', 'none')
  $('#spinal').css('display', 'none')
}
function sendPar(){
  $('#explanation').css('display', 'none')
  $('#temporal').css('display', 'none')
  $('#frontal').css('display', 'none')
  $('#parietal').css('display', 'block')
  $('#occipital').css('display', 'none')
  $('#cereb').css('display', 'none')
  $('#spinal').css('display', 'none')
}
function sendOcc(){
  $('#explanation').css('display', 'none')
  $('#temporal').css('display', 'none')
  $('#frontal').css('display', 'none')
  $('#parietal').css('display', 'none')
  $('#occipital').css('display', 'block')
  $('#cereb').css('display', 'none')
  $('#spinal').css('display', 'none')

}
function sendCere(){
  $('#explanation').css('display', 'none')
  $('#temporal').css('display', 'none')
  $('#frontal').css('display', 'none')
  $('#parietal').css('display', 'none')
  $('#occipital').css('display', 'none')
  $('#cereb').css('display', 'block')
  $('#spinal').css('display', 'none')
}
function sendSpin(){
  $('#explanation').css('display', 'none')
  $('#temporal').css('display', 'none')
  $('#frontal').css('display', 'none')
  $('#parietal').css('display', 'none')
  $('#occipital').css('display', 'none')
  $('#cereb').css('display', 'none')
  $('#spinal').css('display', 'block')
}

$(document).ready(setupHandlers)

/*function sendPart(brain_message) {
  // Tell jQuery to POST a message
  $.post("/", {"brain_part": brain_message}, function(data) {
    addTextToPage(JSON.parse(data).message);
  });
}

function addTextToPage(text_string) {
  console.log(text_string);
  if (text_string == "temporal_lobe") {
    $("#temporal_message").css("display", "block");
    $("#frontal_message").css("display", "none");
}
  else if (text_string == "frontal_lobe") {
    $("#frontal_message").css("display", "block");
    $("#frontal_message").css("display", "none");
}}

function sendTemporalLobe() {
  sendPart("temporal_lobe");
}

function sendFrontalLobe() {
  sendPart("frontal_lobe");
}

function setupHandlers() {
  $('#temporal_lobe').on('click', sendTemporalLobe);
  $('#frontal_lobe').on('click', sendFrontalLobe);
}

$(document).ready(setupHandlers);*/
