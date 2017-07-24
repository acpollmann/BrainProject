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
function sendPart(brain_message) {
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

$(document).ready(setupHandlers);
