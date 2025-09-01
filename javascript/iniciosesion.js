// Validación de formulario de inicio de sesión
const formLogin = document.getElementById("form-iniciosesion");
const camposLogin = {
    username: {
        required: true,
        regex: /^[A-Za-z0-9_]{3,20}$/,
        error: {
            required: "El nombre de usuario es obligatorio.",
            length: "El nombre de usuario debe tener entre 3 y 20 caracteres.",
            format: "Solo se permiten letras, números y guiones bajos."
        }
    },
    password: {
        required: true,
        regex: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,16}$/,
        error: {
            required: "La contraseña es obligatoria.",
            format: "La contraseña debe tener entre 8 y 16 caracteres, incluyendo una mayúscula, una minúscula y un número."
        }
    },
};

function mostrarError(id, mensaje) {
    const input = document.getElementById(id);
    input.classList.add("is-invalid");
    document.getElementById("error-" + id).textContent = mensaje;
}

function limpiarError(id) {
    const input = document.getElementById(id);
    input.classList.remove("is-invalid");
    document.getElementById("error-" + id).textContent = "";
}  

formLogin.addEventListener("submit", function(event) {
    let valido = true;

    Object.keys(camposLogin).forEach(campo => limpiarError(campo));

    const username = formLogin.username.value.trim();
    if(camposLogin.username.required) {
        if(username === "") {
            mostrarError("username", camposLogin.username.error.required);
            valido = false;
        } else if(username.length < 3 || username.length > 20) {
            mostrarError("username", camposLogin.username.error.length);
            valido = false;
        } else if(!camposLogin.username.regex.test(username)) {
            mostrarError("username", camposLogin.username.error.format);
            valido = false;
        }
    }

    const password = formLogin.password.value.trim();
    if(camposLogin.password.required) {
        if(password === "") {
            mostrarError("password", camposLogin.password.error.required);
            valido = false;
        } else if(!camposLogin.password.regex.test(password)) {
            mostrarError("password", camposLogin.password.error.format);
            valido = false;
        }
    }

    if(!valido) {
        event.preventDefault();
    }

});

Object.keys(camposLogin).forEach(campo => {
    const input = document.getElementById(campo);
    input.addEventListener("input", function() {
        limpiarError(campo);
    });
});