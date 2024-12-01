// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}


/*
//Get current stored JSON file for User 
function loadCurrentUser(){
  let fileSystemJSON=window.sessionStorage.getItem("currentUserJSON");
  if (fileSystemJSON === null){
    setJSON("{}");
  }
  else{
    setJSON(fileSystemJSON);
  }
}
//Load the database with data from JSON
function setJSON(JSONString){
  incomingJSON=JSON.parse(JSONString);
  console.log(incomingJSON);
    if (incomingJSON!=null && incomingJSON.username){
      saveuser.username=incomingJSON.username;
      console.log(saveuser.username)
      window.sessionStorage.setItem("currentUserJSON",JSON.stringify(incomingJSON));
  }
}


/*
const saveuser = new XMLHttpRequest();

saveuser.open('GET','/api/login')
saveuser.setRequestHeader('Content-Type','application/json');
saveuser.onload = () => {
  if (saveuser.status === 200){
    const data = JSON.parse(saveuser.responseText);
    console.log(data);
  }
};
saveuser.send();
*/