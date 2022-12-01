function startTimer(duration, display) {

  var timer = duration, horas = 0, minutos = 1, segundos;
  const tempo = document.getElementById("#tempo");

  setInterval(function(){
    horas = parseInt(horas);
    minutos = parseInt(minutos);
    segundos = parseInt(timer % 60, 10);

    if(segundos == 0 && minutos > 0){
      minutos = minutos - 1;
      segundos = 59
    }

    if(minutos == 0 && horas > 0){
      horas = horas - 1;
      minutos = 59
    }

    if(minutos == 0 && segundos == 0 ){
      alert("Acabou o tempo");
    }

    horas = horas < 10 ? "0" + horas : horas;
    minutos = minutos < 10 ? "0" + minutos : minutos;
    segundos = segundos < 10 ? "0" + segundos : segundos;

    display.textContent = horas + ":" + minutos + ":" + segundos;

    if(--timer < 0) {
      timer = duration;
    }

  }, 1000)
}

function iniciar() {
  var duration = 60 * 4;
  var display = document.querySelector("#tempo");

  startTimer(duration, display);
}
