getRandom = (min, max) => {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
  }
  

function getRandomHexaColor () {
  const hexa = '0123456789abcdef';

  result= '';
  for (i=0; i < 6; i++) {
    b = getRandom(0, 15)
    result += hexa[b];  
  }
  return result;

}


setInterval(() => {
  value = '#' + getRandomHexaColor()
  document.querySelector('body').style.backgroundColor =
  value;
}, 100);


const clockContent = document.querySelector('.now');


// Sat May 22 2021 23:03:10 GMT+0900 (대한민국 표준시)
function getCurrentTime () {
  const date = new Date();
  // console.log(date)
  let year = date.getFullYear();
  let month = date.getMonth();
  let day = date.getDate();
  let hour = date.getHours();
  let minute = date.getMinutes();
  let second = date.getSeconds();

  if (month < 10) {
    month = '0' + month
  }
  if (day < 10) {
    day = '0' + day
  }
  if (hour < 10) {
    hour = '0' + hour
  }
  if (minute < 10) {
    minute = '0' + minute
  }
  if (second < 10) {
    second = '0' + second
  }

  result = `${year}년 ${month}월 ${day}일 ${hour}시 ${minute}분 ${second}초`;
  clockContent.innerText = result;
}


function initClock() {
  getCurrentTime();
  setInterval(getCurrentTime, 1000);
};

initClock();