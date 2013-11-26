
console.log("test")

var userChange = function () {
	console.log("user changed");
}

SimpleWebRTC.prototype.sampleHandlePeerStreamAdded = SimpleWebRTC.prototype.handlePeerStreamAdded;
SimpleWebRTC.prototype.handlePeerStreamAdded = function (peer) {
	console.log("in my handlePeerStreamAdded", peer);
	this.sampleHandlePeerStreamAdded(peer)
    
};

var webrtc = new SimpleWebRTC({
  localVideoEl: 'localVideo',
  remoteVideosEl: 'remoteVideo',
  autoRequestMedia: true
});

webrtc.on('readyToCall', function () {
  var roomName = "{{ room_name }}";
  webrtc.joinRoom(roomName);
});

/**
$('#remoteVideo').bind('contentchanged', function() {
  // do something after the div content has changed
  alert('woo');
});
**/
