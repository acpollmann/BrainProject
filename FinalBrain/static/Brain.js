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
function setupHandlers(){
  $('#temporal_lobe').click(sendTemp);
  $('#frontal_lobe').click(sendFront);
  $('#parietal_lobe').click(sendPar);
  $('#occipital_lobe').click(sendOcc);
  $('#cerebellum').click(sendCere);
  $('#spinal_cord').click(sendSpin);
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
