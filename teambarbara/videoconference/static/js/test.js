
console.log("test")

var userChange = function () {
	console.log("user changed");
}

var currentParticipants = {}

var loadData = function(data) {
	currentParticipants={}
	console.log("another Hello");
	console.log(data.participants);
	participants = data.participants;
	for(i=0;i<participants.length;i++){
		if ("{{myname}}" != participants[i]){
			updateVideoID(participants[i]);
		}
	}

}

var updateVideoID = function (name){
	$.getJSON('/get_videoID/'+participants[i], function(p_id){
				currentParticipants[name]=p_id.videoID;
            	addIndivNames(name);
			});
}

var addIndivNames = function (participant) {
	videoID = currentParticipants[participant];
	clickBehavior = toggleVideoAndColor(videoID);
	$(".people_names").html($(".people_names").html()+'<button id=' + 'name_' + videoID + ' onclick=' + clickBehavior+ '>' + participant + '</button>');
	


	console.log("participant: " + participant);
		
	console.log("Added partarticipant");
}

var toggleVideoAndColor = function(videoID) {
	toggleVideo = "$('video[id^=" + videoID + "]').toggle();";
	toggleColor = "$('video[id^=" + 'name_' + videoID + "]').toggleClass('green');";
	return toggleVideo + toggleColor;

} 



/**
$('#remoteVideo').bind('contentchanged', function() {
  // do something after the div content has changed
  alert('woo');
});
**/
