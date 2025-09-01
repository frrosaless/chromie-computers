const formOlvido = document.getElementById('form-olvido');
const camposOlvido = {
    email: {
        required: true,
        regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        error: {
            required: "El correo electrónico es obligatorio.",
            format: "El correo electrónico no es válido."
        }
    },
    confirmEmail: {
        required: true,
        matchField: "email",
        error: {
            required: "La confirmación del correo electrónico es obligatoria.",
            match: "Los correos electrónicos no coinciden."
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

formOlvido.addEventListener("submit", function(event) {
    let valido = true;

    Object.keys(camposOlvido).forEach(campo => limpiarError(campo));

    const email = formOlvido.email.value.trim();
    if(camposOlvido.email.required) {
        if(email === "") {
            mostrarError("email", camposOlvido.email.error.required);
            valido = false;
        } else if(!camposOlvido.email.regex.test(email)) {
            mostrarError("email", camposOlvido.email.error.format);
            valido = false;
        }
    }

    const confirmEmail = formOlvido.confirmEmail.value.trim();
    if(camposOlvido.confirmEmail.required) {
        if(confirmEmail === "") {
            mostrarError("confirmEmail", camposOlvido.confirmEmail.error.required);
            valido = false;
        } else if(confirmEmail !== email) {
            mostrarError("confirmEmail", camposOlvido.confirmEmail.error.match);
            valido = false;
        }
    }

    if(!valido) {
        event.preventDefault();
    }

});

Object.keys(camposOlvido).forEach(campo => {
    const input = document.getElementById(campo);
    input.addEventListener("input", function() {
        limpiarError(campo);
    });
});