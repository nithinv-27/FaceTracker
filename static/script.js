const detect_btn = document.querySelector("#detect_btn");
const stop_btn = document.querySelector("#stop_btn");
const img = document.querySelector(".box");
const on_detect = document.querySelector(".on-detect")

detect_btn.addEventListener("click", ()=>{
    img.src = "http://127.0.0.1:8000/capture";
    detect_btn.style.display = "none";
    on_detect.style.display = "block";    
})

stop_btn.addEventListener("click", ()=>{
    const response = fetch("http://127.0.0.1:8000/stop_capture");
    img.src = "";
    on_detect.style.display = "none";
    detect_btn.style.display = "block";
});



`WEBSOCKETS`
// const socket = new WebSocket("http://127.0.0.1:8000/ws");
// inp_btn.addEventListener("click", async (event)=>{
//     stream = await navigator.mediaDevices.getUserMedia({video:true});
//     inp_video_box.srcObject = stream;
//     setInterval(()=>{
//         const mediaRecorder = new MediaRecorder(stream);
//         mediaRecorder.start();

//         videoChunks = [];

//         mediaRecorder.addEventListener("dataavailable", (event)=>{
//             videoChunks.push(event.data);
//         })

//         mediaRecorder.addEventListener("stop", async()=>{
//             const videoBlob = new Blob(videoChunks, {type:"video/webm"});
//             const buffer = await videoBlob.arrayBuffer();
//             socket.send(buffer);
//         })

//         setTimeout(()=>{
//             mediaRecorder.stop();
//         }, 2000);
//     },2000);

//     socket.addEventListener("message",(event)=>{
//         const videoBlob = new Blob([event.data], {type:"video/webm"});
//         out_video_box.src = URL.createObjectURL(videoBlob);
//     })
// })


