
     // Instantiating EasyHTTP
const http = new EasyHTTP;

const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    phone:  document.getElementById("phone").value,
    message:  document.getElementById("message").value,
}

// Post prototype method 
http.post(
    'http://127.0.0.1:8000/products/create',
    data)
  
    // resolving promise for response data
    .then(data => console.log(data))
  
    // resolving promise for error
    .catch(err => console.log(err));

           