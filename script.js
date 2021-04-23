let days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
let times = ["7:00", "7:30","8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00"];
//create grid
let grid=document.querySelector("#grid");
//creates 28 rows
for (i=0;i<28;i++){
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
