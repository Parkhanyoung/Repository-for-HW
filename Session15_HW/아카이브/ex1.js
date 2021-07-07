const $ulElement = document.querySelector('ul');

$ulElement.addEventListener("click",(event) => {
    const $target = event.target;
    if($target.classList.contains('close')){
        const $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
        deleteTodoList('todos', $parentTarget.childNodes[0].textContent);
    }
    $target.classList.toggle('checked');
})

function newElement() {

    const inputValue = document.getElementById("myInput").value;
    const ulElement = document.getElementById('myUL');

    if (inputValue === '') {
        alert("You must write something!");
    } else {
        ulElement.insertAdjacentHTML('Beforeend', `<li><span>${inputValue}</span><span class="close">&#215;</span>
        </li>`)
        addTodoList('todos', inputValue);
        
    }
    document.getElementById("myInput").value = "";
}

// 두번째 실습


function init() {
    const todoList = getTodoList('todos');
    console.log('투두리스트 시작시' +todoList);
    for (let i=0; i < todoList.length; i++) {
        $ulElement.insertAdjacentHTML('Beforeend', `<li><span>${todoList[i]}</span><span class="close">&#215;</span>
        </li>`);
    }
}

function getTodoList(key) {
    const todos1 = localStorage.getItem(key);
    console.log(todos1)
    if (todos1 === '' || todos1 === null) {
        return []} else {
            return localStorage.getItem(key).split(",")
        }
    //정답
    // return localStorage.getItem(key) ?  localStorage.getItem(key).split(",") : [];
} 


//return 값은 추가된 새 배열 
function addTodoList(key, value) {
    const todoList = getTodoList(key);
    todoList.push(value);
    localStorage.setItem(key, todoList); 
}// 정답
// return localStorage.setItem(key, [...todoList, value])


// key  >> 로컬 스토리지 정보를 가져옴 >> 어레이에서 밸류에 해당되는 값을 지워서 나머지 배열을 리턴
function deleteTodoList(key, value) {
    const todoList = getTodoList(key)
    for (i=0; i<todoList.length; i++) {
        if (todoList[i] === value) {
            todoList.splice(i, 1);
        }
    
    }
    localStorage.setItem(key, todoList); 
    // 정답
    // return localStorage.setItem(key.todoList.filter(todo => todo !== value))
}


function toggle() {
    toggleTarget = document.getElementById('myUL');
    toggleBtn = document.getElementById('toggleBtn');
    if (toggleTarget.style.display !== 'none') {
        toggleTarget.style.display = 'none';   
        toggleBtn.textContent = '보이기';
    } else {
        toggleTarget.style.display = 'block';
        toggleBtn.textContent = '숨기기';
    }
}


function darkMode() {
    const body = document.body;
    const header = document.getElementsByClassName('header')[0];
    const darkModeBtn = document.getElementById('darkMode')
    if (body.className !== 'darkMode') {
        body.className = 'darkMode';
        header.style.backgroundColor = '#555453'
        darkModeBtn.textContent = '화이트';
    } else {
        body.classList.remove('darkMode');
        darkModeBtn.textContent = '다크'
        header.style.backgroundColor = '#f44336'
    }
}



function move() {
  let i = 0;  
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 30);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
        elem.innerHTML = width + "%";
      }
    }
  }
}

init()