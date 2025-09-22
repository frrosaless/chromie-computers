// Validacion formulario registro
const form = document.getElementById("form-registro");
const campos = {
    first_name: {
        required: true,
        // Solo letras y tildes, sin espacios
        regex: /^[A-Za-zÁÉÍÓÚáéíóúÑñ]{3,50}$/,
        error: {
            required: "El nombre es obligatorio.",
            length: "El nombre debe tener entre 3 y 50 caracteres.",
            format: "Solo se permiten letras y tildes, sin espacios."
        }
    },
    last_name: {
        required: true,
        // Solo letras y tildes, sin espacios
        regex: /^[A-Za-zÁÉÍÓÚáéíóúÑñ]{3,50}$/,
        error: {
            required: "El apellido es obligatorio.",
            length: "El apellido debe tener entre 3 y 50 caracteres.",
            format: "Solo se permiten letras y tildes, sin espacios."
        }
    },
    username: {
        required: true,
        regex: /^[A-Za-z0-9_]{3,20}$/,
        error: {
            required: "El nombre de usuario es obligatorio.",
            length: "El nombre de usuario debe tener entre 3 y 20 caracteres.",
            format: "Solo se permiten letras, números y guiones bajos."
        }
    },
    email: {
        required: true,
        regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        error: {
            required: "El correo electrónico es obligatorio.",
            format: "El correo electrónico no es válido."
        }
    },
    password1: {
        required: true,
        regex: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,16}$/,
        error: {
            required: "La contraseña es obligatoria.",
            format: "La contraseña debe tener entre 8 y 16 caracteres, incluyendo una mayúscula, una minúscula y un número."
        }
    },
    password2: {
        required: true,
        matchField: "password",
        error: {
            required: "La confirmación de la contraseña es obligatoria.",
            match: "Las contraseñas no coinciden."
        }
    },
    birthdate: {
        required: true,
        error: {
            required: "La fecha de nacimiento es obligatoria.",
            age: "Debes tener al menos 13 años para registrarte."
        }
    },
    address: {
        required: false,
        regex: /^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s,.-]{0,100}$/,
        error: {
            length: "La dirección debe tener hasta 100 caracteres.",
            format: "La dirección contiene caracteres no permitidos."
        }
    }
};

// ...existing code...
function mostrarError(id, mensaje) {
    const input = document.getElementById(id);
    if (input) input.classList.add("is-invalid");
    const errorSpan = document.getElementById("error-" + id);
    if (errorSpan) errorSpan.textContent = mensaje;
}

function limpiarError(id) {
    const input = document.getElementById(id);
    if (input) input.classList.remove("is-invalid");
    const errorSpan = document.getElementById("error-" + id);
    if (errorSpan) errorSpan.textContent = "";
}
// ...existing code...

/*
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
*/
form.addEventListener("submit", function(event) {
    let valido = true;

    Object.keys(campos).forEach(campo => limpiarError(campo));

    const first_name = form.first_name.value.trim();
    if(campos.first_name.required) {
        const first_name = form.first_name.value.trim();
        if(first_name === "") {
            mostrarError("first_name", campos.first_name.error.required);
            valido = false;
        } else if(first_name.length < 3 || first_name.length > 50) {
            mostrarError("first_name", campos.first_name.error.length);
            valido = false;
        } else if(!campos.first_name.regex.test(first_name)) {
            mostrarError("first_name", campos.first_name.error.format);
            valido = false;
        }
    }

    const last_name = form.last_name.value.trim();
    if(campos.last_name.required) {
        const last_name = form.last_name.value.trim();
        if(last_name === "") {
            mostrarError("last_name", campos.last_name.error.required);
            valido = false;
        } else if(last_name.length < 3 || last_name.length > 50) {
            mostrarError("last_name", campos.last_name.error.length);
            valido = false;
        } else if(!campos.last_name.regex.test(last_name)) {
            mostrarError("last_name", campos.last_name.error.format);
            valido = false;
        }
    }

    const username = form.username.value.trim();
    if(campos.username.required) {
        if(username === "") {
            mostrarError("username", campos.username.error.required);
            valido = false;
        } else if(username.length < 3 || username.length > 20) {
            mostrarError("username", campos.username.error.length);
            valido = false;
        } else if(!campos.username.regex.test(username)) {
            mostrarError("username", campos.username.error.format);
            valido = false;
        }
    }

    const email = form.email.value.trim();
    if(campos.email.required) {
        if(email === "") {
            mostrarError("email", campos.email.error.required);
            valido = false;
        } else if(!campos.email.regex.test(email)) {
            mostrarError("email", campos.email.error.format);
            valido = false;
        }
    }

    const password1 = form.password1.value;
    if(campos.password1.required) {
        if(password1 === "") {
            mostrarError("password1", campos.password1.error.required);
            valido = false;
        } else if(!campos.password1.regex.test(password1)) {
            mostrarError("password1", campos.password1.error.format);
            valido = false;
        }
    }

    const password2 = form.password2.value;
    if(campos.password2.required) {
        if(password2 === "") {
            mostrarError("password2", campos.password2.error.required);
            valido = false;
        } else if(password2 !== password1) {
            mostrarError("password2", campos.password2.error.match);
            valido = false;
        }
    }

    const birthdate = form.birthdate.value;
    if(campos.birthdate.required) {
        if(birthdate === "") {
            mostrarError("birthdate", campos.birthdate.error.required);
            valido = false;
        } else {
            const fechaNacimiento = new Date(birthdate);
            const hoy = new Date();
            const edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
            const mes = hoy.getMonth() - fechaNacimiento.getMonth();
            if(mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
                edad--;
            }
            if(edad < 13) {
                mostrarError("birthdate", campos.birthdate.error.age);
                valido = false;
            }
        }
    }

    const address = form.address.value.trim();
    if(address) {
        if(address.length > 100) {
            mostrarError("address", campos.address.error.length);
            valido = false;
        } else if(!campos.address.regex.test(address)) {
            mostrarError("address", campos.address.error.format);
            valido = false;
        }
    }

    if(!valido) {
        event.preventDefault();
    }

});

// ...existing code...
Object.keys(campos).forEach(campo => {
    const input = document.getElementById(campo);
    if (input) {
        input.addEventListener("input", function() {
            limpiarError(campo);
        });
    }
});
// ...existing code...

/*
Object.keys(campos).forEach(campo => {
    const input = document.getElementById(campo);
    input.addEventListener("input", function() {
        limpiarError(campo);
    });
});
*/