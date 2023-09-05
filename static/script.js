// const img = document.querySelector("#generatedImage");
// const download = document.getElementById("download");

// download.addEventListener('click', async ()=>{
//     const response = await fetch(img.src);
//     const blob = await response.blob();
//     const downloadLink = document.createElement("a");
//     downloadLink.href = URL.createObjectURL(blob);
//     downloadLink.download = "generatedImage.jpg";
//     downloadLink.click();
// })