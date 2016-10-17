//Get
function getData(URL,callback){
  $.get(URL, function(data){
    callback(data)
  });
}