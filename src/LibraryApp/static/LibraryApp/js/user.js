document.addEventListener('DOMContentLoaded', function(){
    let activeBtn = document.getElementsByClassName('active')[0];
    document.getElementById("view").innerHTML
        = document.getElementById(activeBtn.id.replace('-btn', '')).innerHTML;

    let browseBtn = document.getElementsByClassName('btn-outline-secondary')[0];
    browseBtn.href = "/browse";
    browseBtn.innerText = 'Browse';
    document.getElementById('submit-btn').onclick = submit;
});

function changeView(element){
    document.getElementsByClassName('active')[0].classList.remove('active');
    element.classList.add('active');
    document.getElementById("view").innerHTML
        = document.getElementById(element.id.replace('-btn', '')).innerHTML;
}

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
    let emailField = document.getElementById('id_email');
    let passFormField = document.getElementById('password');
    let nameFormField = document.getElementById('name');
    let emailFormField = document.getElementById('email');
    let form = document.getElementById('edit-form');
    if(passField.value !== '') {
        let promise = sha256(passField.value);
        Promise.all([promise]).then((value) => {
            nameFormField.value = nameField.value;
            emailFormField.value = emailField.value;
            passFormField.value = value;
            form.submit();
        });
    }
    else{
        nameFormField.value = nameField.value;
        emailFormField.value = emailField.value;
        passFormField.value = passField.value;
        form.submit();
    }
}