const show_password = () => {
    const password_checkbox = document.getElementById('show_password');
    const password_field = document.getElementById('password');
    
    if (password_checkbox.checked) {
        password_field.type = 'text';
    } else {
        password_field.type = 'password';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("show_password").addEventListener("change", show_password);
});

export default show_password;