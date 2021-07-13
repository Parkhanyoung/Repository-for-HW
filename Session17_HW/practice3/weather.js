//여기부터 변하는 글자색 관련 코드
function getRandom (min, max){
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
  }
  

function getRandomHexaColor () {
  const hexa = '0123456789abcdef';

  let result= '';
  for (let i=0; i < 6; i++) {
    let b = getRandom(0, 15)
    result += hexa[b];  
  }
  return result;

}


setInterval(() => {
  let value = '#' + getRandomHexaColor()
  document.querySelector("h2").style.color =
  value;
}, 200);



//여기부터 날씨 정보 관련 코드
const input = document.querySelector('#city')
const button = document.querySelector('#submit')
const weatherBox = document.querySelector('#weatherBox')

const API_KEY = 'efef11e4c4f07f87c838d68c6b1f70de'

button.addEventListener('click', async () => {
  try {
    //오늘 날씨 정보
    const res = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${input.value}&appid=${API_KEY}&lang=kr`);

    //오늘 날씨 정보의 세부사항 입력
    const { main, description, icon } = res.data.weather[0]
    const name = res.data.name
    const temp = Math.round(res.data.main.temp - 273.15)
    const feels_like = Math.round(res.data.main.feels_like - 273.15)

    //이후 3일 간의 날씨 정보
    const daily_data = await axios.get(`https://api.openweathermap.org/data/2.5/forecast?q=${input.value}&appid=${API_KEY}`)
    
    //이후 3일 간의 날씨 정보 세부사항 입력
    //이후 3일 간의 날씨 정보를 담기 위한 클래스 생성
    class Predict {
      constructor(index) {
        this.icon = daily_data.data.list[index].weather[0].icon;
        this.main = daily_data.data.list[index].weather[0].main;
        this.temp = Math.round(daily_data.data.list[index].main.temp - 273.15);
      }
    }

    //이후 3일 간의 날씨 정보를 담은 객체 생성
    const tomorrow = new Predict(9)
    const day_after = new Predict(17)
    const two_days_after = new Predict(25)


    //html에 날씨 정보 표시
    weatherBox.innerHTML = `
  <div class="today">오늘 <br> 도시명: ${name} <br>  <img class="icon" src="http://openweathermap.org/img/w/${icon}.png"> 
  <br> 기온: ${temp}°C <br> 체감 기온: ${feels_like}°C
  <br> 기상 상황: ${main}[${description}] </div>
  

  <div class="future_day">내일 <br> <img class="icon" src="http://openweathermap.org/img/w/${tomorrow.icon}.png">
  <br> ${tomorrow.temp}°C <br> ${tomorrow.main}</div>

  <div class="future_day">모레 <br> <img class="icon" src="http://openweathermap.org/img/w/${day_after.icon}.png"> 
  <br> ${day_after.temp}°C <br> ${day_after.main}</div>


  <div class="future_day">글피 <br> <img class="icon" src="http://openweathermap.org/img/w/${two_days_after.icon}.png">
  <br> ${two_days_after.temp}°C <br> ${two_days_after.main}</div>
  `
 


  } catch (error) {
    console.log(error);
  }
})

// Math.round()
// 273.15 temp에서 빼기