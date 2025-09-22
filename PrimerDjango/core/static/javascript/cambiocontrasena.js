const formCambioContrasena = document.getElementById('form-cambioContrasena');
const camposCambioContrasena = {
    oldPassword: {
        required: true,
        regex: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,16}$/,
        error: {
            required: "La contraseña actual es obligatoria.",
            format: "La contraseña actual debe tener entre 8 y 16 caracteres, incluyendo una mayúscula, una minúscula y un número."
        }
    },
    password: {
        required: true,
        matchField: "oldPassword",
        regex: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,16}$/,
        error: {
            required: "La contraseña es obligatoria.",
            format: "La contraseña debe tener entre 8 y 16 caracteres, incluyendo una mayúscula, una minúscula y un número.",
            match: "La nueva contraseña no puede ser igual a la actual."
        }
    },
    confirmPassword: {
        required: true,
        matchField: "password",
        error: {
            required: "La confirmación de la contraseña es obligatoria.",
            match: "Las contraseñas no coinciden."
        }
    }
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

formCambioContrasena.addEventListener("submit", function(event) {
    let valido = true;

    Object.keys(camposCambioContrasena).forEach(campo => limpiarError(campo));

    const oldPassword = formCambioContrasena.oldPassword.value;
    if(camposCambioContrasena.oldPassword.required) {
        if(oldPassword === "") {
            mostrarError("oldPassword", camposCambioContrasena.oldPassword.error.required);
            valido = false;
        } else if(!camposCambioContrasena.oldPassword.regex.test(oldPassword)) {
            mostrarError("oldPassword", camposCambioContrasena.oldPassword.error.format);
            valido = false;
        }
    }

    const password = formCambioContrasena.password.value;
    if(camposCambioContrasena.password.required) {
        if(password === "") {
            mostrarError("password", camposCambioContrasena.password.error.required);
            valido = false;
        } else if(password === oldPassword) {
            mostrarError("password", camposCambioContrasena.password.error.match);
            valido = false;
        } else if(!camposCambioContrasena.password.regex.test(password)) {
            mostrarError("password", camposCambioContrasena.password.error.format);
            valido = false;
        }
    }

    const confirmPassword = formCambioContrasena.confirmPassword.value;
    if(camposCambioContrasena.confirmPassword.required) {   
        if(confirmPassword === "") {
            mostrarError("confirmPassword", camposCambioContrasena.confirmPassword.error.required);
            valido = false;
        } else if(confirmPassword !== password) {
            mostrarError("confirmPassword", camposCambioContrasena.confirmPassword.error.match);
            valido = false;
        }
    }

    if(!valido) {
        event.preventDefault();
    }

});

Object.keys(camposCambioContrasena).forEach(campo => {
    const input = document.getElementById(campo);
    input.addEventListener("input", function() {
        limpiarError(campo);
    });
});

