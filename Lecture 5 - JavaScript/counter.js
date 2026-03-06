let totalSeconds = 180;
let resetting = false;

function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

document.addEventListener("DOMContentLoaded", function() {
    const display = document.querySelector("#timer");
    const message = document.querySelector("#message");

    display.innerHTML = formatTime(totalSeconds);

    setInterval(function() {
        if (resetting) return;

        totalSeconds--;
        display.innerHTML = formatTime(totalSeconds);

        if (totalSeconds === 0) {
            resetting = true;
            message.style.display = "block";
            setTimeout(function() {
                message.style.display = "none";
                totalSeconds = 180;
                display.innerHTML = formatTime(totalSeconds);
                resetting = false;
            }, 2000);
        }
    }, 1000);
});
    