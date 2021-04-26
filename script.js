let days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
let times = ["7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"];
//create grid
let grid=document.querySelector("#grid");
//creates 15 rows
for (i=0;i<15;i++){
    let row = document.createElement("div");
    row.setAttribute("class","row");
    //creates 8 columns
    for (j=0;j<8;j++){
        let col = document.createElement("div");
        col.setAttribute("class","col");
        row.appendChild(col);
        //writes days of the week in top row
        if (i==0 && j>0){
          col.innerHTML=days[j-1];
        }
        //writes time slots in first col
        else if(j==0 && i>0){
            col.innerHTML = times[i-1]
        }
        //assigns day.time ids to boxes 
        else if (i>0 && j>0){
        col.setAttribute('id', `${days[j-1]}.${times[i-1]}`);    
        }
    }
    grid.appendChild(row);
}

let form = document.querySelector("#inputForm");
let user = document.querySelector("#userName");
let color = document.querySelector("#colorSelect");
let eventName = document.querySelector("#eventName");
let day = document.querySelector("#daySelect");
let time = document.querySelector("#timeSelect");

form.addEventListener("submit", createEvent);

function createEvent(e){
    e.preventDefault();
    //creates div
    let newEvent = document.createElement("div");
    newEvent.setAttribute("class","newEvent");
    //sets color,title of event
    newEvent.style.backgroundColor=color.value;
    let title = document.createElement("div");
    title.innerHTML=eventName.value;
    console.log(title);
    newEvent.appendChild(title);
    let person = document.createElement("div");
    person.innerHTML = user.value;
    console.log(person);
    newEvent.appendChild(person);
    //places event in schedule
    let gridloc = document.getElementById(`${day.value}.${time.value}`);
    console.log(gridloc);
    gridloc.appendChild(newEvent);
}
