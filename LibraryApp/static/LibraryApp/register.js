document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submit-btn').onclick = hashPassword;
});

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

function hashPassword(){
    let passField = document.getElementById('id_password');
    let nameField = document.getElementById('id_name');
    let emailField = document.getElementById('id_email');
    let userIdField = document.getElementById('id_user_id');
    let subField = document.getElementById('id_subscription');
    let borrowField = document.getElementById('id_borrowings_remaining');
    let passFormField = document.getElementById('password');
    let nameFormField = document.getElementById('name');
    let emailFormField = document.getElementById('email');
    let userIdFormField = document.getElementById('user_id');
    let subFormField = document.getElementById('subscription');
    let borrowFormField = document.getElementById('borrowings_remaining');
    let form = document.getElementById('register-form');
    let promise = sha256(passField.value);
    Promise.all([promise]).then((value) => {
        nameFormField.value = nameField.value;
        emailFormField.value = emailField.value;
        passFormField.value = value;
        userIdFormField.value = userIdField.value;
        subFormField.value = subField.value;
        borrowFormField.value = borrowField.value;
        form.submit();
    });
}