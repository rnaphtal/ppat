
console.log("test")

var userChange = function () {
	console.log("user changed");
}

var currentParticipants = {}

var loadData = function(data) {
	currentParticipants={}
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
			});
}



/**
$('#remoteVideo').bind('contentchanged', function() {
  // do something after the div content has changed
  alert('woo');
});
**/
