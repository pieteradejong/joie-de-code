var ele = document.getElementById("strform");
if(ele.addEventListener){
    ele.addEventListener("submit", formHandler, false);  //Modern browsers
}else if(ele.attachEvent){
    ele.attachEvent('onsubmit', formHandler);            //Old IE
}

function formHandler(event) {
  // alert("handled!");
  event.preventDefault();
  var str1 = $("input[name='str1']").val();
  var str2 = $("input[name='str2']").val();
  console.log("str1: ", str1);
  console.log("str2: ", str2);

  sendStrings(str1, str2);
}

function sendStrings(str1, str2) {
  $.ajax({
        url: '/submit',
        data: {'str1': str1, 'str2': str2},
        type: 'GET',
        success: function(response) {
            console.log(response);
            alert(response);
        },
        error: function(error) {
            console.log(error);
            alert(error);
        }
    });  
}

$( "strfffd orm" ).submit(function( event ) {
      event.preventDefault();
      var str1 = $("input[name='str1']").val();
      var str2 = $("input[name='str2']").val();
      alert("pressed!");
      console.log("str1: ", str1);
      console.log("str2: ", str2);
        $.ajax({
            url: '/submit',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

function onSubmit() {
  var str1 = document.getElementById("str1").value;
  var str2 = document.getElementById("str2").value;
  
  // submit reqest to app
  var data = {
    'str1': str1,
    'str2': str2
  };
  submitAsyncPost(data);
}

function submitAsyncPost(data) {
    var xmlhttpRequest = new XMLHttpRequest();
    
    xmlhttpRequest.onreadystatechange = function() {
        if (xmlhttpRequest.readyState == XMLHttpRequest.DONE ) {
           if(xmlhttpRequest.status == 200){
               document.getElementById("distance").innerHTML = xmlhttpRequest.responseText;
           }
           else if(xmlhttpRequest.status == 400) {
              alert('There was an error 400')
           }
           else {
               alert('error returned (other than 400)')
           }
        }
    }

    xmlhttpRequest.open('POST', '/submit', true);
    xmlhttpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    xmlhttpRequest.send(data);
}

