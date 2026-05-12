let timerEl = document.querySelector('#timer')
let isPausedEl = document.querySelector('#isPaused')

let hoursEl = document.querySelector('#hours');
let minutesEl = document.querySelector('#minutes');
let secondsEl = document.querySelector('#seconds');

let startBtn = document.querySelector('#startBtn');
let resumeBtn = document.querySelector('#resumeBtn');
let pauseBtn = document.querySelector('#pauseBtn');
let finishBtn = document.querySelector('#finishBtn');

let interval;

let hours = 0;
let minutes = 0;
let seconds = 0;
let isPaused = false;

startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pausetimer);
resumeBtn.addEventListener('click', resumetimer);
finishBtn.addEventListener('click', finishTimer);

function startTimer() {
    timerEl.classList.add('active')

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
    finishBtn.style.display = 'block';

    isPausedEl.style.display = 'none';
}

function pausetimer() {

    timerEl.classList.remove('active')

    isPaused = true;

    isPausedEl.style.display = 'block';

    pauseBtn.style.display = 'none';
    resumeBtn.style.display = 'block';
}

function resumetimer() {

    timerEl.classList.add('active')

    isPaused = false;

    pauseBtn.style.display = 'block';
    resumeBtn.style.display = 'none';

    isPausedEl.style.display = 'none';
}

function finishTimer(event) {

    event.preventDefault();

    timerEl.classList.remove('active')

    clearInterval(interval);

    isPaused = false;

    let totalSeconds =
        (hours * 3600) +
        (minutes * 60) +
        seconds;

    sessionStorage.setItem('study_time', totalSeconds);

    event.target.closest('form').submit();
}

function formatTimer(time) {
    return time < 10 ? `0${time}` : time
}