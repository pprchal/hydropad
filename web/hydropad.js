function cmd(type, cmd, param) {
    let qcmd = ''
    if(param === undefined){
        qcmd = `${type}/${cmd}`
    }else{
        qcmd = `${type}/${cmd}/${param}`
    }
    runtime.websocket.send(qcmd)
}

let prevDate = new Date()
let prevBPM = 60
function tapTempo() {
    let date = new Date()
    let delta = (date - prevDate) / 1000
    prevDate = date

    // 40 BPM is minimum, wait for next tap
    let bpm = 40
    if(delta >= 1.5){
        console.debug('wait')
    }else{
        // tbetw[0,5] = 60 / BPM(120)
        let currentBPM = 60 / delta
        bpm = Math.floor((60 * currentBPM  + 40 * prevBPM) / 100)
    }

    if(bpm > 180){
        bpm = 180
    }

    if(bpm < 40){
        bpm = 40
    }

    document.getElementById('divBPM').innerText = bpm
}

function startWS(debug){
    runtime.websocket = new WebSocket(runtime.WS_ADDRESS);
    runtime.websocket.binaryType = "arraybuffer"
    runtime.websocket.onmessage = ({ data }) => {
        if(debug != undefined){
            debug.innerText = 'ws: ' + data
        }
    };
}
