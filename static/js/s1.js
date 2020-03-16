// document.getElementById("demo").innerHTML = navigator.platform;
var mytable = document.querySelector('#demo');

createTable(mytable, 3, 4);

function createTable(parent, cols, rows){
    var table = document.createElement('table');

    for (var i = 0; i < rows; i++){
        var tr = document.createElement('tr');

        for (var j = 0; j < cols; j++){
            var td = document.createElement('dt');
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    parent.appendChild(table);
}