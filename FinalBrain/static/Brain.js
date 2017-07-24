/*explanations = {'1':h,'2':he,'3':hel,'4':hiya,:'5':hello,'6':hooper}*/
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
$('#explanation').text('Temporal Lobe')
}
function sendFront(){
$('#explanation').text('Frontal Lobe')
}
function sendPar(){
$('#explanation').text('Parietal Lobe')
}
function sendOcc(){
  $('#explanation').text('Occipital Lobe')

}
function sendCere(){
  $('#explanation').text('Cerebellum')
}
function sendSpin(){
  $('#explanation').text('Spinal Cord')
}

$(document).ready(setupHandlers)
