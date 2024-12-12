const inp_btn = document.querySelector("#inp_btn");
const out_btn = document.querySelector("#out_btn");
const inp_box = document.querySelector("#input_box");
const out_box = document.querySelector("#output_box");

inp_btn.addEventListener("click", ()=>{

    // Stop the video if it's already playing a different stream
    // if (inp_box.srcObject) {
    //     const stream = inp_box.srcObject;
    //     const tracks = stream.getTracks();
    //     tracks.forEach(track => track.stop());
    // }

    // Fetch the MJPEG stream and set it as the source
    inp_box.src = "http://127.0.0.1:8000/capture";
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


