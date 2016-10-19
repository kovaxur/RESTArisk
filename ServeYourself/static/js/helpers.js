//Get
function getData(URL,callback){
  $.get(URL, function(data){
    if( callback != null) {
      callback(data)
    }
  });
}