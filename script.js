const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask(){
    /**Browser Message when empty*/
    if (inputBox.value === ''){
        alert("Type smoething!");
    }
    else{
        /**Creating Task from Input Text*/
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        /**For deleting a Task with a cross item*/
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    /**Clearing Input*/
    inputBox.value = "";
    /**When a Task is addet, it will be saved with this function*/
    saveData();
}
/**Function to mark or remove Tasks which are done*/
listContainer.addEventListener("click", function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

/**Most important for this course: save the Data!*/
function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}
function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();