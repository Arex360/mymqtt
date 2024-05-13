let imageFile = "sjksdjklsdjklasdjklasdjklasdjasdkljasdkljasdkljasdkljasdkljasdklasdjklasdjklasdjklasdjlasdkkljklfjsdkl"
let fbLen = imageFile.length
for (let n=0;n<fbLen;n=n+(5)) {
    if (n+(5)<fbLen) {
      let str = imageFile.substring(n, n+(5));
      console.log(str)
    }
    else if (fbLen%(5)>0) {
      let remainder = fbLen%(5);
      str = imageFile.substring(n, n+remainder);
      console.log(str)
    }
  }