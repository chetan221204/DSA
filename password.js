function generateOtp(){
    let otp=""
    for(let i=0;i<4;i++){
    otp+=Math.floor(Math.random()*10)
    }
    console.log(otp)
}
generateOtp()
