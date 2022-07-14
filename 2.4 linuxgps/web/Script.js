window.onload = requestNames(); /*calls function to create dropdown*/

//assigns global variables 
var globalProducts = new Array();
var file = "";
var selection = "";
//fucntion for when user selects audio which gethers audio path as guide location 
function selectAudio(){
	selection = document.getElementById("select").value;
	console.log(selection);
	guideMarker()
	playAudiopath(selection)
	}
	//function that gets guide marker
	function guideMarker(){
		console.log(selection)
		eel.getMarker(selection);
	  }

function requestNames(){
	eel.getProduct("hello");

	//calls eels
}

//retuns name for dropdown from python
function returnNames(products){
	console.log(products);
	globalProducts = products;

	dropdown();

}
eel.expose(returnNames)
//creates the dropdown table using array called globalProducts 
function dropdown(){     
	var select = document.getElementById("select");
	console.log(globalProducts);
	console.log("ok");
	for(var i = 0; i < globalProducts.length; i++) {
		var opt = globalProducts[i];
		var el = document.createElement("option");
		el.textContent = opt;
		el.value = opt;
		select.appendChild(el);
	}
}





//sends dat over from create page to python to be put into an SQL database via eels.
function sendMain(file){
	var Gname = document.getElementById('Gname').value;
	var AudioDir = file;
	var LocLAT = document.getElementById('LocLAT').value;
	var LocLON = document.getElementById('LocLON').value;
	if (Gname.length <1)  
	{window.alert("there must be a value Gname and selected a file");
	}
	else if (LocLAT.length <1 || LocLON.length <1)
	{window.alert("there must be a value in both Lat and Long");
	}
	else{	const values = new Array(Gname,AudioDir,LocLAT,LocLON);
		eel.insertm(values)(processAcknowledgement)}

}


//fucntion for making sure we have the file and writing it to screen for user to see.
function processAcknowledgement(r){
	console.log(r);
	file  =  document.getElementById("fileSelected").innerHTML=r;
	console.log(file)

}


function getPathToFile() {
	eel.pythonFunction()(processAcknowledgement)
}

//writes audio path to html
function getTourPath(path){
	console.log(path);
	//correct path to audio
	//based on w3schools
	var x = document.getElementById("myAudio");
      x.innerHTML = "<source src='" + path + "'type='audio/mpeg'>";

}
eel.expose(getTourPath)
//starts funtion to gather audio path data
function playAudiopath(){
	console.log(selection)
	eel.getTourAudio(selection);
}