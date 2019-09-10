$(document).ready(function() {
  reset();
})

document.getElementById('reset-button').addEventListener("click", function(event){
  event.preventDefault();
  reset();
})

function reset() {
  Array.from(document.getElementsByClassName('form-control')).forEach( item => {
    item.value = 0  ;
  });
}
