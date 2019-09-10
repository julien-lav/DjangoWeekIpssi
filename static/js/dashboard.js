document.getElementById('reset-button').addEventListener("click", function(event){
  event.preventDefault();
  Array.from(document.getElementsByClassName('form-control')).forEach( item => {
    item.value = null;
  });
})
