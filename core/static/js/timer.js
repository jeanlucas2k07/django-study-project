let hoursEl = document.querySelector('#hours');
let minutesEl = document.querySelector('#minutes');
let secondsEl = document.querySelector('#seconds');

let startBtn = document.querySelector('#startBtn');
let resumeBtn = document.querySelector('#resumeBtn');
let pauseBtn = document.querySelector('#pauseBtn');
let resetBtn = document.querySelector('#resetBtn');

let interval;

let hours = 0;
let minutes = 0;
let seconds = 0;
let isPaused = false;

startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pausetimer);
resumeBtn.addEventListener('click', resumetimer);
resetBtn.addEventListener('click', resetTimer);

function startTimer() {
    interval = setInterval(() => {
        if (!isPaused) {
            seconds += 1;

            if (seconds === 60) {
                minutes++;
                seconds = 0;
            }

            if (minutes === 60) {
                hours++;
                minutes = 0;
            }

            hoursEl.textContent = formatTimer(hours);
            minutesEl.textContent = formatTimer(minutes);
            secondsEl.textContent = formatTimer(seconds);
        }


    }, 1000)

    startBtn.style.display = 'none';
    pauseBtn.style.display = 'block';

}

function pausetimer() {
    isPaused = true;

    pauseBtn.style.display = 'none';
    resumeBtn.style.display = 'block';
}

function resumetimer() {
    isPaused = false;

    pauseBtn.style.display = 'block';
    resumeBtn.style.display = 'none';
}

function resetTimer() {
    clearInterval(interval);
    isPaused = false;


    hours = 0;
    minutes = 0;
    seconds = 0;

    hoursEl.textContent = '00';
    minutesEl.textContent = '00';
    secondsEl.textContent = '00';

    startBtn.style.display = 'block';
    resumeBtn.style.display = 'none';
    pauseBtn.style.display = 'none';
    resetBtn.style.display = 'block';

}


function formatTimer(time) {
    return time < 10 ? `0${time}` : time
}