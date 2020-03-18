const webcamElement = document.getElementById('webcam');
//const captureVideoButton =document.querySelector('#screenshot .capture-button');
const screenshotButton = document.querySelector('#screenshot-button');


webcamElement.onclick = function() {
          navigator.mediaDevices.getUserMedia(constraints).
            then(handleSuccess).catch(handleError);
};


function handleSuccess(stream) {
        screenshotButton.disabled = false;
        video.srcObject = stream;
}
