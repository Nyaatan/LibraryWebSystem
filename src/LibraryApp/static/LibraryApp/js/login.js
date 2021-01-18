window.onload = function () {
    document.getElementById('submit-btn').onclick = submit;
};

async function sha256(message) {
    // encode as UTF-8
    const msgBuffer = new TextEncoder().encode(message);

    // hash the message
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // convert bytes to hex string
    return hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');
}

function submit(){
    let passField = document.getElementById('id_password');
    let nameField = document.getElementById('id_name');
    let passFormField = document.getElementById('password');
    let nameFormField = document.getElementById('name');
    let form = document.getElementById('login-form');
    let promise = sha256(passField.value);
    Promise.all([promise]).then((value) => {
        nameFormField.value = nameField.value;
        passFormField.value = value;
        form.submit();
    });
}