$(document).ready(function () {
  console.log("ready")
  });

  const detectButton=document.querySelector('#Detect')
  function readURL(input) {
          if (input.files && input.files[0]) {
              var reader = new FileReader();

              reader.onload = function (e) {
                  $('#Picture')
                      .attr('src', e.target.result)

              };
              detectButton.disabled=false;
              $('#Picture').css({'display':'block'})
              reader.readAsDataURL(input.files[0]);
          }
      }
